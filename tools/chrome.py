#!/usr/bin/env python3
"""One header (and one mobile Book a call bar on sub-pages) for every page, English and Hinglish.
Idempotent: run it after any build script.   python3 tools/chrome.py"""
import re, glob, os

IG = 'https://www.instagram.com/timelinebyharsh/'

def header(path):
    hi = path.startswith('hi/')
    name = path.split('/')[-1]
    logo = ('../' if hi else '') + 'assets/logo.jpg'
    def cur(href): return ' aria-current="page"' if href == name else ''
    links = [('index.html#diagnostic', 'Find your fit'), ('index.html#journey', 'How it works'), ('index.html#services', 'Sessions'),
             ('guides.html', 'Guides'), ('index.html#faq', 'Questions')]
    nav = ''.join(f'<li class="nav-item"><a href="{h}"{cur(h)}>{t}</a></li>' for h, t in links)
    if hi:
        lang = (f'<div class="lang-switch" role="group" aria-label="Language"><a href="../{name}" hreflang="en" lang="en" title="English">EN</a>'
                f'<span class="on" aria-current="true">HI</span></div>')
    else:
        lang = (f'<div class="lang-switch" role="group" aria-label="Language"><span class="on" aria-current="true">EN</span>'
                f'<a href="hi/{name}" hreflang="hi" lang="hi" title="Hinglish">HI</a></div>')
    return f'''<header class="site-header">
    <div class="container header-inner">
      <div class="site-brand"><a class="b-av" href="index.html" aria-label="Home"><img class="brand-logo" src="{logo}" width="40" height="40" alt="Harsh Upadhyay"></a><span class="b-txt"><a class="b-name" href="index.html">Harsh</a><a class="b-ig" href="{IG}" target="_blank" rel="noopener noreferrer">@timelinebyharsh</a></span></div>
      <ul class="nav-menu">{nav}</ul>
      <div class="hdr-actions">{lang}<a href="index.html#booking" class="header-cta">Book a call</a></div>
    </div>
  </header>'''

BAR = '''<div class="mobile-bar show" id="mobileBar"><a href="index.html#booking" class="mobile-bar-cta">Book a call</a></div>
<script>
(function () {
  var bar = document.getElementById('mobileBar'), ft = document.querySelector('footer');
  if (!bar || !ft || !('IntersectionObserver' in window)) return;
  new IntersectionObserver(function (e) { bar.classList.toggle('show', !e[0].isIntersecting); }).observe(ft);
})();
</script>'''

def apply(path):
    t = open(path, encoding='utf-8').read()
    n = len(t)
    t, k = re.subn(r'<header[^>]*>.*?</header>', lambda m: header(path), t, count=1, flags=re.S)
    if k == 0: raise SystemExit('no header in ' + path)
    if path not in ('index.html', 'hi/index.html') and 'id="mobileBar"' not in t:
        t = t.replace('</body>', BAR + '\n</body>', 1)
    open(path, 'w', encoding='utf-8').write(t)

if __name__ == '__main__':
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    pages = sorted(glob.glob('*.html')) + sorted(glob.glob('hi/*.html'))
    for p in pages: apply(p)
    print('header applied to', len(pages), 'pages')
