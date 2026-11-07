#!/usr/bin/env python3
"""Three design options for the 'Learn the stories behind the tradition' section (preview only, not on the live site)."""
HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@NAME@@ | Learn section preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Fraunces:opsz,wght,SOFT@9..144,300..700,0..100&family=Tiro+Devanagari+Hindi&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../hero-options/base.css">
<style>
:root{--display:'Fraunces',Georgia,serif}
body{font-variation-settings:'SOFT' 100,'WONK' 0}
.ctx{padding:5rem 1.5rem;text-align:center;background:var(--tint)}
.ctx h2{font-family:var(--display);font-weight:600;font-size:clamp(1.8rem,3.4vw,2.4rem)}
.ctx.after{background:var(--tint)}
.learn{background:#fff;padding:5.5rem 0}
.wrapx{max-width:1040px;margin:0 auto;padding:0 1.5rem}
.sh{font-family:var(--display);font-weight:600;font-size:clamp(1.9rem,3.8vw,2.5rem);line-height:1.2;letter-spacing:-.01em;text-wrap:balance}
.intro{color:var(--muted);font-size:.975rem;max-width:36rem}
.tag{display:inline-block;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--accent);margin-bottom:.6rem}
.btn{min-height:3rem}
.hl{display:inline-flex;align-items:center;min-height:44px;color:var(--muted);text-decoration:underline;text-decoration-color:var(--border-strong);text-underline-offset:5px;transition:color .2s,text-decoration-color .2s}
.hl:hover{color:var(--accent);text-decoration-color:var(--accent)}
.pi{display:grid;place-items:center;width:3.25rem;height:3.25rem;border-radius:50%;background:rgba(255,111,30,.1);color:var(--accent)}
.pi svg{width:1.6rem;height:1.6rem}
.pi .omg{font-family:var(--deva);font-size:1.6rem;line-height:1;transform:translateY(.08em)}
.cover{width:12.5rem;aspect-ratio:3/4;background:#fff;border-radius:12px;border:1px solid var(--border);box-shadow:0 24px 48px rgba(33,37,43,.10);padding:1.25rem 1.1rem;display:flex;flex-direction:column;text-align:left;position:relative;overflow:hidden}
.cover::after{content:"";position:absolute;left:1.1rem;right:1.1rem;bottom:3rem;height:3px;border-radius:3px;background:var(--accent);opacity:.85}
.cover .o{font-family:var(--deva);font-size:2rem;line-height:1;color:var(--accent)}
.cover .k{margin-top:.5rem;font-size:.75rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--faint)}
.cover strong{margin-top:auto;margin-bottom:3.6rem;font-family:var(--display);font-weight:600;font-size:1.3rem;line-height:1.2}
.cover .b{position:absolute;left:1.1rem;bottom:1rem;font-size:.75rem;color:var(--muted)}
@@CSS@@
</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="lotus" viewBox="0 0 48 48"><g fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M24 7C30 15 30 27 24 36C18 27 18 15 24 7Z"/><path d="M24 36C24 36 13 33 11 20C18 21 23 27 24 36Z"/><path d="M24 36C24 36 35 33 37 20C30 21 25 27 24 36Z"/><path d="M24 36C24 36 10 37 5 27C12 25 20 28 24 36Z"/><path d="M24 36C24 36 38 37 43 27C36 25 28 28 24 36Z"/><path d="M10 41Q24 47 38 41"/></g></symbol>
  <symbol id="diya" viewBox="0 0 48 48"><g fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 28H43C43 37 35 43 24 43C13 43 5 37 5 28Z"/><path d="M24 6C29 12 30 18 24 24C18 18 19 12 24 6Z"/></g></symbol>
  <symbol id="trishul" viewBox="0 0 48 48"><g fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M24 4V44"/><path d="M24 4L21 10H27Z"/><path d="M12 8V19C12 26 17 29 24 29C31 29 36 26 36 19V8"/><path d="M12 8L9.5 13H14.5Z"/><path d="M36 8L33.5 13H38.5Z"/><path d="M20 36H28"/></g></symbol>
</svg>
<header><div class="wrap bar">
  <a class="brand" href="#"><img src="../assets/logo.jpg" width="40" height="40" alt="Harsh Upadhyay"><span><b>Harsh</b><small>@timelinebyharsh</small></span></a>
  <nav><ul><li><a href="#">Find your fit</a></li><li><a href="#">How it works</a></li><li><a href="#">Sessions</a></li><li><a href="#">Guides</a></li></ul></nav>
  <a class="cta" href="#">Book a call</a>
</div></header>
<section class="ctx"><h2>Booking section above</h2></section>
@@BODY@@
<section class="ctx after"><h2>Early-access list below</h2></section>
<div class="peek-note">@@NAME@@ (preview only, not on the live site)</div>
@@JS@@
</body>
</html>
'''
def ic(name): return f'<span class="pi"><svg aria-hidden="true"><use href="#{name}"/></svg></span>'
OM = '<span class="pi"><span class="omg" aria-hidden="true">ॐ</span></span>'
P = [('Mandir and history','The stories and heritage behind our temples.',ic('trishul')),
     ('Rituals and traditions','Why, how and when rituals are done.',ic('diya')),
     ('Scriptures and philosophy','The Gita, Ramayana and Mahabharata, simply explained.',ic('lotus')),
     ('Festivals and vrat','Preparation and meaning, in plain words.',OM)]
COVER = '<div class="cover" aria-hidden="true"><span class="o">ॐ</span><span class="k">Guide</span><strong>The Hindu Festival and Vrat Companion</strong><span class="b">Timeline by Harsh</span></div>'

# ------------- Option 1: editorial split, numbered list + guide card -------------
css1 = '''
.o1{display:grid;grid-template-columns:minmax(0,1fr);gap:3rem;align-items:start}
@media(min-width:960px){.o1{grid-template-columns:1.05fr .95fr;gap:5rem}.o1 .left{position:sticky;top:6rem}}
.o1 .intro{margin:.9rem 0 2rem}
.rows{list-style:none;border-top:1px solid var(--border-strong)}
.rows li{display:grid;grid-template-columns:3rem 1fr;gap:1rem;align-items:baseline;padding:1.25rem 0;border-bottom:1px solid var(--border-strong);transition:background .25s}
.rows .n{font-family:var(--display);font-size:1.7rem;color:var(--accent);line-height:1}
.rows h3{font-family:var(--display);font-weight:500;font-size:1.35rem;line-height:1.25;margin-bottom:.2rem;transition:color .25s}
.rows li:hover h3{color:var(--accent)}
.rows p{color:var(--muted);font-size:.95rem}
.gcard{background:var(--tint);border-radius:12px;padding:2.25rem 1.75rem;text-align:center}
.gcard .cover{margin:0 auto 1.75rem}
.gcard h3{font-family:var(--display);font-weight:600;font-size:1.6rem;line-height:1.2;margin-bottom:.6rem}
.gcard p{color:var(--muted);font-size:.95rem;margin-bottom:1.5rem}
.gcard .btn{width:100%}
@media(max-width:959px){.o1 .left{text-align:center}.o1 .intro{margin-left:auto;margin-right:auto}.rows li{text-align:left}}
'''
body1 = f'''<section class="learn"><div class="wrapx o1">
  <div class="left">
    <span class="tag">Learn</span>
    <h2 class="sh">Learn the stories behind the tradition</h2>
    <p class="intro">Hindu history, temples, rituals and scriptures, told in simple Hindi on Instagram. Here is what I share, and what I am building next.</p>
    <ol class="rows">{''.join(f'<li><span class="n">0{i+1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i,(t,d,_) in enumerate(P))}</ol>
  </div>
  <div class="gcard">
    <span class="tag">Coming first</span>
    {COVER}
    <h3>The Hindu Festival and Vrat Companion</h3>
    <p>One guide for the festivals and vrats you observe: what each one means, how to prepare, and what you will need.</p>
    <a class="btn" href="#">Get early access</a>
    <a class="hl" href="#">See the guide</a>
  </div>
</div></section>'''

# ------------- Option 2: pillar tabs that reveal the matching guide -------------
css2 = '''
.o2{text-align:center}
.o2 .intro{margin:.9rem auto 2rem}
.ptabs{display:inline-flex;flex-wrap:wrap;justify-content:center;gap:.5rem;margin-bottom:2rem}
.ptab{display:inline-flex;align-items:center;gap:.6rem;min-height:3rem;padding:0 1.15rem 0 .5rem;border-radius:9999px;border:1px solid var(--border-strong);background:var(--bg);color:var(--muted);font:inherit;font-weight:500;cursor:pointer;transition:background .25s,border-color .25s,color .25s}
.ptab .pi{width:2.1rem;height:2.1rem}.ptab .pi svg{width:1.1rem;height:1.1rem}.ptab .pi .omg{font-size:1.1rem}
.ptab:hover{border-color:var(--accent);color:var(--text)}
.ptab[aria-selected=true]{background:#fff;border-color:var(--accent);color:var(--text);box-shadow:0 0 0 2px rgba(255,111,30,.18)}
.panel{background:var(--tint);border-radius:12px;padding:2rem 1.5rem;display:grid;grid-template-columns:minmax(0,1fr);gap:2rem;align-items:center;text-align:center;animation:settle .5s var(--ease) both}
@media(min-width:900px){.panel{grid-template-columns:1fr 17rem;padding:3rem;gap:3.5rem;text-align:left}}
.panel h3{font-family:var(--display);font-weight:600;font-size:clamp(1.6rem,3vw,2.1rem);line-height:1.2;margin-bottom:.6rem}
.panel .d{color:var(--muted);font-size:1.02rem;max-width:32rem;margin-bottom:1.25rem}
.rel{display:grid;gap:.5rem;margin-bottom:1.5rem;list-style:none}
.rel li{position:relative;padding-left:1.1rem;font-size:.95rem}
.rel li::before{content:"";position:absolute;left:0;top:.62em;width:6px;height:6px;border-radius:50%;background:var(--accent)}
.rel small{color:var(--faint);margin-left:.4rem}
.panel .cover{margin:0 auto}
@media(min-width:900px){.panel .cover{width:100%;max-width:17rem}}
@media(max-width:899px){.rel{max-width:22rem;margin-left:auto;margin-right:auto;text-align:left}.panel .btn{width:100%}}
@media(max-width:599px){.ptabs{display:grid;grid-template-columns:1fr 1fr;width:100%}.ptab{padding:0 .6rem 0 .4rem;font-size:.85rem;justify-content:flex-start}}
'''
DATA2 = [
 ('Mandir and history','The stories, history and heritage behind our temples, told simply.',[('Temple stories on Instagram','now')],'Follow on Instagram'),
 ('Rituals and traditions','Why, how and when rituals are done, so you understand the meaning and not only the steps.',[('Daily Puja Guide for Beginners','planned'),('Hindu Rituals and Traditions Handbook','planned')],'Join the early-access list'),
 ('Scriptures and philosophy','The Gita, Ramayana and Mahabharata and what they teach, in plain language.',[('Bhagavad Gita Beginner Study Guide','planned'),('Live Gita sessions','coming soon')],'Join the early-access list'),
 ('Festivals and vrat','Festival calendars, preparation and the meaning behind each vrat.',[('The Hindu Festival and Vrat Companion','coming first'),('Free festival and vrat calendar','coming first')],'Get early access'),
]
body2 = f'''<section class="learn"><div class="wrapx o2">
  <span class="tag">Learn</span>
  <h2 class="sh">Learn the stories behind the tradition</h2>
  <p class="intro">Hindu history, temples, rituals and scriptures, told in simple Hindi on Instagram. Pick a topic to see what I share and what is coming.</p>
  <div class="ptabs" role="tablist">{''.join(f'<button class="ptab" role="tab" data-i="{i}" aria-selected="{"true" if i==3 else "false"}">{P[i][2]}<span>{DATA2[i][0].split(" and ")[0]}</span></button>' for i in range(4))}</div>
  <div class="panel" id="panel">
    <div>
      <span class="tag" id="pTag">Festivals and vrat</span>
      <h3 id="pTitle"></h3>
      <p class="d" id="pDesc"></p>
      <ul class="rel" id="pRel"></ul>
      <a class="btn" id="pBtn" href="#">Get early access</a>
    </div>
    {COVER}
  </div>
</div></section>'''
import json
js2 = '<script>const D=' + json.dumps([dict(t=a,d=b,r=c,b=e) for a,b,c,e in DATA2]) + ''';
const tabs=[...document.querySelectorAll('.ptab')];
function show(i){
  tabs.forEach((t,k)=>t.setAttribute('aria-selected',k===i?'true':'false'));
  const d=D[i], p=document.getElementById('panel');
  p.style.animation='none'; void p.offsetWidth; p.style.animation='';
  document.getElementById('pTag').textContent=d.t; document.getElementById('pTitle').textContent=d.t;
  document.getElementById('pDesc').textContent=d.d;
  document.getElementById('pRel').innerHTML=d.r.map(x=>'<li>'+x[0]+'<small>'+x[1]+'</small></li>').join('');
  document.getElementById('pBtn').textContent=d.b;
}
tabs.forEach((t,i)=>t.addEventListener('click',()=>show(i)));
show(3);
</script>'''

# ------------- Option 3: bento grid -------------
css3 = '''
.o3 .head{text-align:center;margin-bottom:2.5rem}
.o3 .intro{margin:.9rem auto 0}
.bento{display:grid;grid-template-columns:minmax(0,1fr);gap:1.1rem}
@media(min-width:900px){.bento{grid-template-columns:1.15fr 1fr 1fr;grid-template-rows:auto auto;gap:1.25rem}.big{grid-row:1 / span 2}}
.tile{background:var(--bg);border:1px solid var(--border);border-radius:12px;padding:1.75rem 1.5rem;transition:border-color .3s var(--ease),box-shadow .3s var(--ease)}
.tile:hover{border-color:rgba(255,111,30,.5);box-shadow:0 10px 30px rgba(33,37,43,.06)}
.tile .pi{margin-bottom:1rem}
.tile h3{font-family:var(--display);font-weight:500;font-size:1.3rem;line-height:1.25;margin-bottom:.4rem}
.tile p{color:var(--muted);font-size:.925rem}
.big{background:var(--tint);border-color:transparent;display:flex;flex-direction:column;align-items:center;text-align:center;justify-content:center;padding:2.25rem 1.75rem}
.big:hover{border-color:transparent;box-shadow:none}
.big .cover{margin:1rem auto 1.5rem}
.big h3{font-family:var(--display);font-weight:600;font-size:1.55rem;line-height:1.2;margin-bottom:.5rem}
.big p{color:var(--muted);font-size:.95rem;margin-bottom:1.25rem;max-width:22rem}
.big .btn{width:100%}
@media(max-width:899px){.tile{text-align:center}.tile .pi{margin-left:auto;margin-right:auto}.big{order:-1}}
'''
body3 = f'''<section class="learn"><div class="wrapx o3">
  <div class="head">
    <span class="tag">Learn</span>
    <h2 class="sh">Learn the stories behind the tradition</h2>
    <p class="intro">Hindu history, temples, rituals and scriptures, told in simple Hindi on Instagram. Here is what I share, and what I am building next.</p>
  </div>
  <div class="bento">
    <div class="tile big">
      <span class="tag">Coming first</span>
      {COVER}
      <h3>The Hindu Festival and Vrat Companion</h3>
      <p>One guide for the festivals and vrats you observe: what each one means, how to prepare, and what you will need.</p>
      <a class="btn" href="#">Get early access</a>
      <a class="hl" href="#">See the guide</a>
    </div>
    {''.join(f'<div class="tile">{ic_}<h3>{t}</h3><p>{d}</p></div>' for t,d,ic_ in P)}
    <div class="tile" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:#fff">
      <span class="tag">Instagram</span>
      <h3>New stories every week</h3>
      <p style="margin-bottom:1rem">Follow along for temple stories, rituals and Gita ideas.</p>
      <a class="hl" href="https://www.instagram.com/timelinebyharsh/">Follow @timelinebyharsh</a>
    </div>
  </div>
</div></section>'''

# "New stories every week" is a claim about posting frequency, so soften it
body3 = body3.replace('New stories every week','Stories on Instagram').replace('Follow along for temple stories, rituals and Gita ideas.','Temple stories, rituals and Gita ideas, told in simple Hindi.')

for fn, name, css, body, js in [('learn-1-editorial','Learn option 1: editorial list + guide card',css1,body1,''),
                                ('learn-2-tabs','Learn option 2: topic tabs',css2,body2,js2),
                                ('learn-3-bento','Learn option 3: bento grid',css3,body3,'')]:
    h = HEAD.replace('@@NAME@@', name).replace('@@CSS@@', css).replace('@@BODY@@', body).replace('@@JS@@', js)
    open(f'learn-options/{fn}.html', 'w', encoding='utf-8').write(h)
print('learn previews written')
