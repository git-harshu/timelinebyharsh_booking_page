#!/usr/bin/env python3
"""Writes about.html (English) and hi/about.html (Hinglish). Header and footer come from privacy.html / hi/privacy.html.
Run after build_legal_hi.py:  python3 tools/build_about.py"""
import re

IG = 'https://www.instagram.com/timelinebyharsh/'

EN = dict(
 title='About', meta='About Harsh Upadhyay and how the one-on-one guidance calls at Timeline by Harsh work.',
 h1='Hi, I am Harsh',
 lead='I am Harsh Upadhyay, the person behind <b>Timeline by Harsh</b>. I create Hindu religious content on Instagram and talk with people about Sanatan Dharma and everyday life.',
 btn='Book a call', ig='@timelinebyharsh on Instagram',
 why_h='Why I take calls',
 why_p='The problems people bring are usually familiar: too much overthinking, a routine that keeps slipping, or a big decision that is hard to make alone. A comment or a short message is rarely enough for that, which is why I offer one-on-one calls.',
 how_h='How a call works',
 how=[('You talk','You explain where you are stuck. Take your time. Nobody is rushing you.'),('I ask','I ask direct questions to find the real problem, not just the loudest one.'),('We plan','We agree a few clear steps for the days ahead. I send a written summary on WhatsApp within 24 hours.')],
 draw_h='What I draw on',
 draw_q='Practical wisdom, daily practices such as dhyan, and what I have learned from Sanatan Dharma. Not generic motivation.',
 not_h='What a call is not',
 nots=[('Not therapy','It is not therapy, counselling or medical advice.'),('Not professional advice','It is not legal, financial or investment advice.'),('Not a guarantee','You do the work. I help you see it clearly.')],
 not_note='If you are in crisis or feel unsafe, please contact your local emergency services (in India, call 112) or someone you trust.',
 priv_h='Your privacy', priv_p='What you tell me stays between us. I collect only what is needed to book and prepare for your call.', priv_a='Read the privacy policy', priv_href='privacy.html',
 cta_h='Ready to talk?', cta_p='Find the session that fits, or go straight to choosing a time.', cta1='Find your fit', cta1_href='index.html#diagnostic', cta2='Book a call', cta2_href='index.html#booking',
 tag='About', alt='Harsh Upadhyay', home='index.html', asset='assets/logo.jpg', switch_old='hi/privacy.html', switch_new='hi/about.html',
)
HI = dict(
 title='About', meta='Harsh Upadhyay ke baare mein aur Timeline by Harsh ki one-on-one guidance calls kaise kaam karti hain.',
 h1='Hi, I am Harsh',
 lead='Main Harsh Upadhyay hoon, <b>Timeline by Harsh</b> ke peeche. Main Instagram par Hindu dharmik content banata hoon aur Sanatan Dharma aur roz ki zindagi par logon se baat karta hoon.',
 btn='Book a call', ig='@timelinebyharsh on Instagram',
 why_h='Why I take calls',
 why_p='Log aksar ek jaisi dikkatein lekar aate hain: zyada sochna, aisa routine jo tikta nahi, ya koi bada faisla jo akele lena mushkil hai. Iske liye ek comment ya chhota message kaafi nahi hota, isiliye main one-on-one calls karta hoon.',
 how_h='How a call works',
 how=[('You talk','Aap batate hain ki kahan phanse hain. Aaram se bolein, koi jaldi nahi hai.'),('I ask','Main seedhe sawaal poochta hoon taaki asli dikkat milein, sirf sabse zor wali nahi.'),('We plan','Hum aane wale dinon ke liye kuch saaf kadam tay karte hain. 24 ghante ke andar main WhatsApp par likhit summary bhejta hoon.')],
 draw_h='What I draw on',
 draw_q='Samajhdari ki baatein, roz ki practice jaise dhyan, aur Sanatan Dharma se seekhi baatein. Bas motivation wali baatein nahi.',
 not_h='What a call is not',
 nots=[('Not therapy','Ye therapy, counselling ya medical salah nahi hai.'),('Not professional advice','Ye legal, paison ya investment ki salah nahi hai.'),('Not a guarantee','Mehnat aapko karni hai. Main bas saaf dekhne mein madad karta hoon.')],
 not_note='Agar aap mushkil mein hain ya safe mehsoos nahi kar rahe, toh apni local emergency service (India mein 112) ya kisi bharosemand insaan se turant sampark karein.',
 priv_h='Your privacy', priv_p='Aap jo batate hain woh sirf hamare beech rehta hai. Main sirf wahi jaankari leta hoon jo booking aur taiyaari ke liye zaroori hai.', priv_a='Read the privacy policy', priv_href='privacy.html',
 cta_h='Ready to talk?', cta_p='Apne liye sahi session chunein, ya seedha time chunein.', cta1='Find your fit', cta1_href='index.html#diagnostic', cta2='Book a call', cta2_href='index.html#booking',
 tag='About', alt='Harsh Upadhyay', home='index.html', asset='../assets/logo.jpg', switch_old='../privacy.html', switch_new='../about.html',
)

CSS = '''
main{background:#fff}
.wrapn{max-width:960px;margin:0 auto;padding:0 1.5rem}
.sec{padding:4.5rem 0}.sec.tint{background:var(--tint)}
.tag{display:inline-block;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--accent);margin-bottom:.6rem}
.ab-hero{background:linear-gradient(180deg,#fff 0%,#FFF8F0 100%);padding:4rem 0 4.5rem}
.ab-grid{display:grid;grid-template-columns:1fr;gap:2rem;justify-items:center;text-align:center;align-items:center}
@media(min-width:800px){.ab-grid{grid-template-columns:auto 1fr;gap:3.5rem;justify-items:start;text-align:left}}
.ab-photo{width:9.5rem;height:9.5rem;border-radius:50%;padding:5px;background:linear-gradient(135deg,#FF6F1E,#FFB27A);box-shadow:0 20px 40px rgba(255,111,30,.22)}
.ab-photo img{width:100%;height:100%;border-radius:50%;object-fit:cover;display:block;border:4px solid #fff}
@media(min-width:800px){.ab-photo{width:12rem;height:12rem}}
.ab-intro h1{font-family:var(--display);font-weight:600;font-size:clamp(2.2rem,5vw,3.4rem);line-height:1.1;letter-spacing:-.02em;margin-bottom:1rem}
.ab-intro .lead{color:var(--muted);font-size:1.1rem;max-width:34rem;margin-bottom:1.75rem}
.ab-intro .lead b{color:var(--text);font-weight:600}
.ab-links{display:flex;flex-direction:column;gap:.75rem;align-items:stretch}
@media(min-width:560px){.ab-links{flex-direction:row;align-items:center;gap:1.5rem}}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:3rem;padding:0 1.75rem;border-radius:9999px;background:var(--accent);color:#fff;font-size:1rem;font-weight:500;transition:background .2s,box-shadow .25s}
.btn:hover{background:var(--accent-hover);box-shadow:0 6px 18px rgba(255,111,30,.3)}
.tl{display:inline-flex;align-items:center;justify-content:center;min-height:44px;color:var(--muted);text-decoration:underline;text-decoration-color:var(--border-strong);text-underline-offset:5px;transition:color .2s,text-decoration-color .2s}
.tl:hover{color:var(--accent);text-decoration-color:var(--accent)}
h2.h{font-family:var(--display);font-weight:600;font-size:clamp(1.6rem,3vw,2.1rem);line-height:1.25;margin-bottom:1.25rem}
.center{text-align:center}
.why p{color:var(--muted);font-size:1.1rem;max-width:40rem;margin:0 auto}
.cards{display:grid;grid-template-columns:1fr;gap:1.1rem}
@media(min-width:800px){.cards.c3{grid-template-columns:repeat(3,1fr)}}
.card{border:1px solid var(--border);background:var(--bg);border-radius:12px;padding:1.75rem 1.5rem;text-align:center;transition:border-color .3s var(--ease),box-shadow .3s var(--ease)}
.card:hover{border-color:rgba(255,111,30,.5);box-shadow:0 10px 30px rgba(33,37,43,.06)}
.card .n{font-family:var(--display);font-size:2rem;line-height:1;color:var(--accent);margin-bottom:.6rem;display:block}
.card h3{font-family:var(--display);font-weight:500;font-size:1.3rem;margin-bottom:.4rem}
.card p{color:var(--muted);font-size:.95rem}
.quote{font-family:var(--display);font-weight:500;font-size:clamp(1.4rem,3vw,2rem);line-height:1.4;max-width:40rem;margin:0 auto;text-align:center;text-wrap:balance}
.quote::before{content:"";display:block;width:3rem;height:3px;border-radius:3px;background:var(--accent);margin:0 auto 1.5rem}
.note{max-width:40rem;margin:1.5rem auto 0;text-align:center;color:var(--muted);font-size:.9rem}
.priv{display:flex;flex-direction:column;gap:1rem;align-items:center;text-align:center}
.priv p{color:var(--muted);max-width:34rem}
.cta-band{background:var(--tint);border-radius:12px;padding:3rem 1.5rem;text-align:center}
.cta-band p{color:var(--muted);margin-bottom:1.5rem}
.cta-row{display:flex;flex-direction:column;gap:.75rem;align-items:stretch;max-width:20rem;margin:0 auto}
@media(min-width:560px){.cta-row{flex-direction:row;max-width:none;justify-content:center;align-items:center;gap:1.5rem}}
'''

def page(L, base, out):
    t = open(base, encoding='utf-8').read()
    t = re.sub(r'<title>.*?</title>', f'<title>{L["title"]} | Timeline by Harsh</title>', t, count=1, flags=re.S)
    t = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{L["meta"]}">', t, count=1)
    t = t.replace(L['switch_old'], L['switch_new'])
    t = t.replace('</head>', '<style>' + CSS + '</style>\n</head>', 1)
    t = re.sub(r'<section class="title">.*?</section>', lambda m: '@@HERO@@', t, count=1, flags=re.S)
    hero = f'''<section class="ab-hero"><div class="wrapn ab-grid">
  <div class="ab-photo"><img src="{L['asset']}" width="150" height="150" alt="{L['alt']}"></div>
  <div class="ab-intro">
    <span class="tag">{L['tag']}</span>
    <h1>{L['h1']}</h1>
    <p class="lead">{L['lead']}</p>
    <div class="ab-links"><a class="btn" href="index.html#booking">{L['btn']}</a><a class="tl" href="{IG}" target="_blank" rel="noopener noreferrer">{L['ig']}</a></div>
  </div>
</div></section>'''
    cards = ''.join(f'<div class="card"><span class="n">0{i+1}</span><h3>{h}</h3><p>{p}</p></div>' for i, (h, p) in enumerate(L['how']))
    nots = ''.join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in L['nots'])
    main = f'''<main>
<section class="sec why"><div class="wrapn center"><h2 class="h">{L['why_h']}</h2><p>{L['why_p']}</p></div></section>
<section class="sec tint"><div class="wrapn center"><h2 class="h">{L['how_h']}</h2><div class="cards c3">{cards}</div></div></section>
<section class="sec"><div class="wrapn center"><h2 class="h">{L['draw_h']}</h2><p class="quote">{L['draw_q']}</p></div></section>
<section class="sec tint"><div class="wrapn center"><h2 class="h">{L['not_h']}</h2><div class="cards c3">{nots}</div><p class="note">{L['not_note']}</p></div></section>
<section class="sec"><div class="wrapn priv"><h2 class="h" style="margin-bottom:0">{L['priv_h']}</h2><p>{L['priv_p']}</p><a class="tl" href="{L['priv_href']}">{L['priv_a']}</a></div></section>
<section class="sec" style="padding-top:0"><div class="wrapn"><div class="cta-band"><h2 class="h">{L['cta_h']}</h2><p>{L['cta_p']}</p><div class="cta-row"><a class="btn" href="{L['cta2_href']}">{L['cta2']}</a><a class="tl" href="{L['cta1_href']}">{L['cta1']}</a></div></div></div></section>
</main>'''
    t = t.replace('@@HERO@@', hero)
    t = re.sub(r'<article>.*?</article>', lambda m: main, t, count=1, flags=re.S)
    open(out, 'w', encoding='utf-8').write(t)

page(EN, 'privacy.html', 'about.html')
page(HI, 'hi/privacy.html', 'hi/about.html')
print('about pages written')
