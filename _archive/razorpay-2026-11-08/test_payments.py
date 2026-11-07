#!/usr/bin/env python3
"""Checks the payment and form endpoints against a running Worker (wrangler dev or the deployed URL).
usage: python3 tools/test_payments.py [base_url] [--send-email]
Uses the TEST Razorpay keys from .env.local; no secret is printed. Without --send-email no mail is sent."""
import sys, json, hmac, hashlib, urllib.request, urllib.error, os
base = next((a for a in sys.argv[1:] if a.startswith('http')), 'http://127.0.0.1:8787').rstrip('/')
send_email = '--send-email' in sys.argv
env = {}
for l in open('.env.local', encoding='utf-8'):
    if '=' in l and not l.startswith('#'):
        k, v = l.rstrip('\n').split('=', 1); env[k] = v
ok_all = True
def call(method, path, body=None, headers=None, raw=None):
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    h = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 harsh-test'}; h.update(headers or {})
    req = urllib.request.Request(base + path, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=40) as r: return r.status, r.read().decode()
    except urllib.error.HTTPError as e: return e.code, e.read().decode()
def check(name, cond, extra=''):
    global ok_all; ok_all &= bool(cond)
    print(('PASS ' if cond else 'FAIL ') + name + (('  ' + extra) if extra else ''))
def j(s):
    try: return json.loads(s)
    except Exception: return {}

# static site
for p in ['/', '/hi/', '/guides.html', '/about.html', '/hi/about.html', '/assets/qrcode.min.js']:
    s, _ = call('GET', p); check('static ' + p, s == 200, str(s))
s, t = call('GET', '/.env.local'); check('secrets are not served (/.env.local)', s == 404 or 'RAZORPAY' not in t, str(s))
s, t = call('GET', '/.dev.vars'); check('secrets are not served (/.dev.vars)', s == 404 or 'RAZORPAY' not in t, str(s))

form = dict(name='TEST Payment Check', whatsapp='9876543210', email=env.get('OWNER_EMAIL') or env.get('GMAIL_USER'), age='28', city='Lucknow',
            track='1:1 Clarity & Roadmap Call (30 Mins)', preferred_date='2026-11-20', preferred_time='Evening (6 PM - 9 PM)', question='Automated test of the payment flow')
# create-order
s, t = call('POST', '/api/create-order', {'form': form}); d = j(t)
check('create-order returns a Razorpay test order', s == 200 and str(d.get('order_id', '')).startswith('order_'), f"status {s}, key {str(d.get('key_id'))[:9]}, amount {d.get('amount')}")
check('create-order amount for the 30 min session is 29900 paise', d.get('amount') == 29900)
form2 = dict(form, track='Deep-Dive Personal Advisory (60 Mins)')
s, t = call('POST', '/api/create-order', {'form': form2}); d2 = j(t)
check('create-order amount for the 60 min session is 69900 paise', d2.get('amount') == 69900, str(d2.get('amount')))
s, t = call('POST', '/api/create-order', {'form': dict(form, name='')}); check('create-order rejects a missing name', s == 400, str(s))
s, t = call('GET', '/api/create-order'); check('create-order rejects GET', s == 405, str(s))

# verify (signature logic)
oid, pid = d.get('order_id', 'order_x'), 'pay_TESTFAKE000001'
good = hmac.new(env['RAZORPAY_KEY_SECRET'].encode(), f'{oid}|{pid}'.encode(), hashlib.sha256).hexdigest()
s, t = call('POST', '/api/verify', {'razorpay_order_id': oid, 'razorpay_payment_id': pid, 'razorpay_signature': 'deadbeef' * 8}); check('verify rejects a wrong signature', s == 200 and j(t).get('valid') is False, t[:80])
s, t = call('POST', '/api/verify', {'razorpay_order_id': oid}); check('verify rejects missing fields', s == 400, str(s))
s, t = call('POST', '/api/verify', {'razorpay_order_id': oid, 'razorpay_payment_id': pid, 'razorpay_signature': good}); check('verify accepts a correct signature', s == 200 and 'valid' in j(t), t[:100])

# webhook (signature + events)
body = json.dumps({'event': 'payment.failed', 'payload': {'payment': {'entity': {'id': pid, 'error_description': 'test'}}}}).encode()
sig = hmac.new(env['RAZORPAY_WEBHOOK_SECRET'].encode(), body, hashlib.sha256).hexdigest()
s, t = call('POST', '/api/webhook', raw=body, headers={'x-razorpay-signature': 'bad'}); check('webhook rejects a bad signature', s == 400, str(s))
s, t = call('POST', '/api/webhook', raw=body, headers={'x-razorpay-signature': sig}); check('webhook accepts a signed payment.failed', s == 200, str(s))
if send_email:
    cap = json.dumps({'event': 'payment.captured', 'payload': {'payment': {'entity': {'id': pid, 'amount': 29900, 'method': 'upi', 'notes': {k: form[k] for k in form}}}}}).encode()
    sg = hmac.new(env['RAZORPAY_WEBHOOK_SECRET'].encode(), cap, hashlib.sha256).hexdigest()
    s, t = call('POST', '/api/webhook', raw=cap, headers={'x-razorpay-signature': sg}); check('webhook accepts a signed payment.captured (sends 2 emails to the owner address)', s == 200, str(s))

# admin list
s, t = call('GET', '/api/bookings'); check('bookings needs the admin token', s == 401, str(s))
s, t = call('GET', '/api/bookings?token=' + env['ADMIN_TOKEN']); check('bookings works with the admin token', s == 200 and 'bookings' in j(t), f"status {s}, count {j(t).get('count')}")

# form endpoints (validation only)
s, t = call('POST', '/api/upi-claim', {'email': 'bad', 'utr': '123', 'amount': 299, 'session': 'x'}); check('upi-claim rejects bad input', s == 400, str(s))
s, t = call('POST', '/api/subscribe', {'email': 'bad', 'consent': True}); check('subscribe rejects a bad email', s == 400, str(s))
s, t = call('POST', '/api/subscribe', {'email': 'a@b.co', 'consent': False}); check('subscribe needs consent', s == 400, str(s))
s, t = call('POST', '/api/subscribe', {'email': 'a@b.co', 'consent': True, 'website': 'bot'}); check('subscribe ignores bots silently', s == 200, str(s))
print('\nALL PASSED' if ok_all else '\nSOME CHECKS FAILED')
