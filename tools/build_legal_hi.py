#!/usr/bin/env python3
"""Writes the Hinglish (Hindi in English letters) legal/about pages into hi/ and keeps the language switch on the English ones.
Run:  python3 tools/build_legal_hi.py"""
UPD = '8 November 2026'
IG = '<a href="https://www.instagram.com/timelinebyharsh/" rel="noopener noreferrer">@timelinebyharsh</a>'
CONTACT = f'Instagram par {IG} ko message karein, ya apni booking confirmation email ya WhatsApp ka reply karein.'

HEAD = '''<!DOCTYPE html>
<html lang="hi-Latn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Timeline by Harsh</title>
<meta name="description" content="{desc}">
<link rel="alternate" hreflang="en" href="../{fn}">
<link rel="icon" type="image/jpeg" href="../assets/logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Fraunces:opsz,wght,SOFT@9..144,300..700,0..100&family=Tiro+Devanagari+Hindi&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../legal.css">
</head>
<body>
<header>
  <div class="wrap bar">
    <div class="brand"><a class="b-av" href="index.html" aria-label="Home"><img src="../assets/logo.jpg" width="40" height="40" alt="Harsh Upadhyay"></a><span class="b-txt"><a class="b-name" href="index.html">Harsh</a><a class="b-ig" href="https://www.instagram.com/timelinebyharsh/" target="_blank" rel="noopener noreferrer">@timelinebyharsh</a></span></div>
    <nav><a class="lang" href="../{fn}" hreflang="en" lang="en" title="English" aria-label="Switch to English">EN</a><a class="cta" href="index.html#booking">Book a call</a></nav>
  </div>
</header>
<section class="title">
  <div class="wrap rise">
    <h1>{title}</h1>
    <p>{sub}</p>
  </div>
</section>
<article>
{body}
</article>
<footer>
  <div class="wrap top">
    <div class="fb">
      <div class="brand"><a class="b-av" href="index.html" aria-label="Home"><img src="../assets/logo.jpg" width="40" height="40" alt="Harsh Upadhyay"></a><span class="b-txt"><a class="b-name" href="index.html">Harsh</a><a class="b-ig" href="https://www.instagram.com/timelinebyharsh/" target="_blank" rel="noopener noreferrer">@timelinebyharsh</a></span></div>
      <p>Zyada sochne, roz ke routine aur bade faislon ke liye private one-on-one calls.</p>
      <a class="ig" href="https://www.instagram.com/timelinebyharsh/" target="_blank" rel="noopener noreferrer">Instagram</a>
    </div>
    <nav class="fc" aria-label="Explore"><h4>Explore</h4><ul>
      <li><a href="index.html#diagnostic">Find your fit</a></li>
      <li><a href="index.html#journey">How it works</a></li>
      <li><a href="index.html#booking">Choose a time</a></li>
      <li><a href="index.html#faq">Common questions</a></li>
      <li><a href="guides.html">Guides</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="collaborate.html">Collaborate</a></li>
    </ul></nav>
    <nav class="fc" aria-label="Sessions"><h4>Sessions</h4><ul>
      <li><a href="index.html#services">Clarity Call</a></li>
      <li><a href="index.html#services">Dincharya Reset</a></li>
      <li><a href="index.html#services">Deep Dive</a></li>
    </ul></nav>
    <nav class="fc" aria-label="Policies"><h4>Policies</h4><ul>
      <li><a href="privacy.html">Privacy</a></li>
      <li><a href="terms.html">Terms</a></li>
      <li><a href="refund.html">Refunds</a></li>
      <li><a href="cookies.html">Cookies</a></li>
    </ul></nav>
  </div>
  <div class="wrap bottom">
    <p>© 2026 Timeline by Harsh. All rights reserved.</p>
    <p class="note2">Guidance calls therapy, medical, legal ya paison ki salah nahi hain. Kitaabon ke links Amazon affiliate links hain.</p>
    <p class="shloka" aria-hidden="true">ॐ सर्वे भवन्तु सुखिनः</p>
  </div>
</footer>
</body>
</html>
'''

PAGES = {}
PAGES['about.html'] = ('About', 'Main kaun hoon aur ye calls kaise kaam karti hain', 'Harsh Upadhyay ke baare mein aur Timeline by Harsh ki one-on-one guidance calls kaise kaam karti hain.', f'''
<h2>Namaste, main Harsh hoon</h2>
<p>Main Harsh Upadhyay hoon, <strong>Timeline by Harsh</strong> (@timelinebyharsh) ke peeche. Main Instagram par Hindu dharmik content banata hoon aur Sanatan Dharma aur roz ki zindagi par logon se baat karta hoon.</p>
<p>Log aksar ek jaisi dikkatein lekar aate hain: zyada sochna, aisa routine jo tikta nahi, ya koi bada faisla jo akele lena mushkil hai. Iske liye ek comment ya chhota message kaafi nahi hota, isiliye main one-on-one calls karta hoon.</p>

<h2>Call kya hai</h2>
<p>Google Meet par ek private baatcheet, bas aap aur main. Aap batate hain ki kahan phanse hain. Main seedhe sawaal poochkar asli dikkat dhoondta hoon. Phir hum aane wale dinon ke liye kuch saaf kadam tay karte hain. Baad mein 24 ghante ke andar main WhatsApp par likhit summary bhejta hoon.</p>
<p>Main samajhdari ki baaton, roz ki practice jaise dhyan, aur Sanatan Dharma se seekhi baaton se kaam leta hoon. Main bas motivation wali baatein nahi karta.</p>

<h2>Call kya nahi hai</h2>
<ul>
<li>Ye therapy, counselling ya medical salah nahi hai.</li>
<li>Ye legal, paison ya investment ki salah nahi hai.</li>
<li>Ye kisi nateeje ki guarantee nahi hai. Mehnat aapko karni hai, main bas saaf dekhne mein madad karta hoon.</li>
</ul>
<p>Agar aap mushkil mein hain ya safe mehsoos nahi kar rahe, toh apni local emergency service (India mein 112) ya kisi bharosemand insaan se turant sampark karein.</p>

<h2>Aapki privacy</h2>
<p>Aap jo batate hain woh sirf hamare beech rehta hai. Main sirf wahi jaankari leta hoon jo booking aur taiyaari ke liye zaroori hai. Poori jaankari <a href="privacy.html">privacy policy</a> mein hai.</p>

<h2>Baat karne ke liye taiyaar?</h2>
<p>Aap <a href="index.html#diagnostic">apne liye sahi session chun</a> sakte hain ya seedha <a href="index.html#booking">time chun</a> sakte hain. Pehle kuch poochna ho toh {CONTACT}</p>
''')

PAGES['privacy.html'] = ('Privacy Policy', f'Aakhri update: {UPD}', 'Timeline by Harsh aapki personal jaankari kaise leta hai, use karta hai aur surakshit rakhta hai.', f'''
<p class="note">Is page mein bataya gaya hai ki website use karne ya call book karne par kaun si personal jaankari li jaati hai, kyun li jaati hai, aur aapke paas kya haq hain.</p>

<h2>Zimmedaar kaun hai</h2>
<p>Timeline by Harsh, jise Harsh Upadhyay ("main") chalate hain, yahan batayi gayi personal jaankari ke liye zimmedaar hai. {CONTACT}</p>

<h2>Main kya jaankari leta hoon</h2>
<p>Jab aap priority slot book karte hain, form mein ye poocha jaata hai:</p>
<ul>
<li>Aapka naam, email aur WhatsApp number</li>
<li>Aapki umar aur city</li>
<li>Aapne kaun sa session chuna, aur pasand ki date aur time</li>
<li>Aap kis baare mein baat karna chahte hain, aur koi aur baat jo aap batana chahein</li>
<li>Agar aap UPI se payment karte hain, toh payment ka reference number (UTR) aur woh email jisse aapne book kiya</li>
<li>Agar aap early-access list join karte hain, toh aapka email, optional WhatsApp number aur woh topics jo aap chunte hain</li>
</ul>
<p>Calendar se book karne par scheduling service woh jaankari maangti hai jo use chahiye, jaise aapka naam aur email.</p>
<p>Aapki dikkat ka byora personal ho sakta hai. Kripya wahi batayein jisme aap comfortable hon.</p>
<p>Main aapke card, UPI ya bank ki detail <strong>nahi</strong> dekhta aur na rakhta hoon. Aap payment apne UPI app se seedhe karte hain, isliye main sirf wo transaction reference (UTR) dekhta hoon jo aap mujhe bhejte hain.</p>

<h2>Main iska kya karta hoon</h2>
<ul>
<li>Aapki call tay karne aur Google Meet link bhejne ke liye</li>
<li>Call ki taiyaari karne aur WhatsApp par likhit summary bhejne ke liye</li>
<li>Payment confirm karne aur booking emails bhejne ke liye</li>
<li>Aapne jo guides, calendar aur updates maange hain woh bhejne ke liye</li>
<li>Aapke sawaalon ke jawaab dene, time badalne ya refund karne ke liye, aur woh records rakhne ke liye jo kanoon maangta hai</li>
</ul>
<p>Main aapki jaankari bechta nahi hoon aur advertising ke liye use nahi karta.</p>

<h2>Aur kaun ise sambhalta hai</h2>
<p>Service chalane ke liye main in companies ki madad leta hoon. Sabki apni privacy policy hai.</p>
<ul>
<li><strong>Cal.com</strong> aur <strong>Google</strong> (Calendar, Meet aur Gmail): scheduling, video call aur booking emails.</li>
<li><strong>WhatsApp</strong>: follow-up messages aur aapki likhit summary.</li>
<li><strong>Google Fonts</strong>: is site ke fonts load karta hai, yaani aapka browser Google se judta hai.</li>
<li><strong>Amazon</strong>: kitaabon ke links affiliate links hain. Link par click karne ke baad ki baatein Amazon ki site par Amazon sambhalta hai.</li>
</ul>
<p>Agar kanoon maange toh main jaankari share kar sakta hoon.</p>

<h2>Kitne time tak rakhta hoon</h2>
<p>Booking ki jaankari main tab tak rakhta hoon jab tak service dene, aapse follow-up karne aur tax-accounting ke niyam nibhane ke liye zaroori hai. Uske baad jo hata sakta hoon, hata deta hoon.</p>

<h2>Aapke options aur haq</h2>
<p>Digital Personal Data Protection Act, 2023 ke tehat aap mujhse pooch sakte hain ki mere paas aapki kaun si jaankari hai, use theek karwa sakte hain ya hatwa sakte hain, aur apni sahmati wapas le sakte hain. Iske liye upar bataye tareeke se sampark karein. Main jald se jald jawaab doonga. Santusht na hon toh aap Data Protection Board of India mein shikayat bhi kar sakte hain.</p>

<h2>Bachche</h2>
<p>Agar aapki umar 18 saal se kam hai, toh kripya mata-pita ya guardian ki jaankari aur sahmati se hi book karein. Main umar isiliye poochta hoon.</p>

<h2>Security</h2>
<p>Ye site HTTPS par chalti hai aur payment aap apne UPI app se karte hain. Koi bhi system poori tarah surakshit nahi hota, isliye kripya booking form mein sensitive documents ya passwords na bhejein.</p>

<h2>Cookies</h2>
<p><a href="cookies.html">Cookie policy</a> dekhein.</p>

<h2>Badlaav</h2>
<p>Agar main ye policy badloonga toh upar ki date badal doonga. Bade badlaav hone par home page par bata doonga.</p>
''')

PAGES['terms.html'] = ('Terms of Use', f'Aakhri update: {UPD}', 'Timeline by Harsh website use karne aur guidance calls book karne ke niyam.', f'''
<p class="note">Call book karne ya website use karne ka matlab hai ki aap in niyamon se sahmat hain. Kuch samajh na aaye ya theek na lage toh book karne se pehle pooch lein.</p>

<h2>Service</h2>
<p>Timeline by Harsh mein Harsh Upadhyay ke saath Google Meet par private one-on-one guidance call milti hai. Abhi ye sessions hain: Clarity Call (30 minute), Dincharya Reset (45 minute) aur Deep Dive (60 minute). Keemat Indian rupees mein booking section aur checkout mein dikhti hai.</p>

<h2>Ye service kya nahi hai</h2>
<p>Ye calls samajhdari ki baaton aur Sanatan Dharma ki parampara par aadharit guidance wali baatcheet hain. Ye therapy, counselling, medical, legal, paison ya investment ki salah <strong>nahi</strong> hain, aur main kisi licensed professional ki jagah nahi le sakta. Aise maamlon mein kripya sahi professional se milein.</p>
<p>Main kisi khaas nateeje ka vaada nahi karta. Call ke baad aap kya karte hain, ye aapka faisla hai.</p>
<p>Ye emergency service nahi hai. Agar aap mushkil mein hain ya safe mehsoos nahi kar rahe, toh apni local emergency service (India mein 112) se sampark karein.</p>

<h2>Booking aur payment</h2>
<ul>
<li>Aap calendar se book karte hain. Booking ke baad aap UPI se payment karte hain aur main aapka slot confirm karta hoon.</li>
<li>Aapka slot tab pakka hota hai jab aapki booking ya payment confirm ho jaaye.</li>
<li>Calendar se ki gayi booking tab tak sirf request hoti hai jab tak main use confirm na karoon. Agar aap UPI se pay karte hain, toh payment dikhne ke baad main booking confirm karta hoon.</li>
<li>Kripya sahi jaankari dein. Mujhe aapse email ya WhatsApp par sampark karna pad sakta hai.</li>
<li>Time badalne aur refund ke niyam <a href="refund.html">refund policy</a> mein hain.</li>
</ul>

<h2>Kaun book kar sakta hai</h2>
<p>Aapki umar 18 saal ya usse zyada honi chahiye. Usse chhote hon toh kripya mata-pita ya guardian ki sahmati se hi book karein.</p>

<h2>Call par hum kaise pesh aayein</h2>
<ul>
<li>Kripya samman se baat karein. Agar call gaali-galoch ya unsafe ho jaaye toh main use khatam kar sakta hoon.</li>
<li>Kripya meri likhit ijaazat ke bina call record na karein aur uski baatein sabke saamne share na karein.</li>
<li>Aap jo batate hain main use private rakhta hoon. Sirf tab todoonga jab kanoon maange, ya jab mujhe lage ki kisi ko gambhir khatra hai.</li>
</ul>

<h2>Guides aur live sessions</h2>
<p>Guides aur live sessions seekhne ke liye hain. Tyohaaron ki tithiyan aur puja ke riwaaj kshetra aur parampara ke hisaab se alag hote hain, isliye koi bhi riwaaj apnane se pehle apne parivaar ya pandit se pooch lein. Main kisi puja, mantra ya product se dhan, vivah, safalta ya suraksha ka vaada nahi karta. Jab koi guide ya session bikri par aayega, uski keemat aur refund ke niyam pay karne se pehle dikhaye jaayenge.</p>

<h2>Kitaabein aur links</h2>
<p>Kitaabon wale section mein Amazon affiliate links hain, aur section mein ye likha hota hai. Inse kharidne par mujhe thoda commission mil sakta hai, aapko koi extra kharcha nahi. Doosri sites ke apne niyam hote hain.</p>

<h2>Mera content</h2>
<p>Is site ka text, design aur tasveerein Timeline by Harsh ki hain, jab tak kuch aur na likha ho. Kripya ijaazat ke bina copy na karein.</p>

<h2>Zimmedaari ki seema</h2>
<p>Main har call ki achhe se taiyaari karta hoon aur use poora karta hoon, lekin kanoon jitni chhoot deta hai, utna, call ya is website ke aadhar par aapke liye gaye faislon ya nuksaan ki zimmedaari meri nahi hai. Isse Indian consumer law mein aapka koi haq kam nahi hota.</p>

<h2>Kaun sa kanoon lagu hota hai</h2>
<p>Ye niyam India ke kanoon ke hisaab se hain. Koi dikkat aaye toh pehle mujhse baat karein, hum suljha lenge. Na suljhe toh India ki adaalaton ko sunwayi ka adhikaar hoga.</p>

<h2>Badlaav</h2>
<p>Main ye niyam badal sakta hoon. Upar ki date se pata chalta hai ki sabse naya version kaun sa hai. Jo booking aap pehle kar chuke hain, woh unhi niyamon se chalegi jo book karte samay the.</p>

<h2>Sampark</h2>
<p>{CONTACT}</p>
''')

PAGES['refund.html'] = ('Refunds and Rescheduling', f'Aakhri update: {UPD}', 'Timeline by Harsh ki guidance calls ke liye time badalne aur refund ke niyam.', f'''
<p class="note">Chhote mein: call se kam se kam 6 ghante pehle bata dein toh time free mein badal sakte hain. Agar main aapki call nahi kar paaya, toh poora refund milega.</p>

<h2>Time badalna</h2>
<p>Call se kam se kam <strong>6 ghante</strong> pehle WhatsApp par ya confirmation email ka reply karke bata dein, hum bina extra kharche ke doosra time tay kar lenge.</p>

<h2>Kab poora refund milta hai</h2>
<ul>
<li>Main call cancel kar doon ya aa na paaoon aur hum naya time tay na kar paayein.</li>
<li>Meri taraf ki kisi technical dikkat ki wajah se call na ho paaye.</li>
<li>Ek hi booking ke liye aapse ek se zyada baar paise kat jaayein, ya payment ho gaya par booking confirm nahi hui.</li>
</ul>

<h2>Kab refund nahi milta</h2>
<ul>
<li>Aap call par nahi aaye aur pehle bataya bhi nahi.</li>
<li>Aapne call se 6 ghante se kam pehle cancel karne ko kaha. Aise mein bhi jahan ho saka main ek baar time badalne ka mauka doonga.</li>
<li>Call ho chuki hai. Salah wapas nahi ki ja sakti, isliye poore ho chuke session ka refund nahi hota.</li>
</ul>
<p>Agar kuch gadbad hui aur upar ki koi baat fit nahi baithti, toh mujhe likhein. Main imaandaari se dekhkar case ke hisaab se faisla karoonga.</p>

<h2>Refund kaise milta hai</h2>
<p>Manzoor hua refund UPI se aapke paas wapas aata hai. Isme aam taur par 5 se 7 kaam-kaaji din lagte hain, aapke bank ya UPI app ke hisaab se.</p>

<h2>Kaise maangein</h2>
<p>{CONTACT} Kripya woh naam aur email batayein jisse book kiya tha, aur payment ID agar aapke paas ho.</p>

<p>Ye niyam <a href="terms.html">terms of use</a> ke saath chalte hain. Inse Indian consumer law mein aapka koi haq kam nahi hota.</p>
''')

PAGES['cookies.html'] = ('Cookie Policy', f'Aakhri update: {UPD}', 'Timeline by Harsh aur uske booking-payment partners kaun si cookies use karte hain.', f'''
<p class="note">Chhote mein: ye site apni koi cookie nahi lagati aur isme koi analytics ya advertising tracker nahi hai. Isme use hone wali kuch services apni cookies laga sakti hain.</p>

<h2>Cookie kya hoti hai</h2>
<p>Cookie ek chhoti file hoti hai jo website aapke browser mein save karti hai. Sites inse login ya chal rahe payment jaisi baatein yaad rakhti hain.</p>

<h2>Ye site kya karti hai</h2>
<p>Is website ki apni koi cookie nahi hai, aur ye analytics, advertising ya tracking tools use nahi karti. Ye aapke browser mein aisi koi jaankari save nahi karti jisse aapka peecha kiya ja sake.</p>

<h2>Doosri services kya kar sakti hain</h2>
<p>Page ke kuch hisse doosri companies se load hote hain. Load hone par woh apni cookies ya waisi hi storage laga sakti hain, jin par mera control nahi hai:</p>
<ul>
<li><strong>Cal.com</strong>: page par booking ka calendar.</li>
<li><strong>Google Fonts</strong>: fonts load karta hai. Iske liye aapka browser Google se judta hai.</li>
<li><strong>Amazon</strong>: sirf tab jab aap kitaab ka link kholkar is site se bahar jaayein.</li>
</ul>

<h2>Aapke options</h2>
<p>Aap apne browser ki settings mein cookies block ya delete kar sakte hain. Sab kuch block karne par booking calendar ya checkout ka kuch hissa kaam karna band kar sakta hai.</p>

<h2>Aur jaankari</h2>
<p>Aapki jaankari kaise use hoti hai, ye jaanne ke liye <a href="privacy.html">privacy policy</a> padhein. {CONTACT}</p>
''')


PAGES['collaborate.html'] = ('Collaborate', 'Timeline by Harsh ke saath collaborate karein', 'Brands, publishers aur platforms ke liye: Timeline by Harsh ke saath kaise kaam karein.', f'''
<h2>Ye page kinke liye hai</h2>
<p>Un brands, publishers aur platforms ke liye jo Hindu itihaas, mandir, rituals aur shaastra mein dilchaspi rakhne wali audience tak pahunchna chahte hain.</p>

<h2>Timeline by Harsh ke baare mein</h2>
<p>Timeline by Harsh, Harsh Upadhyay ka Hindi-first Instagram page hai. Ye Hindu itihaas, mandir, paramparayein, tyohaar aur shaastra ko aasaan kahaniyon mein samjhata hai. Audience zyada tar India mein hai.</p>

<h2>Main kinke saath kaam karta hoon</h2>
<ul>
<li>Rudraksha aur devotional product brands</li>
<li>Puja samagri banane wale</li>
<li>Kitaab publishers</li>
<li>Hindu education platforms</li>
<li>Faith-tech aur puja-booking platforms</li>
<li>Mandir aur teerth yatra service providers</li>
</ul>

<h2>Saath kaam karne ke tareeke</h2>
<ul>
<li>Dedicated Instagram Reels</li>
<li>Kisi product ke aas-paas educational content</li>
<li>Instagram Stories</li>
<li>Tyohaar campaigns</li>
<li>Lambi partnerships</li>
<li>Affiliate aur performance-based collaborations</li>
</ul>

<h2>Main kaise kaam karta hoon</h2>
<ul>
<li>Main kisi puja, mantra, ratna ya product se dhan, vivah, safalta ya suraksha ki guarantee ka vaada nahi karta.</li>
<li>Rudraksha, ratna ya spiritual product ke baare mein kuch kehne se pehle main specifications check karta hoon.</li>
<li>Sponsored aur affiliate content par saaf label hota hai, jaise Ad, Sponsored, Collaboration ya Affiliate.</li>
<li>Itihaas ke saboot, dharmik maanyata, shaastra ki vyakhya aur kshetriya riwaaj main alag-alag rakhta hoon.</li>
<li>Puja booking jaisi services ke liye main provider, ritual, keemat aur confirmation pehle verify karta hoon.</li>
</ul>

<h2>Sampark karein</h2>
<p>Instagram par {IG} ko message karein, aur batayein: aapka brand, product ya service, aap kis audience tak pahunchna chahte hain, aur aapki timeline. Reach aur audience ki details main maangne par share karta hoon.</p>
''')


PAGES.pop('about.html', None)   # the About page is built by tools/build_about.py
import re as _re
def _h2s(path):
    return _re.findall(r'<h2>(.*?)</h2>', open(path, encoding='utf-8').read(), flags=_re.S)
for fn in list(PAGES):
    title, sub, desc, body = PAGES[fn]
    en = _h2s(fn)
    hi = _re.findall(r'<h2>(.*?)</h2>', body, flags=_re.S)
    assert len(en) == len(hi), (fn, len(en), len(hi))
    it = iter(en)
    body = _re.sub(r'<h2>.*?</h2>', lambda m: '<h2>' + next(it) + '</h2>', body, flags=_re.S)
    PAGES[fn] = (title, sub, desc, body)

for fn, (title, sub, desc, body) in PAGES.items():
    open('hi/' + fn, 'w', encoding='utf-8').write(HEAD.format(title=title, sub=sub, desc=desc, body=body, fn=fn))
print('legal pages written')
