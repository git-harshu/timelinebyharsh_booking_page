#!/usr/bin/env python3
"""Writes guides.html (English) and hi/guides.html (Hinglish), reusing the header and footer of about.html.
Run after build_legal_hi.py:  python3 tools/build_guides.py"""
import re

def split(path):
    t = open(path, encoding='utf-8').read()
    return t

EN = dict(
 lang='en', title='Guides', sub='Simple, sourced guides for the traditions you follow',
 meta='Guides from Timeline by Harsh: the Hindu Festival and Vrat Companion and more. Join the early-access list.',
 tag_first='Coming first', tag_planned='Planned', tag_soon='Coming soon',
 g_title='The Hindu Festival and Vrat Companion',
 g_lead='One guide for the festivals and vrats you observe: what each one means, how to prepare, and what you will need.',
 for_h='Who it is for',
 for_li=['People who observe festivals and vrats and want to know the why, not only the how.','Families who want one clear reference at home.','Anyone starting out who is not sure where to begin.'],
 in_h='What is inside',
 in_li=['Major festivals explained','Preparation checklists','Common puja samagri lists','Basic ritual steps','Mantra meanings and pronunciation','Traditional variations and references','Common questions answered'],
 how_h='How it is made',
 how_p='Practices differ by region, calendar and tradition. Where they do, the guide marks the variations instead of presenting one way as the only way. Sources are named. It does not promise any result from a puja, mantra or product.',
 price_h='Price and format',
 price_p='The free Hindu Festival and Vrat Calendar comes first. The full guide will be a paid download, and its price will be shown before you pay.',
 join_h='Get early access', join_p='Join the list and I will write when it is ready.',
 f_email='Email', f_wa='WhatsApp (optional)', f_wa_ph='10-digit number', f_int='What are you interested in?',
 chips=['Festival and vrat guide','Live sessions','Puja preparation session','Gita study circle'],
 consent='I agree to receive messages about these resources. I can stop anytime.', btn='Join the list',
 more_h='Also planned',
 more=[('Daily Puja Guide for Beginners','A simple start for a daily puja: what you need and the usual order.'),
       ('Bhagavad Gita Beginner Study Guide','A plain-language introduction to the main ideas of the Gita.'),
       ('Hindu Rituals and Traditions Handbook','Why and how common rituals are done, with regional differences marked.')],
 live_h='Learn live',
 live=[('Live group sessions','Small online sessions on the Gita, rituals and festivals, with time for your questions.'),
       ('Puja preparation session','A short one-on-one to plan a puja: samagri, the usual sequence, and where practices differ. This is planning and education. I do not perform pujas.')],
 faq_h='Common questions',
 faq=[('When will it be ready?','I am preparing it now. Join the list and I will write to you when it is ready.'),
      ('Is it free?','The calendar is free. The full guide will be a paid download, and the price will be shown before you pay.'),
      ('Will it match my family\'s tradition?','It marks where practices differ by region and tradition and names its sources. It cannot cover every family tradition, so please check with your own family or priest.')],
 q_h='Have a question first?', q_a='Message me on Instagram',
 e_email='Please enter a valid email address.', e_wa='Please enter a valid 10-digit WhatsApp number, or leave it empty.', e_box='Please tick the box to agree.', sending='Sending...', ok='Thank you. You are on the list. I will write when the first guide is ready.', e_gen='Something went wrong.',
 cta='Book a call', home='index.html', ig_label='Instagram', toggle='<a class="lang" href="hi/guides.html" hreflang="hi" lang="hi" title="Hinglish" aria-label="Switch to Hinglish">HI</a>',
)
HI = dict(
 lang='hi-Latn', title='Guides', sub='Aapki paramparaon ke liye aasaan, sources wali guides',
 meta='Timeline by Harsh ki guides: Hindu Festival and Vrat Companion aur aur bhi. Early-access list join karein.',
 tag_first='Coming first', tag_planned='Planned', tag_soon='Coming soon',
 g_title='The Hindu Festival and Vrat Companion',
 g_lead='Aapke tyohaaron aur vraton ke liye ek guide: har ek ka matlab, taiyaari kaise karein, aur kya-kya chahiye.',
 for_h='Who it is for',
 for_li=['Jo log tyohaar aur vrat rakhte hain aur sirf "kaise" nahi, "kyun" bhi jaanna chahte hain.','Parivaar jo ghar par ek saaf reference chahte hain.','Jo abhi shuru kar rahe hain aur samajh nahi paa rahe ki kahan se shuru karein.'],
 in_h='What is inside',
 in_li=['Major festivals explained','Preparation checklists','Common puja samagri lists','Basic ritual steps','Mantra meanings and pronunciation','Traditional variations and references','Common questions answered'],
 how_h='How it is made',
 how_p='Riwaaj kshetra, calendar aur parampara ke hisaab se alag hote hain. Jahan farq hai, guide use saaf likhti hai, ek tareeke ko hi akela tareeka nahi batati. Sources ka naam diya jaata hai. Ye kisi puja, mantra ya product se kisi nateeje ka vaada nahi karti.',
 price_h='Price and format',
 price_p='Free Hindu Festival and Vrat Calendar pehle aayega. Poori guide paid download hogi, aur uski keemat pay karne se pehle dikhayi jaayegi.',
 join_h='Get early access', join_p='List join karein, tayyar hote hi main likhunga.',
 f_email='Email', f_wa='WhatsApp (optional)', f_wa_ph='10-digit number', f_int='What are you interested in?',
 chips=['Festival and vrat guide','Live sessions','Puja preparation session','Gita study circle'],
 chip_labels=['Festival and vrat guide','Live sessions','Puja preparation session','Gita study circle'],
 consent='Mujhe in resources ke baare mein messages bhejna theek hai. Kabhi bhi band karwa sakte hain.', btn='Join the list',
 more_h='Also planned',
 more=[('Daily Puja Guide for Beginners','Roz ki puja ki aasaan shuruaat: kya chahiye aur aam kram kya hai.'),
       ('Bhagavad Gita Beginner Study Guide','Gita ke mukhya vicharon ka aasaan bhasha mein parichay.'),
       ('Hindu Rituals and Traditions Handbook','Aam rituals kyun aur kaise kiye jaate hain, kshetra ke farq saaf likhe hue.')],
 live_h='Learn live',
 live=[('Live group sessions','Gita, rituals aur tyohaaron par chhote online sessions, aapke sawaalon ke liye time ke saath.'),
       ('Puja preparation session','Puja plan karne ke liye ek chhota one-on-one: samagri, aam kram, aur jahan riwaaj alag hote hain. Ye planning aur jaankari ke liye hai. Main puja karwata nahi hoon.')],
 faq_h='Common questions',
 faq=[('When will it be ready?','Main abhi ise bana raha hoon. List join karein, tayyar hote hi main aapko likhunga.'),
      ('Is it free?','Calendar free hai. Poori guide paid download hogi, aur keemat pay karne se pehle dikhayi jaayegi.'),
      ('Will it match my family\'s tradition?','Ye likhti hai ki kshetra aur parampara ke hisaab se riwaaj kahan alag hain, aur sources ka naam deti hai. Ye har parivaar ki parampara ko cover nahi kar sakti, isliye apne parivaar ya pandit se zaroor poochein.')],
 q_h='Have a question first?', q_a='Message me on Instagram',
 e_email='Kripya sahi email likhein.', e_wa='Kripya 10 digit ka sahi WhatsApp number likhein, ya khaali chhod dein.', e_box='Kripya sahmati ka box tick karein.', sending='Bhej rahe hain...', ok='Dhanyavaad. Aap list mein hain. Pehli guide tayyar hote hi main likhunga.', e_gen='Kuch gadbad ho gayi.',
 cta='Book a call', home='index.html', ig_label='Instagram', toggle='<a class="lang" href="../guides.html" hreflang="en" lang="en" title="English" aria-label="Switch to English">EN</a>',
)

CSS = '''
main{background:#fff}
.sec{padding:4.5rem 0}
.sec.tint{background:var(--tint)}
.wrapn{max-width:960px;margin:0 auto;padding:0 1.5rem}
h2.h{font-family:var(--display);font-weight:600;font-size:clamp(1.6rem,3vw,2.1rem);line-height:1.25;margin-bottom:1.25rem}
.tag{display:inline-block;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:var(--accent);margin-bottom:.6rem}
.flag{display:grid;grid-template-columns:1fr;gap:2rem;align-items:start}
@media(min-width:900px){.flag{grid-template-columns:1.15fr .85fr;gap:3rem}}
.flag h2{font-family:var(--display);font-weight:600;font-size:clamp(1.9rem,3.6vw,2.6rem);line-height:1.15;margin-bottom:.75rem}
.lead{color:var(--muted);font-size:1.05rem;max-width:34rem;margin-bottom:1.5rem}
.blk{margin-bottom:1.5rem}
.blk h3{font-family:var(--display);font-weight:600;font-size:1.2rem;margin-bottom:.6rem}
.blk p{color:var(--muted);font-size:.975rem}
.dots-list{list-style:none;display:grid;gap:.45rem}
.dots-list li{position:relative;padding-left:1.1rem;font-size:.975rem;color:var(--text)}
.dots-list li::before{content:"";position:absolute;left:0;top:.65em;width:6px;height:6px;border-radius:50%;background:var(--accent)}
.two{display:grid;grid-template-columns:1fr;gap:0 2rem}
@media(min-width:560px){.two{grid-template-columns:1fr 1fr}}
.joincard{background:var(--tint);border-radius:12px;padding:1.75rem 1.5rem}
@media(min-width:900px){.joincard{position:sticky;top:6rem}}
.joincard h3{font-family:var(--display);font-weight:600;font-size:1.4rem;margin-bottom:.3rem}
.joincard>p{color:var(--muted);font-size:.9rem;margin-bottom:1.1rem}
.fld{margin-bottom:1rem}
.fld label,.fld legend{display:block;font-size:.8rem;font-weight:500;color:var(--muted);margin-bottom:.35rem}
.fld input[type=email],.fld input[type=tel]{width:100%;padding:.8rem .9rem;border:1px solid var(--border-strong);border-radius:12px;font:inherit;font-size:.95rem;background:#fff}
.fld input:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(255,111,30,.15)}
fieldset.fld{border:0;display:flex;flex-wrap:wrap;gap:.5rem}
fieldset.fld legend{width:100%}
.chip{cursor:pointer}
.chip input{position:absolute;opacity:0;pointer-events:none}
.chip span{display:inline-flex;align-items:center;min-height:2.4rem;padding:0 .9rem;border:1px solid var(--border-strong);border-radius:9999px;font-size:.85rem;color:var(--muted);background:#fff;transition:background .25s,border-color .25s,color .25s}
.chip:hover span{border-color:var(--accent);color:var(--text)}
.chip input:checked+span{background:rgba(255,111,30,.1);border-color:var(--accent);color:var(--text);font-weight:500}
.chip input:focus-visible+span{outline:2px solid var(--accent);outline-offset:2px}
.hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}
.consent{display:flex;gap:.6rem;align-items:flex-start;font-size:.85rem;color:var(--muted);margin-bottom:1rem;cursor:pointer}
.consent input{margin-top:.3rem;accent-color:var(--accent);width:1.05rem;height:1.05rem;flex-shrink:0}
.sbtn{width:100%;display:inline-flex;align-items:center;justify-content:center;min-height:3rem;border-radius:9999px;background:var(--accent);color:#fff;font:inherit;font-size:1rem;font-weight:500;border:0;cursor:pointer;transition:background .2s,box-shadow .25s}
.sbtn:hover{background:var(--accent-hover);box-shadow:0 6px 18px rgba(255,111,30,.3)}
.sbtn:disabled{opacity:.55}
.msg{min-height:1.25rem;margin-top:.8rem;font-size:.9rem;text-align:center;color:var(--muted)}
.msg.err{color:#B42318}.msg.ok{color:#2F5D2A;font-weight:500}
.cards{display:grid;grid-template-columns:1fr;gap:1.1rem}
@media(min-width:800px){.cards.c3{grid-template-columns:repeat(3,1fr)}.cards.c2{grid-template-columns:1fr 1fr}}
.card{border:1px solid var(--border);background:var(--bg);border-radius:12px;padding:1.5rem;transition:border-color .3s var(--ease),box-shadow .3s var(--ease)}
.card:hover{border-color:rgba(255,111,30,.5);box-shadow:0 10px 30px rgba(33,37,43,.06)}
.card h3{font-family:var(--display);font-weight:500;font-size:1.25rem;line-height:1.3;margin-bottom:.4rem}
.card p{color:var(--muted);font-size:.925rem}
@media(max-width:799px){.card{text-align:center}}
.faq details{border-bottom:1px solid var(--border);padding:1rem 0}
.faq summary{cursor:pointer;list-style:none;font-weight:600;font-size:1rem;display:flex;justify-content:space-between;gap:1rem;transition:color .25s}
.faq summary::-webkit-details-marker{display:none}
.faq summary:hover{color:var(--accent)}
.faq summary::after{content:"+";color:var(--faint);font-size:1.3rem;line-height:1;transition:transform .35s var(--ease)}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq p{color:var(--muted);margin-top:.6rem;font-size:.95rem}
.q{text-align:center}
.q p{color:var(--muted);margin-bottom:.9rem}
.q a{color:var(--text);text-decoration:underline;text-decoration-color:var(--border-strong);text-underline-offset:5px;transition:color .2s,text-decoration-color .2s}
.q a:hover{color:var(--accent);text-decoration-color:var(--accent)}
'''

def page(L, base, out, prefix):
    t = open(base, encoding='utf-8').read()
    # head
    t = re.sub(r'<title>.*?</title>', f'<title>{L["title"]} | Timeline by Harsh</title>', t, 1, flags=re.S)
    t = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{L["meta"]}">', t, 1)
    t = t.replace('hi/about.html', 'hi/guides.html').replace('../about.html', '../guides.html')
    # toggle (already points to guides after the replace above)
    # title section
    t = re.sub(r'<h1>.*?</h1>', f'<h1>{L["title"]}</h1>', t, 1, flags=re.S)
    t = re.sub(r'(<h1>' + re.escape(L['title']) + r'</h1>\s*<p>).*?(</p>)', r'\g<1>' + L['sub'].replace('\\', '\\\\') + r'\g<2>', t, 1, flags=re.S)
    # extra css
    t = t.replace('</head>', '<style>' + CSS + '</style>\n</head>', 1)
    labels = L.get('chip_labels', L['chips'])
    chips = ''.join(f'<label class="chip"><input type="checkbox" name="interest" value="{v}"{" checked" if k == 0 else ""}><span>{lab}</span></label>' for k, (v, lab) in enumerate(zip(L['chips'], labels)))
    li = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    cards = lambda items, tag: ''.join(f'<div class="card"><span class="tag">{tag}</span><h3>{h}</h3><p>{p}</p></div>' for h, p in items)
    faq = ''.join(f'<details name="g"><summary>{q}</summary><p>{a}</p></details>' for q, a in L['faq'])
    main = f'''<main>
<section class="sec"><div class="wrapn flag">
  <div>
    <span class="tag">{L['tag_first']}</span>
    <h2>{L['g_title']}</h2>
    <p class="lead">{L['g_lead']}</p>
    <div class="blk"><h3>{L['for_h']}</h3><ul class="dots-list">{li(L['for_li'])}</ul></div>
    <div class="blk"><h3>{L['in_h']}</h3><ul class="dots-list two">{li(L['in_li'])}</ul></div>
    <div class="blk"><h3>{L['how_h']}</h3><p>{L['how_p']}</p></div>
    <div class="blk"><h3>{L['price_h']}</h3><p>{L['price_p']}</p></div>
  </div>
  <form class="joincard" id="joinForm" novalidate>
    <h3>{L['join_h']}</h3><p>{L['join_p']}</p>
    <div class="fld"><label for="jEmail">{L['f_email']}</label><input type="email" id="jEmail" placeholder="rahul@example.com" required autocomplete="email"></div>
    <div class="fld"><label for="jWa">{L['f_wa']}</label><input type="tel" id="jWa" placeholder="{L['f_wa_ph']}" autocomplete="tel" inputmode="numeric"></div>
    <fieldset class="fld"><legend>{L['f_int']}</legend>{chips}</fieldset>
    <input type="text" id="jHp" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
    <label class="consent"><input type="checkbox" id="jConsent"><span>{L['consent']}</span></label>
    <button type="submit" class="sbtn" id="jBtn">{L['btn']}</button>
    <p class="msg" id="jMsg" role="status" aria-live="polite"></p>
  </form>
</div></section>

<section class="sec tint"><div class="wrapn">
  <h2 class="h">{L['more_h']}</h2>
  <div class="cards c3">{cards(L['more'], L['tag_planned'])}</div>
</div></section>

<section class="sec"><div class="wrapn">
  <h2 class="h">{L['live_h']}</h2>
  <div class="cards c2">{cards(L['live'], L['tag_soon'])}</div>
</div></section>

<section class="sec tint"><div class="wrapn faq" style="max-width:720px">
  <h2 class="h">{L['faq_h']}</h2>
  {faq}
</div></section>

<section class="sec"><div class="wrapn q"><h2 class="h">{L['q_h']}</h2><a href="https://www.instagram.com/timelinebyharsh/" target="_blank" rel="noopener noreferrer">{L['q_a']}</a></div></section>
</main>
<script>
(function () {{
  var f = document.getElementById('joinForm'), msg = document.getElementById('jMsg'), btn = document.getElementById('jBtn');
  function say(t, c) {{ msg.textContent = t; msg.className = 'msg' + (c ? ' ' + c : ''); }}
  f.addEventListener('submit', function (e) {{
    e.preventDefault();
    var email = document.getElementById('jEmail').value.trim();
    var wa = document.getElementById('jWa').value.replace(/\\D/g, '').slice(-10);
    if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{{2,}}$/.test(email)) return say({L['e_email']!r}, 'err');
    if (wa && !/^[6-9]\\d{{9}}$/.test(wa)) return say({L['e_wa']!r}, 'err');
    if (!document.getElementById('jConsent').checked) return say({L['e_box']!r}, 'err');
    var interests = Array.prototype.map.call(f.querySelectorAll('input[name=interest]:checked'), function (i) {{ return i.value; }});
    btn.disabled = true; say({L['sending']!r}, '');
    fetch('/api/subscribe', {{ method: 'POST', headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{ email: email, whatsapp: wa, interests: interests, consent: true, website: document.getElementById('jHp').value }}) }})
      .then(function (r) {{ return r.json().then(function (j) {{ return {{ ok: r.ok, j: j }}; }}); }})
      .then(function (res) {{ if (!res.ok) throw new Error(res.j.error || {L['e_gen']!r}); f.reset(); say({L['ok']!r}, 'ok'); }})
      .catch(function (ex) {{ say(ex.message, 'err'); }})
      .then(function () {{ btn.disabled = false; }});
  }});
}})();
</script>'''
    t = re.sub(r'<article>.*?</article>', lambda m: main, t, 1, flags=re.S)
    open(out, 'w', encoding='utf-8').write(t)

page(EN, 'about.html', 'guides.html', '')
page(HI, 'hi/about.html', 'hi/guides.html', '../')
print('guides pages written')
