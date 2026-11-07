#!/usr/bin/env python3
"""Writes three scroll-driven Clarity Finder previews into finder-options/ (preview only, not on the live site)."""
import json, math
DATA=[
 dict(label="Overthinking",sub="Too many ideas, nothing finished.",short="Overthinking",title="Clarity Call",price="₹299 · 30 minutes",body="<b>What helps:</b> Too many options can feel like a lack of discipline, but it is mostly noise. In thirty minutes we find the one thing that matters and agree three steps for tomorrow."),
 dict(label="A routine that keeps slipping",sub="Fresh start Monday, lost by Thursday.",short="Routine",title="Dincharya Reset",price="₹499 · 45 minutes",body="<b>What helps:</b> A routine borrowed from someone else rarely lasts. We build a simple morning and evening rhythm around your real work hours, one you can keep on a bad day too."),
 dict(label="A big decision",sub="A big fork and no honest view.",short="Decision",title="Deep Dive",price="₹699 · 60 minutes",body="<b>What helps:</b> Family and friends give kind advice. You may need an outside view, free of emotional bias, to weigh your options and choose with a calm mind."),
 dict(label="Someone to talk to",sub="Somewhere safe to say it out loud.",short="Talk",title="Clarity Call",price="₹299 · 30 minutes",body="<b>What helps:</b> Often you already know the answer, but the noise around you is louder. This is a quiet, judgment-free space to say it out loud."),
]
dj=json.dumps(DATA,ensure_ascii=False)

HEAD='''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@NAME@@ | Clarity Finder preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Fraunces:opsz,wght,SOFT@9..144,300..700,0..100&family=Tiro+Devanagari+Hindi&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../hero-options/base.css">
<style>
:root{--display:'Fraunces',Georgia,serif}
body{font-variation-settings:'SOFT' 100,'WONK' 0}
.intro{min-height:70vh;display:grid;place-items:center;text-align:center;background:linear-gradient(180deg,#fff,#FFF6EC);padding:3rem 1.5rem}
.intro h1{font-size:clamp(2rem,4vw,3rem);font-weight:600;line-height:1.15;margin-bottom:.75rem}
.intro p{color:var(--muted)}
.scroll-hint{margin-top:2rem;font-size:.85rem;color:var(--faint);letter-spacing:.14em;text-transform:uppercase}
.outro{min-height:60vh;display:grid;place-items:center;text-align:center;background:#fff;padding:3rem 1.5rem}
.outro h2{font-family:var(--display);font-weight:600;font-size:clamp(1.8rem,3.4vw,2.4rem)}
.finder{position:relative;height:340vh;background:var(--tint)}
.stage{position:sticky;top:4.25rem;height:calc(100vh - 4.25rem);display:flex;flex-direction:column;justify-content:center;overflow:hidden}
.f-head{text-align:center;margin-bottom:1rem}
.f-eyebrow{display:block;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--accent);margin-bottom:.4rem}
.f-head h2{font-family:var(--display);font-weight:600;font-size:clamp(1.8rem,3vw,2.4rem);line-height:1.2}
.f-head p{color:var(--muted);font-size:.95rem;margin-top:.35rem}
.detail{background:#fff;border-radius:12px;padding:2rem;text-align:left}
.detail .d-top{display:flex;justify-content:space-between;align-items:baseline;gap:1rem;flex-wrap:wrap;padding-bottom:1rem;margin-bottom:1rem;border-bottom:1px solid var(--border)}
.detail h3{font-family:var(--display);font-weight:600;font-size:1.5rem}
.detail .price{color:var(--accent);font-weight:600}
.detail .body{color:var(--muted);font-size:.975rem;line-height:1.7;margin-bottom:1.5rem}
.detail .body b{color:var(--text)}
.detail .note{font-size:.8rem;color:var(--faint);margin-top:.9rem}
.detail .btn{width:100%}
.swap{animation:settle .55s var(--ease) both}
.dots{display:flex;gap:.5rem;justify-content:center;margin-top:1rem}
.dots i{width:7px;height:7px;border-radius:50%;background:var(--border-strong);transition:background .3s,transform .3s}
.dots i.on{background:var(--accent);transform:scale(1.3)}
.item{cursor:pointer;border:0;background:none;font:inherit;color:inherit;text-align:left}
.item:focus-visible{outline:2px solid var(--accent);outline-offset:4px;border-radius:12px}
@@CSS@@
@media(max-width:899px),(prefers-reduced-motion:reduce){
  .finder{height:auto;padding:3.5rem 0}
  .stage{position:static;height:auto;display:block;overflow:visible}
}
</style>
</head>
<body>
<header><div class="wrap bar">
  <a class="brand" href="#"><img src="../assets/logo.jpg" width="40" height="40" alt="Harsh Upadhyay"><span><b>Timeline by Harsh</b><small>@timelinebyharsh</small></span></a>
  <nav><ul><li><a href="#">Find your fit</a></li><li><a href="#">How it works</a></li><li><a href="#">Sessions</a></li><li><a href="#">Questions</a></li></ul></nav>
  <a class="cta" href="#">Book a call</a>
</div></header>
<section class="intro"><div><h1>It is rarely a lack of discipline.</h1><p>Scroll down to try the new Clarity Finder.</p><div class="scroll-hint">Scroll</div></div></section>
@@BODY@@
<section class="outro"><h2>The rest of the page continues here.</h2></section>
<div class="peek-note">@@NAME@@ (preview only, not on the live site)</div>
<script>
const DATA=@@DATA@@;
const N=DATA.length;
const finder=document.querySelector('.finder');
const items=[...document.querySelectorAll('.item')];
const dots=[...document.querySelectorAll('.dots i')];
const $=s=>document.querySelector(s);
const mq=window.matchMedia('(max-width:899px)');
let cur=-1, mobileF=0;
function setSel(i){
  cur=i;
  const d=DATA[i];
  const box=$('.detail'); box.classList.remove('swap'); void box.offsetWidth; box.classList.add('swap');
  $('#dTitle').textContent=d.title; $('#dPrice').textContent=d.price; $('#dBody').innerHTML=d.body;
  items.forEach(el=>el.classList.toggle('on',+el.dataset.i===i));
  dots.forEach((x,k)=>x.classList.toggle('on',k===i));
  if(typeof onSel==='function') onSel(i);
}
function scrollProgress(){
  const r=finder.getBoundingClientRect();
  const total=finder.offsetHeight-$('.stage').offsetHeight;
  return Math.min(1,Math.max(0,-r.top/total));
}
function frame(){
  const f=mq.matches?mobileF:scrollProgress()*(N-1);
  items.forEach(el=>layout(el,+el.dataset.i-f,f));
  if(typeof onFrame==='function') onFrame(f);
  const idx=Math.round(f); if(idx!==cur) setSel(idx);
}
let t=false; addEventListener('scroll',()=>{if(!t){t=true;requestAnimationFrame(()=>{t=false;frame()})}},{passive:true});
addEventListener('resize',frame);
items.forEach(el=>el.addEventListener('click',()=>{
  const i=+el.dataset.i;
  if(mq.matches){mobileF=i;frame();return}
  const total=finder.offsetHeight-$('.stage').offsetHeight;
  window.scrollTo({top:finder.offsetTop+total*(i/(N-1)),behavior:'smooth'});
}));
@@JS@@
frame();
</script>
</body>
</html>
'''
DETAIL='<div class="detail"><div class="d-top"><h3 id="dTitle"></h3><span class="price" id="dPrice"></span></div><p class="body" id="dBody"></p><a class="btn" href="#">Book this session</a><p class="note">Written summary on WhatsApp within 24 hours</p></div>'
HEADBLK='<div class="f-head wrap"><span class="f-eyebrow">Clarity Finder</span><h2>Which one sounds like you?</h2><p>Scroll to roll through. The one in the middle is yours.</p></div>'
DOTS='<div class="dots">'+'<i></i>'*4+'</div>'
MASK='-webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 28%,#000 72%,transparent 100%);mask-image:linear-gradient(to bottom,transparent 0,#000 28%,#000 72%,transparent 100%)'

css1=f'''
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;max-width:1040px;margin:0 auto;padding:0 2rem;width:100%}}
.drum{{position:relative;height:26rem;perspective:900px;{MASK}}}
.drum .item{{position:absolute;left:0;right:0;top:50%;height:5.5rem;margin-top:-2.75rem;display:flex;align-items:center;gap:1rem;padding:0 1.4rem;background:#fff;border-radius:12px;will-change:transform,opacity;box-shadow:0 1px 2px rgba(33,37,43,.04);transition:box-shadow .3s}}
.drum .item.on{{box-shadow:0 0 0 2px var(--accent),0 12px 30px rgba(255,111,30,.15)}}
.drum .num{{font-family:var(--display);font-size:1.6rem;color:var(--accent);width:2.2rem;flex-shrink:0}}
.drum .t{{font-family:var(--display);font-weight:500;font-size:1.3rem;line-height:1.25}}
.drum .s{{font-size:.9rem;color:var(--muted);margin-top:.15rem}}
@media(max-width:899px){{.grid{{display:block;padding:0 1.25rem}}.drum{{height:auto;perspective:none;-webkit-mask-image:none;mask-image:none;display:grid;gap:.75rem;margin-bottom:1rem}}.drum .item{{position:static;margin:0;transform:none!important;opacity:1!important}}}}
'''
body1=f'''<section class="finder" id="finder"><div class="stage">
  {HEADBLK}
  <div class="grid">
    <div class="drum">
      {''.join(f'<button class="item" data-i="{i}"><span class="num">0{i+1}</span><span><div class="t">{d["label"]}</div><div class="s">{d["sub"]}</div></span></button>' for i,d in enumerate(DATA))}
    </div>
    {DETAIL}
  </div>
  {DOTS}
</div></section>'''
js1='''
function layout(el,d){
  const a=Math.abs(d);
  el.style.transform=`translateY(${d*92}px) rotateX(${-d*26}deg) scale(${1-Math.min(a,2)*0.1})`;
  el.style.opacity=Math.max(0,1-a*0.62);
  el.style.pointerEvents=a>1.4?'none':'auto';
}
'''
css2=f'''
.odo-wrap{{max-width:900px;margin:0 auto;padding:0 2rem;width:100%;text-align:center}}
.odo{{position:relative;height:15rem;perspective:800px;-webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 30%,#000 70%,transparent 100%);mask-image:linear-gradient(to bottom,transparent 0,#000 30%,#000 70%,transparent 100%)}}
.odo .item{{position:absolute;left:0;right:0;top:50%;height:4.6rem;margin-top:-2.3rem;display:grid;place-items:center;text-align:center;will-change:transform,opacity}}
.odo .t{{font-family:var(--display);font-weight:600;font-size:clamp(2.2rem,4.4vw,3.6rem);line-height:1.1;letter-spacing:-.02em;color:var(--text);transition:color .3s}}
.odo .item.on .t{{color:var(--accent)}}
.odo-lines{{position:absolute;left:50%;top:50%;width:min(34rem,86%);height:4.8rem;transform:translate(-50%,-50%);border-top:1px solid var(--border-strong);border-bottom:1px solid var(--border-strong);pointer-events:none}}
.odo-detail{{max-width:34rem;margin:1.25rem auto 0}}
@media(max-width:899px){{.odo-wrap{{padding:0 1.25rem}}.odo{{height:auto;perspective:none;-webkit-mask-image:none;mask-image:none;display:grid;gap:.5rem;margin-bottom:1rem}}.odo .item{{position:static;margin:0;height:auto;padding:.9rem 0;transform:none!important;opacity:1!important;background:#fff;border-radius:12px}}.odo .t{{font-size:1.5rem}}.odo-lines{{display:none}}}}
'''
body2=f'''<section class="finder" id="finder"><div class="stage">
  {HEADBLK}
  <div class="odo-wrap">
    <div class="odo"><span class="odo-lines" aria-hidden="true"></span>
      {''.join(f'<button class="item" data-i="{i}"><span class="t">{d["label"]}</span></button>' for i,d in enumerate(DATA))}
    </div>
    <div class="odo-detail">{DETAIL}</div>
    {DOTS}
  </div>
</div></section>'''
js2='''
function layout(el,d){
  const a=Math.abs(d);
  el.style.transform=`translateY(${d*78}px) rotateX(${-d*38}deg) scale(${1-Math.min(a,2)*0.14})`;
  el.style.opacity=Math.max(0,1-a*0.7);
  el.style.pointerEvents=a>1.4?'none':'auto';
}
'''
cx,cy,R,RL=280,270,205,248
pos=[]
for i in range(4):
    th=math.radians(180-i*60)
    pos.append((cx+RL*math.cos(th), cy-RL*math.sin(th), cx+R*math.cos(th), cy-R*math.sin(th)))
css3='''
.grid{display:grid;grid-template-columns:1.05fr .95fr;gap:3.5rem;align-items:center;max-width:1080px;margin:0 auto;padding:0 2rem;width:100%}
.dial{position:relative;width:560px;max-width:100%;height:330px;margin:0 auto}
.dial svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.dial .track{fill:none;stroke:var(--border-strong);stroke-width:10;stroke-linecap:round}
.dial .fill{fill:none;stroke:var(--accent);stroke-width:10;stroke-linecap:round}
.dial .tick{fill:#fff;stroke:var(--border-strong);stroke-width:2}
.dial .tick.on{fill:var(--accent);stroke:var(--accent)}
.needle{position:absolute;left:280px;top:270px;width:0;height:0}
.needle i{position:absolute;left:-185px;top:-2px;width:185px;height:4px;border-radius:4px;background:var(--text);transform-origin:185px 50%}
.hub{position:absolute;left:268px;top:258px;width:24px;height:24px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 6px rgba(255,111,30,.2)}
.dial .item{position:absolute;transform:translate(-50%,-50%);padding:.5rem .9rem;border-radius:9999px;background:#fff;white-space:nowrap;font-family:var(--display);font-weight:500;font-size:1.05rem;box-shadow:0 1px 2px rgba(33,37,43,.05);will-change:transform,opacity;transition:background .3s,color .3s,box-shadow .3s}
.dial .item.on{background:var(--accent);color:#fff;box-shadow:0 10px 24px rgba(255,111,30,.3)}
@media(max-width:899px){.grid{display:block;padding:0 1.25rem}.dial{height:auto;width:100%;display:grid;gap:.6rem;margin-bottom:1rem}.dial svg,.needle,.hub{display:none}.dial .item{position:static;transform:none!important;opacity:1!important;border-radius:12px;padding:1rem 1.1rem;white-space:normal;font-size:1.15rem}}
'''
items3=''.join(f'<button class="item" data-i="{i}" style="left:{pos[i][0]:.0f}px;top:{pos[i][1]:.0f}px">{DATA[i]["short"]}</button>' for i in range(4))
ticks=''.join(f'<circle class="tick" cx="{pos[i][2]:.1f}" cy="{pos[i][3]:.1f}" r="9"/>' for i in range(4))
body3=f'''<section class="finder" id="finder"><div class="stage">
  {HEADBLK}
  <div class="grid">
    <div class="dial">
      <svg viewBox="0 0 560 330" aria-hidden="true">
        <path class="track" d="M {cx-R} {cy} A {R} {R} 0 0 1 {cx+R} {cy}" pathLength="100"/>
        <path class="fill" id="fillArc" d="M {cx-R} {cy} A {R} {R} 0 0 1 {cx+R} {cy}" pathLength="100" stroke-dasharray="0 100"/>
        {ticks}
      </svg>
      <div class="needle" aria-hidden="true"><i id="needle"></i></div>
      <span class="hub" aria-hidden="true"></span>
      {items3}
    </div>
    {DETAIL}
  </div>
  {DOTS}
</div></section>'''
js3='''
const needle=document.getElementById('needle'), fillArc=document.getElementById('fillArc'), ticks=[...document.querySelectorAll('.tick')];
function layout(el,d){ const a=Math.abs(d); el.style.opacity=1-Math.min(a,1)*0.35; el.style.transform=`translate(-50%,-50%) scale(${1+(1-Math.min(a,1))*0.12})`; }
function onFrame(f){ needle.style.transform=`rotate(${f*60}deg)`; fillArc.setAttribute('stroke-dasharray',`${f/(N-1)*100} 100`); }
function onSel(i){ ticks.forEach((t,k)=>t.classList.toggle('on',k<=i)); }
'''
for fn,name,css,body,js in [('roll-1-drum','Roll 1: Drum picker',css1,body1,js1),('roll-2-odometer','Roll 2: Odometer',css2,body2,js2),('roll-3-dial','Roll 3: Speedometer dial',css3,body3,js3)]:
    h=HEAD.replace('@@NAME@@',name).replace('@@CSS@@',css).replace('@@BODY@@',body).replace('@@JS@@',js).replace('@@DATA@@',dj)
    open(f'finder-options/{fn}.html','w',encoding='utf-8').write(h)
print('written')
