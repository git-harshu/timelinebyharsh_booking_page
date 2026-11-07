#!/usr/bin/env python3
"""Three cleaner versions of the guide card inside the chosen 'topic tabs' option (preview only).
Needs learn-options/learn-2-tabs.html from build_learn_previews.py as the template."""
import re, json
base = open('learn-options/learn-2-tabs.html', encoding='utf-8').read()

CARDS = [
 dict(topic='Mandir and history', desc='The stories, history and heritage behind our temples, told simply.',
      status='On Instagram', title='Temple stories', line='Temple stories, history and heritage, told in simple Hindi.', items=[], cta='Follow on Instagram', href='https://www.instagram.com/timelinebyharsh/', icon='trishul'),
 dict(topic='Rituals and traditions', desc='Why, how and when rituals are done, so you understand the meaning and not only the steps.',
      status='Planned', title='Daily Puja Guide for Beginners', line='A simple start for a daily puja: what you need and the usual order.', items=[], cta='Join the list', href='#', icon='diya'),
 dict(topic='Scriptures and philosophy', desc='The Gita, Ramayana and Mahabharata and what they teach, in plain language.',
      status='Planned', title='Bhagavad Gita Beginner Study Guide', line='A plain-language introduction to the main ideas of the Gita.', items=[], cta='Join the list', href='#', icon='lotus'),
 dict(topic='Festivals and vrat', desc='Festival calendars, preparation and the meaning behind each vrat.',
      status='Coming first', title='The Hindu Festival and Vrat Companion', line='One guide for the festivals and vrats you observe: what each one means, how to prepare, and what you will need.',
      items=['Preparation checklists', 'Puja samagri lists', 'Mantra meanings'], cta='Get early access', href='#', icon='om', more='See the guide'),
]
ICON = {'trishul': '<svg aria-hidden="true"><use href="#trishul"/></svg>', 'diya': '<svg aria-hidden="true"><use href="#diya"/></svg>', 'lotus': '<svg aria-hidden="true"><use href="#lotus"/></svg>', 'om': '<span class="omg" aria-hidden="true">ॐ</span>'}
cj = json.dumps(CARDS, ensure_ascii=False)
ij = json.dumps(ICON, ensure_ascii=False)

COMMON_CSS = '''
.o2 .panel{display:block;background:none;padding:0;text-align:center;animation:settle .5s var(--ease) both}
.ph{max-width:38rem;margin:0 auto 1.75rem}
.ph h3{font-family:var(--display);font-weight:600;font-size:clamp(1.5rem,3vw,2rem);line-height:1.2;margin-bottom:.5rem}
.ph .d{color:var(--muted);font-size:1rem;margin:0}
.chipx{display:inline-block;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:var(--accent);margin-bottom:.5rem}
.dots{list-style:none;display:grid;gap:.4rem}
.dots li{position:relative;padding-left:1.1rem;font-size:.95rem;color:var(--text)}
.dots li::before{content:"";position:absolute;left:0;top:.62em;width:6px;height:6px;border-radius:50%;background:var(--accent)}
.acts{display:flex;flex-direction:column;gap:.5rem;align-items:stretch;margin-top:1.25rem}
@media(min-width:560px){.acts{flex-direction:row;align-items:center;gap:1.5rem}}
.acts .hl{justify-content:center}
'''
VARIANTS = {
 'a-flat': ('Guide card A: flat product card', '''
.pc{max-width:34rem;margin:0 auto;background:var(--tint);border-radius:12px;padding:2rem 1.75rem;text-align:left}
.pc h4{font-family:var(--display);font-weight:600;font-size:1.65rem;line-height:1.2;margin-bottom:.5rem}
.pc p{color:var(--muted);font-size:.975rem}
.pc .dots{margin-top:1rem}
@media(max-width:559px){.pc{padding:1.75rem 1.25rem;text-align:center}.pc .dots{text-align:left;max-width:15rem;margin-left:auto;margin-right:auto}}
''', '''
function card(c){
  const items=c.items.length?'<ul class="dots">'+c.items.map(i=>'<li>'+i+'</li>').join('')+'</ul>':'';
  const more=c.more?'<a class="hl" href="guides.html">'+c.more+'</a>':'';
  return '<div class="pc"><span class="chipx">'+c.status+'</span><h4>'+c.title+'</h4><p>'+c.line+'</p>'+items+'<div class="acts"><a class="btn" href="'+c.href+'">'+c.cta+'</a>'+more+'</div></div>';
}'''),
 'b-cover': ('Guide card B: clean cover beside text', '''
.pc{max-width:44rem;margin:0 auto;background:#fff;border:1px solid var(--border);border-radius:12px;padding:1.5rem;display:grid;grid-template-columns:minmax(0,1fr);gap:1.5rem;align-items:center;text-align:left}
@media(min-width:700px){.pc{grid-template-columns:9.5rem minmax(0,1fr);gap:2rem;padding:1.75rem 2rem}}
.cv{width:8.5rem;aspect-ratio:3/4;margin:0 auto;border-radius:10px;background:var(--tint);display:flex;flex-direction:column;justify-content:space-between;padding:1rem .9rem;position:relative}
.cv.icon{aspect-ratio:1;width:7rem;border-radius:50%;place-items:center;justify-content:center;align-items:center;margin:0 auto}
.cv.icon .pi{width:3.4rem;height:3.4rem;background:#fff}.cv.icon .pi svg{width:1.8rem;height:1.8rem}.cv.icon .pi .omg{font-size:1.8rem}
.cv .o{font-family:var(--deva);font-size:1.7rem;line-height:1;color:var(--accent)}
.cv strong{font-family:var(--display);font-weight:600;font-size:.98rem;line-height:1.2}
.pc h4{font-family:var(--display);font-weight:600;font-size:1.45rem;line-height:1.2;margin:.1rem 0 .4rem}
.pc p{color:var(--muted);font-size:.95rem}
.pc .dots{margin-top:.9rem}
@media(max-width:699px){.pc{text-align:center}.pc .dots{text-align:left;max-width:15rem;margin-left:auto;margin-right:auto}}
''', '''
function card(c){
  const vis=c.icon==='om'?'<div class="cv"><span class="o">ॐ</span><strong>Festival and Vrat Companion</strong></div>':'<div class="cv icon"><span class="pi">'+ICON[c.icon]+'</span></div>';
  const items=c.items.length?'<ul class="dots">'+c.items.map(i=>'<li>'+i+'</li>').join('')+'</ul>':'';
  const more=c.more?'<a class="hl" href="guides.html">'+c.more+'</a>':'';
  return '<div class="pc">'+vis+'<div><span class="chipx">'+c.status+'</span><h4>'+c.title+'</h4><p>'+c.line+'</p>'+items+'<div class="acts"><a class="btn" href="'+c.href+'">'+c.cta+'</a>'+more+'</div></div></div>';
}'''),
 'c-bar': ('Guide card C: one-line bar', '''
.pc{max-width:44rem;margin:0 auto;background:#fff;border:1px solid var(--border);border-radius:12px;padding:1.5rem;display:grid;grid-template-columns:minmax(0,1fr);gap:1.1rem;align-items:center;text-align:left;transition:border-color .3s var(--ease),box-shadow .3s var(--ease)}
.pc:hover{border-color:rgba(255,111,30,.5);box-shadow:0 10px 30px rgba(33,37,43,.06)}
@media(min-width:700px){.pc{grid-template-columns:minmax(0,1fr) auto;gap:2rem;padding:1.5rem 2rem}}
.pc h4{font-family:var(--display);font-weight:600;font-size:1.35rem;line-height:1.25;margin-bottom:.25rem}
.pc p{color:var(--muted);font-size:.925rem;max-width:30rem}
.pc .side{display:flex;flex-direction:column;gap:.4rem;align-items:stretch}
.pc .side .hl{justify-content:center;min-height:36px}
@media(max-width:699px){.pc{text-align:center}.pc p{margin:0 auto}}
''', '''
function card(c){
  const more=c.more?'<a class="hl" href="guides.html">'+c.more+'</a>':'';
  return '<div class="pc"><div><span class="chipx">'+c.status+'</span><h4>'+c.title+'</h4><p>'+c.line+'</p></div><div class="side"><a class="btn" href="'+c.href+'">'+c.cta+'</a>'+more+'</div></div>';
}'''),
}

for key, (name, css, jscard) in VARIANTS.items():
    t = base
    t = t.replace('Learn option 2: topic tabs', name)
    t = t.replace('</style>', COMMON_CSS + css + '</style>', 1)
    # panel markup: header + card slot (no duplicated eyebrow, no cover on tabs that have no product)
    t = re.sub(r'<div class="panel" id="panel">.*?</div>\s*</div></section>',
               '<div class="panel" id="panel"><div class="ph"><h3 id="pTitle"></h3><p class="d" id="pDesc"></p></div><div id="pCard"></div></div>\n</div></section>', t, count=1, flags=re.S)
    script = '<script>const C=' + cj + ';const ICON=' + ij + ';\n' + jscard + '''
const tabs=[...document.querySelectorAll('.ptab')];
function show(i){
  tabs.forEach((t,k)=>t.setAttribute('aria-selected',k===i?'true':'false'));
  const c=C[i], p=document.getElementById('panel');
  p.style.animation='none'; void p.offsetWidth; p.style.animation='';
  document.getElementById('pTitle').textContent=c.topic;
  document.getElementById('pDesc').textContent=c.desc;
  document.getElementById('pCard').innerHTML=card(c);
}
tabs.forEach((t,i)=>t.addEventListener('click',()=>show(i)));
show(3);
</script>'''
    t = re.sub(r'<script>const D=.*?</script>', lambda m: script, t, count=1, flags=re.S)
    open(f'learn-options/learn-2{key}.html', 'w', encoding='utf-8').write(t)
    print('written learn-2' + key)
