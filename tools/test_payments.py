#!/usr/bin/env python3
"""Smoke test for the live endpoints. Usage: python3 tools/test_payments.py [base_url]
Checks secrets are not served, upi-claim and subscribe validate input. No mail is sent."""
import sys, json, urllib.request, urllib.error
base = (sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8787').rstrip('/')
def call(m, path, body=None):
    d = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(base + path, data=d, method=m, headers={'content-type': 'application/json'})
    try:
        with urllib.request.urlopen(r) as x: return x.status, x.read().decode()
    except urllib.error.HTTPError as e: return e.code, e.read().decode()
bad = 0
def check(n, ok, info=''):
    global bad; bad += not ok; print(('PASS ' if ok else 'FAIL ') + n, info)
for f in ['/.env.local', '/.dev.vars', '/api/_mail.js', '/bookings.html']:
    s, t = call('GET', f); check('not served: ' + f, s == 404 or 'GMAIL' not in t, str(s))
s, t = call('POST', '/api/upi-claim', {}); check('upi-claim rejects empty body', s == 400, str(s))
s, t = call('POST', '/api/subscribe', {}); check('subscribe rejects empty body', s == 400, str(s))
s, t = call('GET', '/'); check('home page loads', s == 200 and 'Timeline' in t, str(s))
s, t = call('GET', '/hi/'); check('hinglish loads', s == 200, str(s))
sys.exit(1 if bad else 0)
