#!/usr/bin/env python3
"""Inserts the audience / reach block into collaborate.html and hi/collaborate.html.
Numbers come from the Instagram dashboard screenshots (30 days, 8 Oct to 6 Nov 2026).
Run AFTER tools/build_legal_hi.py (that script rewrites hi/collaborate.html). Idempotent."""
import re

T = {
 'en': dict(
  h='Who is watching', sub='Numbers from my Instagram dashboard for the last 30 days (8 Oct to 6 Nov 2026).',
  gender='Men 77.8%, women 22.2%',
  stats=[('3.1M','Views','+58.6% vs 7 Oct'),('1.9M','Viewers','Unique accounts'),('12.4K','Followers','+3,720 in 30 days'),('95%','In India','Hindi first audience')],
  charts=[('Age',[('13-17',11.7),('18-24',24.0),('25-34',36.4),('35-44',17.9),('45+',9.9)]),
          ('Top countries',[('India',95.0),('Nepal',1.1),('UAE',0.7),('USA',0.4)]),
          ('Top cities',[('Delhi',3.4),('Mumbai',3.1),('Bangalore',2.7),('Ahmedabad',1.6),('Pune',1.5)]),
          ('Languages',[('Hindi',53.2),('English',27.0),('Marathi',5.3),('Gujarati',4.5)])],
  top='Best reels this month', topn=[('Sharad Purnima ki chaandni','25 Oct','440K'),('Mahashtami aur Mahanavami','18 Oct','190K'),('Din ki shuruaat Bhagwan Narayan se','28 Oct','190K')],
  views='views', proof='The dashboard, unedited', proofsub='Screenshots taken straight from Instagram. Swipe to see all six.',
  caps=['Summary','Performance','Content','Audience','Countries and languages','Cities'],
  cta='Want a fresh export for your campaign?', btn='Message on Instagram', mail='Or email timelinebyharsh@gmail.com',
  note='Instagram numbers for the 30 days to 6 Nov 2026. They change daily, so I send a current export on request. Views are all plays, viewers are unique accounts.'),
 'hi': dict(
  h='Who is watching', sub='Mere Instagram dashboard ke pichhle 30 din ke numbers (8 Oct se 6 Nov 2026).',
  gender='Men 77.8%, women 22.2%',
  stats=[('3.1M','Views','+58.6% vs 7 Oct'),('1.9M','Viewers','Alag-alag accounts'),('12.4K','Followers','30 din mein +3,720'),('95%','In India','Hindi audience sabse zyada')],
  charts=[('Age',[('13-17',11.7),('18-24',24.0),('25-34',36.4),('35-44',17.9),('45+',9.9)]),
          ('Top countries',[('India',95.0),('Nepal',1.1),('UAE',0.7),('USA',0.4)]),
          ('Top cities',[('Delhi',3.4),('Mumbai',3.1),('Bangalore',2.7),('Ahmedabad',1.6),('Pune',1.5)]),
          ('Languages',[('Hindi',53.2),('English',27.0),('Marathi',5.3),('Gujarati',4.5)])],
  top='Best reels this month', topn=[('Sharad Purnima ki chaandni','25 Oct','440K'),('Mahashtami aur Mahanavami','18 Oct','190K'),('Din ki shuruaat Bhagwan Narayan se','28 Oct','190K')],
  views='views', proof='The dashboard, unedited', proofsub='Screenshots seedhe Instagram se liye gaye hain. Chhahon dekhne ke liye swipe karein.',
  caps=['Summary','Performance','Content','Audience','Countries and languages','Cities'],
  cta='Apne campaign ke liye taaza export chahiye?', btn='Message on Instagram', mail='Ya email karein timelinebyharsh@gmail.com',
  note='Instagram ke numbers, 6 Nov 2026 tak ke 30 din ke. Ye roz badalte hain, isliye main maangne par taaza export bhejta hoon. Views matlab saare plays, viewers matlab alag-alag accounts.'),
}
IMGS = ['home','performance','content','audience','locations','cities']

def block(t, pre):
    stats = ''.join(f'<div class="rs"><b>{n}</b><span>{l}</span><i>{s}</i></div>' for n, l, s in t['stats'])
    charts = ''
    for title, rows in t['charts']:
        mx = max(v for _, v in rows)
        r = ''.join(f'<div class="rb"><em>{k}</em><span class="bar"><u style="width:{max(v/mx*100,2):.1f}%"></u></span><b>{v:g}%</b></div>' for k, v in rows)
        extra = f'<p class="rg">{t["gender"]}</p>' if title == 'Age' else ''
        charts += f'<div class="rc"><h3>{title}</h3>{extra}{r}</div>'
    top = ''.join(f'<li><span>{a}<small>{b}</small></span><b>{c}<small> {t["views"]}</small></b></li>' for a, b, c in t['topn'])
    figs = ''.join(f'<figure><a href="{pre}assets/reach/{n}.jpg" target="_blank" rel="noopener"><img src="{pre}assets/reach/{n}.jpg" width="430" height="733" loading="lazy" alt="Instagram dashboard: {c}"></a><figcaption>{c}</figcaption></figure>' for n, c in zip(IMGS, t['caps']))
    return f'''<!--reach-->
<section class="reach">
  <div class="wrap">
    <h2 class="rh">{t['h']}</h2>
    <p class="rsub">{t['sub']}</p>
    <div class="rstats">{stats}</div>
    <div class="rcharts">{charts}</div>
    <div class="rtop"><h3>{t['top']}</h3><ol>{top}</ol></div>
  </div>
  <div class="rproof">
    <div class="wrap"><h3>{t['proof']}</h3><p>{t['proofsub']}</p></div>
    <div class="rrow" tabindex="0" aria-label="{t['proof']}">{figs}</div>
  </div>
  <div class="wrap rcta"><p>{t['cta']}</p><a class="cta" href="https://www.instagram.com/timelinebyharsh/" target="_blank" rel="noopener noreferrer">{t['btn']}</a><a class="rmail" href="mailto:timelinebyharsh@gmail.com">{t['mail']}</a><p class="rnote">{t['note']}</p></div>
</section>
<!--/reach-->
'''

for path, lang, pre in (('collaborate.html', 'en', ''), ('hi/collaborate.html', 'hi', '../')):
    s = open(path, encoding='utf-8').read()
    s = re.sub(r'<!--reach-->.*?<!--/reach-->\n', '', s, flags=re.S)
    assert '<article>' in s, path
    s = s.replace('<article>', block(T[lang], pre) + '<article>', 1)
    open(path, 'w', encoding='utf-8').write(s)
    print('reach block in', path)
