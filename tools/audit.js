(() => {
  const iw = innerWidth, out = { w: iw, sw: document.documentElement.scrollWidth, over: [], clip: [], tap: [], tiny: [], img: [] };
  const skip = e => e.closest('.marquee,.hero-waves,.pay-modal,.hp,.mobile-bar') || e.className === 'hp';
  const name = e => (e.id ? '#' + e.id : '') + (typeof e.className === 'string' && e.className ? '.' + e.className.trim().split(/\s+/)[0] : e.tagName.toLowerCase());
  document.querySelectorAll('body *').forEach(e => {
    if (skip(e)) return;
    const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden') return;
    const r = e.getBoundingClientRect(); if (r.width === 0 || r.height === 0) return;
    if (cs.position !== 'fixed' && (r.right > iw + 1 || r.left < -1)) out.over.push(name(e) + ':' + Math.round(r.left) + '-' + Math.round(r.right));
    if (['H1','H2','H3','H4','P','LI','A','BUTTON','SPAN','LABEL','SUMMARY'].includes(e.tagName) && e.scrollWidth > e.clientWidth + 2 && cs.overflowX !== 'auto' && cs.overflowX !== 'scroll' && cs.display !== 'inline') out.clip.push(name(e) + ':' + e.scrollWidth + '>' + e.clientWidth);
    if (iw <= 820 && ['A', 'BUTTON', 'SUMMARY', 'INPUT', 'SELECT', 'TEXTAREA'].includes(e.tagName) && !(e.tagName === 'INPUT' && (e.type === 'checkbox' || e.type === 'radio')) && cs.position !== 'fixed') {
      const insideText = e.tagName === 'A' && e.closest('p,li') && !e.closest('.footer-col,.footer-bottom,nav');
      const brandLink = e.classList.contains('b-name') || e.classList.contains('b-ig') || !!e.closest('.lang-switch');
      if (!insideText && (brandLink ? r.height < 24 : (r.height < 40 || r.width < 40))) out.tap.push(name(e) + ':' + Math.round(r.width) + 'x' + Math.round(r.height) + '|' + (e.textContent || '').trim().slice(0, 18));
    }
    const own = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (own && parseFloat(cs.fontSize) < 11.5) out.tiny.push(name(e) + ':' + cs.fontSize);
    if (e.tagName === 'IMG' && (!e.complete || e.naturalWidth === 0)) out.img.push(e.src.slice(-30));
  });
  const hd = document.querySelector('header'); if (hd && hd.getBoundingClientRect().height > 84) out.over.push('header-wrap:' + Math.round(hd.getBoundingClientRect().height));
  document.querySelectorAll('.footer-col, .fc').forEach(c => { const h = c.querySelector('h4'), u = c.querySelector('ul'); if (h && u && u.getBoundingClientRect().top < h.getBoundingClientRect().bottom - 1) out.over.push('footer-column-side-by-side'); });
  for (const k of ['over', 'clip', 'tap', 'tiny', 'img']) out[k] = [...new Set(out[k])].slice(0, 8);
  return JSON.stringify(out);
})()
