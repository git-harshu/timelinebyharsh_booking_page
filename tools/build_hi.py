#!/usr/bin/env python3
"""Builds hi/index.html (Hinglish: everyday Hindi written in English letters) from index.html.
The shlokas and the closing Hindi quote stay in Devanagari on purpose.
Run:  python3 tools/build_hi.py
Every English string must be found or the build stops, so the two versions cannot drift silently."""
import re, sys
s = open('index.html', encoding='utf-8').read()
missing = []


# Hinglish rule: only sentences are translated. Headings, eyebrows, buttons, form labels, tags and the whole
# "How a session goes" section stay in English, exactly as on the English page.
KEEP = {
 'Find your fit','How it works','Questions','Book a call','Or book a call','What is on your mind?',
 'It is rarely a lack of discipline.','At night','The loop','By Thursday','The fade','At home','The advice',
 'Clarity Finder','Which one sounds like you?','Overthinking','A routine that keeps slipping','A big decision','Someone to talk to',
 'Suggested session','₹299 · 30 minutes','What helps:','Book this session','Written summary on WhatsApp within 24 hours',
 'What changes after one honest conversation','See how a call goes','You can say the problem in one sentence.','You leave with three steps, not thirty.','You stop carrying it alone.',
 'How a session goes','Thirty minutes. Just you, me, and the one problem you cannot seem to solve.','You talk','Say it unfiltered.','I ask','Direct questions find the root.','We plan','A plan built on practical wisdom.','Next three steps','Three actions for tomorrow morning.',
 'Pick the length that fits','30 minutes · Google Meet','45 minutes · Google Meet','60 minutes · Google Meet','What is included','Book',
 'Choose a time','Live availability, booked on Google Meet','Open in new tab','About you','Your question','Which session?',
 'Clarity Call, 30 min, ₹299','Dincharya Reset, 45 min, ₹499','Deep Dive, 60 min, ₹699','General Life Guidance & Sounding Board (₹299)',
 'Preferred date','Time window','Morning (9 AM – 12 PM)','Afternoon (1 PM – 4 PM)','Evening (6 PM – 9 PM)','Night (9 PM – 11 PM)',
 'Full name','Email address','City','Age','WhatsApp number','What is the one problem you want to talk about?','Back','Continue','Pay ₹299 securely',
 'Rahul Sharma','10-digit number','A few lines is enough.','you@example.com','12 digit number',
 'Booking progress','Explore','Close','UPI QR code',
 'Common questions','Something else on your mind?','Message me on Instagram',
 'Where does the call happen?','Which session should I pick?','Why do the calls have a fee?','Can I reschedule if something comes up?','Is what I share kept private?','Is this therapy or medical advice?','How should I prepare?',
 'refund policy','privacy policy','terms',
 'Books I Recommend','Discipline','Philosophy','Grounding','Deep Work','5-Mukhi Rudraksha Mala','View on Amazon',
 'Learn the stories behind the tradition','Mandir and history','Rituals and traditions','Scriptures and philosophy','Festivals and vrat','Coming first',
 'Major festivals explained','Preparation checklists','Common puja samagri lists','Basic ritual steps','Mantra meanings and pronunciation','Regional differences, clearly marked',
 'Get early access','See the guide','Be the first to get them','What are you interested in?','Join the list','Collaborate',
 'About','Policies','Privacy','Terms','Refunds','Cookies','© 2026 Timeline by Harsh. All rights reserved.',
 'Booking requested','One last step','Pay with UPI app','Copy','Email you booked with','UTR or reference number from your UPI app','I have paid',
 "btn.disabled = false; btn.textContent = 'I have paid'","btn.textContent = 'Sending'","'Copied'",
 'Payment received','Session Confirmed','<span>Track:</span>','<span>Fee:</span>','Message on WhatsApp','Pay ₹${price} securely',
}

def node(en, hi):
    global s
    if en in KEEP: return
    s, n = re.subn(r'(>\s*)' + re.escape(en) + r'(\s*<)', lambda m: m.group(1) + hi + m.group(2), s)
    if n == 0: missing.append(('node', en))

def attr(name, en, hi):
    global s
    if en in KEEP: return
    a = f'{name}="{en}"'
    if a not in s: missing.append((name, en)); return
    s = s.replace(a, f'{name}="{hi}"')

def raw(en, hi):
    global s
    if en in KEEP: return
    if en not in s: missing.append(('raw', en)); return
    s = s.replace(en, hi)

# head / meta
node('Timeline by Harsh | Personal guidance calls', 'Timeline by Harsh | Personal guidance calls')
attr('content', 'Overthinking, a routine that will not stick, a decision you cannot make alone? Private one-on-one calls with Harsh Upadhyay to think it through.', 'Zyada sochna, aisa routine jo tikta nahi, ya aisa faisla jo akele nahi ho pa raha? Harsh Upadhyay ke saath private one-on-one call.')
attr('content', "Thirty minutes. Just you, me, and the one problem you can't seem to solve. Private one-on-one calls with Harsh (@timelinebyharsh).", '30 minute. Bas aap, main, aur woh ek dikkat jo suljh nahi rahi. Harsh (@timelinebyharsh) ke saath private call.')
attr('content', 'Private one-on-one calls with Harsh Upadhyay. Book a time that suits you.', 'Harsh Upadhyay ke saath private one-on-one call. Apne hisaab se time chunein.')

# header
node('Find your fit', 'Sahi session chunein')
node('How it works', 'Kaise kaam karta hai')
node('Questions', 'Sawaal')
node('Book a call', 'Call book karein')

# hero
node('You keep thinking about it.', 'Aap <span class="nb">baar-baar</span> sochte rehte hain.')
node('And', 'Aur')
node('nothing moves.', 'kuch aage nahi badhta.')
node('You do not need another pep talk. You need someone to think it through with.',
     'Aapko ek aur motivational speech nahi chahiye. Aapko koi chahiye jiske saath baithkar aap ise suljha sakein.')
node('What is on your mind?', 'Aapke mann mein kya hai?')
node('Or book a call', 'Ya seedha call book karein')

# understand
node('It is rarely a lack of discipline.', 'Ye aksar discipline ki kami nahi hoti.')
node('At night', 'Raat ko')
node('The loop', 'Wahi uljhan')
node('The same thought, again and again. You are tired, and still cannot say what the real problem is.', 'Wahi baat baar-baar dimaag mein ghoomti hai. Aap thak jaate hain, phir bhi samajh nahi aata ki asli dikkat kya hai.')
node('By Thursday', 'Thursday tak')
node('The fade', 'Josh thanda pad jaata hai')
node('Monday starts strong. By Thursday the plan is gone, and the guilt arrives before the weekend.', 'Monday ko shuruaat zordaar hoti hai. Thursday tak plan chhoot jaata hai, aur weekend se pehle hi guilt aa jaata hai.')
node('At home', 'Ghar par')
node('The advice', 'Sabki salah')
node('Everyone has an opinion. The people who love you also want a say in what you choose.', 'Sabke paas apni raay hai. Jo log aapse pyaar karte hain, woh bhi chahte hain ki aap wahi chunein jo woh kahein.')
node('None of this is weakness. It is a mind with nobody to think out loud with.', 'Ye kamzori nahi hai. Ye bas aisa mann hai jiske paas khulkar baat karne ke liye koi nahi hai.')

# finder
node('Clarity Finder', 'Sahi raasta')
node('Which one sounds like you?', 'Inmein se kaun sa aap jaisa lagta hai?')
node('Tap the one that feels closest. I will show you what usually helps.', 'Jo sabse kareeb lage uspar tap karein. Main bataunga ki aam taur par kya kaam aata hai.')
node('Overthinking', 'Zyada sochna')
node('Too many ideas, nothing finished.', 'Bahut saare ideas, poora kuch nahi.')
node('A routine that keeps slipping', 'Routine jo tikta nahi')
node('Fresh start Monday, lost by Thursday.', 'Monday ko nayi shuruaat, Thursday tak sab khatam.')
node('A big decision', 'Ek bada faisla')
node('A big fork and no honest view.', 'Do raaste hain, aur sachchi raay dene wala koi nahi.')
node('Someone to talk to', 'Koi jisse baat kar sakein')
node('Somewhere safe to say it out loud.', 'Ek safe jagah jahan khulkar bol sakein.')
node('₹299 · 30 minutes', '₹299 · 30 minute')
node('What helps:', 'Kya kaam aata hai:')
node('Too many options can feel like a lack of discipline, but it is mostly noise. In thirty minutes we find the one thing that matters and agree three steps for tomorrow.',
     'Bahut saare options discipline ki kami jaise lagte hain, par asal mein woh shor hote hain. 30 minute mein hum woh ek cheez dhoondte hain jo zaroori hai, aur kal ke liye teen kadam tay karte hain.')
node('Book this session', 'Ye session book karein')
node('Written summary on WhatsApp within 24 hours', '24 ghante mein WhatsApp par likhit summary')

# relief
node('What changes after one honest conversation', 'Ek sachchi baatcheet ke baad kya badalta hai')
node('I cannot promise a new life in thirty minutes. This is what we work towards.', 'Main 30 minute mein nayi zindagi ka vaada nahi kar sakta. Par hum in cheezon ki taraf kaam karte hain.')
node('See how a call goes', 'Dekhein call kaise chalti hai')
node('You can say the problem in one sentence.', 'Aap apni dikkat ek line mein bol paate hain.')
node('A lot of the heaviness comes from not knowing what the real problem is. Naming it is the first relief.', 'Bahut saara bojh isliye hota hai kyunki asli dikkat pata nahi hoti. Use naam dena pehli raahat hai.')
node('You leave with three steps, not thirty.', 'Aapke paas tees nahi, sirf teen kadam hote hain.')
node('Small enough to start tomorrow morning, and clear enough to know when you are done.', 'Itne chhote ki kal subah se shuru kar sakein, aur itne saaf ki pata chale kab poore hue.')
node('You stop carrying it alone.', 'Aap akele bojh nahi uthaate.')
node('Someone outside your situation has listened and thought it through with you.', 'Koi jo aapki situation se bahar hai, usne aapki baat suni aur aapke saath milkar socha.')

# journey
node('How a session goes', 'Session kaise chalta hai')
node('Thirty minutes. Just you, me, and the one problem you cannot seem to solve.', '30 minute. Bas aap, main, aur woh ek dikkat jo suljh nahi rahi.')
node('You talk', 'Aap bolte hain')
node('Say it unfiltered.', 'Jaisa hai waisa boliye.')
node('I ask', 'Main poochta hoon')
node('Direct questions find the root.', 'Seedhe sawaal asli jad tak pahunchate hain.')
node('We plan', 'Hum plan banate hain')
node('A plan built on practical wisdom.', 'Samajhdari wala, kaam ka plan.')
node('Next three steps', 'Agle teen kadam')
node('Three actions for tomorrow morning.', 'Kal subah ke liye teen kaam.')

# sessions
node('Pick the length that fits', 'Apne hisaab se time chunein')
node('Every call is one-on-one with me. If you are unsure, start with the Clarity Call.', 'Har call sirf mere saath, ek-ek karke hoti hai. Pakka nahi pata toh Clarity Call se shuru karein.')
node('30 minutes · Google Meet', '30 minute · Google Meet')
node('For when you feel stuck or overwhelmed. We find the real problem and leave with three rules to follow.', 'Jab aap phanse hue ya bahut pareshan mehsoos karein. Hum asli dikkat dhoondte hain aur aapke paas follow karne ke liye teen rules hote hain.')
node('What is included', 'Isme kya milta hai')
node('5 minutes of you talking, no interruptions', '5 minute aap bolte hain, beech mein koi nahi tokta')
node('10 minutes of direct questions', '10 minute seedhe sawaal')
node('15 minutes to plan tomorrow', '15 minute kal ka plan banane ke liye')
node('Book', 'Book karein')
node('45 minutes · Google Meet', '45 minute · Google Meet')
node('For rebuilding focus and calm. A realistic morning and evening routine built around your work hours and energy.', 'Focus aur shaanti wapas laane ke liye. Aapke kaam ke time aur energy ke hisaab se subah-shaam ka asli routine.')
node('A morning and evening rhythm that fits your day', 'Aapke din ke hisaab se subah-shaam ka routine')
node('A plan to cut mindless phone checking', 'Bekaar mein phone dekhna kam karne ka plan')
node('A simple dhyan practice to start with, ten minutes', 'Shuru karne ke liye 10 minute ka aasaan dhyan')
node('A daily habit tracker in Notion', 'Notion mein roz ki aadaton ka tracker')
node('60 minutes · Google Meet', '60 minute · Google Meet')
node('For bigger crossroads such as career, family expectations or a major change. We work through the assumptions and build a 90-day path.', 'Bade mod ke liye, jaise career, ghar ki ummeedein ya koi bada badlaav. Hum aapki soch ko parakhte hain aur 90 din ka raasta banate hain.')
node('A full hour, no clock watching', 'Poora ek ghanta, ghadi dekhe bina')
node('A clear look at what is blocking the decision', 'Faisla kahan atka hai, uski saaf tasveer')
node('A written 90-day plan after the call', 'Call ke baad 90 din ka likha hua plan')
node('Seven days of WhatsApp voice-note follow-up', 'Saat din WhatsApp voice note se follow-up')

# booking
node('Choose a time', 'Time chunein')
node('Pick a free slot on the calendar, or book a priority slot with payment.', 'Calendar se khaali slot chunein, ya payment karke priority slot book karein.')
node('Live availability, booked on Google Meet', 'Live availability, Google Meet par book hoga')
node('Open in new tab', 'Naye tab mein kholein')
node('Pay now to hold your time. I prepare for your question before the call.', 'Abhi payment karke apna time pakka karein. Main call se pehle aapke sawaal ki taiyaari karta hoon.')
node('About you', 'Aapke baare mein')
node('Your question', 'Aapka sawaal')
node('Which session?', 'Kaun sa session?')
node('Clarity Call, 30 min, ₹299', 'Clarity Call, 30 minute, ₹299')
node('Dincharya Reset, 45 min, ₹499', 'Dincharya Reset, 45 minute, ₹499')
node('Deep Dive, 60 min, ₹699', 'Deep Dive, 60 minute, ₹699')
node('General Life Guidance & Sounding Board (₹299)', 'General life guidance aur baat karne ki jagah (₹299)')
node('Preferred date', 'Pasand ki date')
node('Time window', 'Kaun sa time theek rahega')
node('Morning (9 AM – 12 PM)', 'Subah (9 baje – 12 baje)')
node('Afternoon (1 PM – 4 PM)', 'Dopahar (1 baje – 4 baje)')
node('Evening (6 PM – 9 PM)', 'Shaam (6 baje – 9 baje)')
node('Night (9 PM – 11 PM)', 'Raat (9 baje – 11 baje)')
node('Full name', 'Poora naam')
attr('placeholder', '10-digit number', '10 digit ka number')
node('Email address', 'Email')
node('Age', 'Umar')
attr('placeholder', 'Age', 'Umar')
node('What is the one problem you want to talk about?', 'Woh ek dikkat kya hai jiske baare mein aap baat karna chahte hain?')
attr('placeholder', 'A few lines is enough.', 'Kuch lines kaafi hain.')
node('Back', 'Peeche')
node('Continue', 'Aage badhein')
node('Pay ₹299 securely', '₹299 pay karein')
node('Secure checkout via Razorpay. UPI, Cards & Netbanking supported.', 'Razorpay se secure checkout. UPI, cards aur netbanking chalte hain.')

# faq
node('Common questions', 'Aam sawaal')
node('Something else on your mind?', 'Kuch aur poochna hai?')
node('Message me on Instagram', 'Instagram par mujhe message karein')
node('Where does the call happen?', 'Call kahan hoti hai?')
node('Privately over Google Meet. After you book, a calendar invite with your Meet link reaches your email and WhatsApp.', 'Google Meet par, bilkul private. Book karne ke baad aapke email aur WhatsApp par Meet link wala calendar invite aa jaata hai.')
node('Which session should I pick?', 'Main kaun sa session chunoon?')
node('Start with the Clarity Call. If you need more time after that, we can plan a longer session.', 'Clarity Call se shuru karein. Uske baad zaroorat ho toh hum lamba session rakh sakte hain.')
node('Why do the calls have a fee?', 'Call ki fees kyun hai?')
node('When calls were free, many people booked and did not show up, which blocked others who needed the time. A small fee keeps slots for people who will attend, and lets me prepare properly for you.', 'Jab calls free thi, toh kai log book karke aate nahi the, aur jinhe sach mein zaroorat thi unka time chala jaata tha. Chhoti si fees se slots unhi ke liye rehte hain jo aayenge, aur main aapke liye theek se taiyaari kar paata hoon.')
node('Can I reschedule if something comes up?', 'Kuch kaam aa jaaye toh kya time badal sakta hoon?')
node('Yes. Tell me at least 6 hours before, on WhatsApp or by replying to your confirmation email, and we will pick another time at no extra cost. More in the', 'Haan. Kam se kam 6 ghante pehle WhatsApp par ya confirmation email ka reply karke bata dein, hum bina extra kharche ke doosra time tay kar lenge. Aur jaankari yahan:')
node('Is what I share kept private?', 'Kya meri baat private rehti hai?')
node('Yes. What you share stays between you and me. Details are in the', 'Haan. Jo aap batate hain woh sirf aapke aur mere beech rehta hai. Poori jaankari yahan:')
node('Is this therapy or medical advice?', 'Kya ye therapy ya medical advice hai?')
node('No. These are guidance conversations, not therapy, medical, legal or financial advice. Read the', 'Nahi. Ye guidance wali baatcheet hai, therapy, medical, legal ya paison ki salah nahi. Padhein:')
node('How should I prepare?', 'Main taiyaari kaise karoon?')
node('Keep a pen and paper nearby. Write down your main problem and what you have already tried, so we can start at the root.', 'Pen aur kaagaz paas rakhein. Apni main dikkat aur ab tak jo koshish ki hai woh likh lein, taaki hum seedhe jad se shuru kar sakein.')

# books
node('Books I Recommend', 'Meri pasand ki kitaabein')
node('Books and tools I use myself. These are Amazon affiliate links: if you buy through them, I earn a small commission at no cost to you.', 'Ye kitaabein aur cheezein main khud use karta hoon. Ye Amazon affiliate links hain: inse kharidne par mujhe thoda commission milta hai, aapko koi extra kharcha nahi.')
node("James Clear's practical framework for breaking destructive loops and building steady daily momentum.", 'James Clear ka aasaan tareeka, buri aadaton ka chakra todne aur roz aage badhte rehne ke liye.')
node('Philosophy', 'Zindagi ki seekh')
node("A timeless manual on duty, detaching from outcome anxiety, and finding clarity in life's battles.", 'Kartavya, nateeje ki chinta chhodne aur zindagi ki ladaiyon mein saaf soch paane ki sadabahaar kitaab.')
node('Grounding', 'Mann ki shaanti')
node('5-Mukhi Rudraksha Mala', '5 Mukhi Rudraksha Mala')
node('108+1 certified beads used for daily mantra dhyan and emotional centering during busy workdays.', '108+1 certified daane, roz mantra jaap aur dhyan ke liye, aur busy din mein mann ko sthir rakhne ke liye.')
node('A mechanical timer to replace phone timers, eliminating notifications during 30-minute focus blocks.', 'Phone ke timer ki jagah mechanical timer, taaki 30 minute ke focus mein notifications na aayein.')
node('View on Amazon', 'Amazon par dekhein')

# footer
node('Private one-on-one calls for overthinking, daily routine and big life decisions.', 'Zyada sochne, roz ke routine aur bade faislon ke liye private one-on-one calls.')
attr('aria-label', 'Explore', 'Dekhein')
node('Explore', 'Dekhein')
node('About', 'Parichay')
node('© 2026 Timeline by Harsh. All rights reserved.', '© 2026 Timeline by Harsh. Sabhi adhikaar surakshit.')
node('Guidance calls are not therapy, medical, legal or financial advice. Book links are Amazon affiliate links.', 'Guidance calls therapy, medical, legal ya paison ki salah nahi hain. Kitaabon ke links Amazon affiliate links hain.')

# payment popup
attr('aria-label', 'Close', 'Band karein')
node('Booking requested', 'Booking request mil gayi')
node('One last step', 'Bas ek aakhri kadam')
node('Pay to confirm your slot. I confirm the booking once I see the payment.', 'Apna slot pakka karne ke liye payment karein. Payment dikhte hi main booking confirm kar doonga.')
node('Pay with UPI app', 'UPI app se pay karein')
node('Email you booked with', 'Jis email se book kiya')
attr('placeholder', 'you@example.com', 'aap@example.com')
node('UTR or reference number from your UPI app', 'UPI app mein dikhne wala UTR ya reference number')
attr('placeholder', '12 digit number', '12 digit ka number')
node('I have paid', 'Maine pay kar diya')
node('Thank you. I will check the payment and confirm your booking. Cal.com will email you the Meet link once it is confirmed.', 'Dhanyavaad. Main payment dekhkar aapki booking confirm karoonga. Confirm hote hi Cal.com aapko Meet link email kar dega.')


# ---------- guides, puja preparation, early-access list ----------
node('Learn the stories behind the tradition', 'Parampara ke peeche ki kahaniyan seekhein')
node('Hindu history, temples, rituals and scriptures, told in simple Hindi on Instagram. Here is what I share, and what I am building next.', 'Hindu itihaas, mandir, rituals aur shaastra, Instagram par aasaan Hindi mein. Yahan dekhein main kya share karta hoon, aur aage kya bana raha hoon.')
node('Mandir and history', 'Mandir aur itihaas')
node('The stories and heritage behind our temples.', 'Hamare mandiron ke peeche ki kahaniyan aur virasat.')
node('Rituals and traditions', 'Rituals aur parampara')
node('Why, how and when rituals are done.', 'Rituals kyun, kaise aur kab kiye jaate hain.')
node('Scriptures and philosophy', 'Shaastra aur darshan')
node('The Gita, Ramayana and Mahabharata, simply explained.', 'Gita, Ramayan aur Mahabharat, aasaan shabdon mein.')
node('Festivals and vrat', 'Tyohaar aur vrat')
node('Preparation and meaning, in plain words.', 'Taiyaari aur matlab, saaf shabdon mein.')
node('Coming first', 'Sabse pehle aa raha hai')
node('One guide for the festivals and vrats you observe: what each one means, how to prepare, and what you will need.', 'Aapke tyohaaron aur vraton ke liye ek guide: har ek ka matlab, taiyaari kaise karein, aur kya-kya chahiye.')
node('Major festivals explained', 'Bade tyohaaron ki jaankari')
node('Preparation checklists', 'Taiyaari ki checklist')
node('Common puja samagri lists', 'Puja samagri ki aam list')
node('Basic ritual steps', 'Rituals ke basic steps')
node('Mantra meanings and pronunciation', 'Mantra ka matlab aur uchcharan')
node('Regional differences, clearly marked', 'Kshetra ke hisaab se farq, saaf likha hua')
node('Dates and practices differ by region and tradition. I mark where they do and name my sources.', 'Tithiyan aur riwaaj kshetra aur parampara ke hisaab se alag hote hain. Jahan farq hai main likh deta hoon aur apne sources ka naam bhi.')
node('Get early access', 'Pehle access paayein')
node('Be the first to get them', 'Sabse pehle paayein')
node('Join the early-access list. You will get the free Hindu Festival and Vrat Calendar when it is ready, and first access to guides and live sessions.', 'Early-access list join karein. Free Hindu Festival and Vrat Calendar tayyar hote hi aapko milega, aur guides aur live sessions ka pehle access bhi.')
node('What are you interested in?', 'Aapko kis mein dilchaspi hai?')
node('Festival and vrat guide', 'Festival aur vrat guide')
node('I agree to receive messages about these resources. I can stop anytime.', 'Mujhe in resources ke baare mein messages bhejna theek hai. Kabhi bhi band karwa sakte hain.')
node('Join the list', 'List join karein')
node('Collaborate', 'Saath kaam karein')
node('See the guide', 'Guide dekhein')

# JS strings
J = [
 ('Please enter a valid 10-digit WhatsApp number, or leave it empty.', 'Kripya 10 digit ka sahi WhatsApp number likhein, ya khaali chhod dein.'),
 ('Please tick the box to agree.', 'Kripya sahmati ka box tick karein.'),
 ("say('Sending...', '')", "say('Bhej rahe hain...', '')"),
 ('Thank you. You are on the list. I will write when the first guide is ready.', 'Dhanyavaad. Aap list mein hain. Pehli guide tayyar hote hi main likhunga.'),
 ('price: "₹299 · 30 minutes"', 'price: "₹299 · 30 minute"'),
 ('price: "₹499 · 45 minutes"', 'price: "₹499 · 45 minute"'),
 ('price: "₹699 · 60 minutes"', 'price: "₹699 · 60 minute"'),
 ('<b>What helps:</b> Too many options can feel like a lack of discipline, but it is mostly noise. In thirty minutes we find the one thing that matters and agree three steps for tomorrow.', '<b>What helps:</b> Bahut saare options discipline ki kami jaise lagte hain, par asal mein woh shor hote hain. 30 minute mein hum woh ek cheez dhoondte hain jo zaroori hai, aur kal ke liye teen kadam tay karte hain.'),
 ('<b>What helps:</b> A routine borrowed from someone else rarely lasts. We build a simple morning and evening rhythm around your real work hours, one you can keep on a bad day too.', '<b>What helps:</b> Kisi aur se udhaar liya routine kam hi tikta hai. Hum aapke asli kaam ke time ke hisaab se subah-shaam ka aasaan routine banate hain, jo kharab din mein bhi chal sake.'),
 ('<b>What helps:</b> Family and friends give kind advice. You may need an outside view, free of emotional bias, to weigh your options and choose with a calm mind.', '<b>What helps:</b> Ghar waale aur dost pyaar se salah dete hain. Aapko shayad ek bahar ki nazar chahiye, jo bina kisi bhavna ke aapke options tole aur aap shaant mann se chun sakein.'),
 ('<b>What helps:</b> Often you already know the answer, but the noise around you is louder. This is a quiet, judgment-free space to say it out loud.', '<b>What helps:</b> Aksar jawaab aapko pehle se pata hota hai, bas aaspaas ka shor zyada hota hai. Ye ek shaant jagah hai jahan koi judge nahi karega, aap khulkar bol sakte hain.'),
 ('Please enter your full name.', 'Kripya apna poora naam likhein.'),
 ('Please enter a valid email address.', 'Kripya sahi email likhein.'),
 ('Please enter a valid 10-digit Indian WhatsApp number.', 'Kripya 10 digit ka sahi WhatsApp number likhein.'),
 ('Please describe your question or issue in a few words.', 'Kripya apna sawaal ya dikkat kuch shabdon mein likhein.'),
 ('Initializing priority slot checkout...', 'Checkout khul raha hai...'),
 ('Failed to initialize order', 'Order shuru nahi ho paya'),
 ('Verifying payment...', 'Payment check ho raha hai...'),
 ('Payment was cancelled or failed. Please try again.', 'Payment cancel ya fail ho gaya. Kripya dobara koshish karein.'),
 ('Razorpay is in test mode. Feel free to pick a time directly on Cal.com!', 'Razorpay abhi test mode mein hai. Aap seedhe Cal.com par bhi time chun sakte hain!'),
 ('Please choose a date.', 'Kripya date chunein.'),
 ('Please enter your city.', 'Kripya apni city likhein.'),
 ('Please enter your age (15 to 85).', 'Kripya apni umar likhein (15 se 85).'),
 ('Thank you. Your booking is requested. I will confirm it by email shortly.', 'Dhanyavaad. Aapki booking ki request mil gayi hai. Main jaldi hi email se confirm karoonga.'),
 ('Please enter the email you booked with.', 'Kripya woh email likhein jisse book kiya tha.'),
 ('Please enter the UTR or reference number from your UPI app.', 'Kripya UPI app wala UTR ya reference number likhein.'),
 ('Something went wrong.', 'Kuch gadbad ho gayi.'),
 ('Thank you. I will check the payment and confirm your booking. Cal.com will email you the Meet link once it is confirmed.', 'Dhanyavaad. Main payment dekhkar aapki booking confirm karoonga. Confirm hote hi Cal.com aapko Meet link email kar dega.'),
 ("btn.disabled = false; btn.textContent = 'I have paid'", "btn.disabled = false; btn.textContent = 'Maine pay kar diya'"),
 ("btn.textContent = 'Sending'", "btn.textContent = 'Bhej rahe hain'"),
 ("'Copied'", "'Copy ho gaya'"),
 ('Payment received', 'Payment mil gaya'),
 ('Session Confirmed', 'Session confirm ho gaya'),
 ('Thank you, <b>${escapeHtml(formData.name)}</b>. Your booking is confirmed. I will reach out on your WhatsApp within 24 hours.', 'Dhanyavaad, <b>${escapeHtml(formData.name)}</b>. Aapki booking confirm ho gayi hai. Main 24 ghante mein aapke WhatsApp par sampark karoonga.'),
 ('<span>Track:</span>', '<span>Session:</span>'),
 ('<span>Fee:</span>', '<span>Fees:</span>'),
 ("'Hi Harsh, I just booked my session for '", "'Namaste Harsh, maine abhi ye session book kiya hai: '"),
 ('Message on WhatsApp', 'WhatsApp par message karein'),
 ('Pay ₹${price} securely', '₹${price} pay karein'),
]
# the finder label inside JS was already changed by the node() pass above, so match the changed prefix
for en, hi in J: raw(en, hi)

# closing quote in Roman letters on this version (the shlokas in the strip stay Devanagari)
node('“परंपरा कोई बंधन नहीं, यह याद है उस रास्ते की, जहाँ से हम आए थे।”', '“Parampara koi bandhan nahi, yeh yaad hai us raaste ki, jahan se hum aaye the.”')
node('~ हर्ष उपाध्याय', '~ Harsh Upadhyay')

# page shell
raw('<html lang="en">', '<html lang="hi-Latn">')
s = s.replace('src="assets/', 'src="../assets/').replace('href="assets/', 'href="../assets/').replace('content="assets/', 'content="../assets/')
raw('<a class="lang-switch" href="hi/index.html" hreflang="hi" lang="hi" title="Hinglish" aria-label="Switch to Hinglish">HI</a>', '<a class="lang-switch" href="../index.html" hreflang="en" lang="en" title="English" aria-label="Switch to English">EN</a>')
raw('<link rel="alternate" hreflang="hi" href="hi/index.html">', '<link rel="alternate" hreflang="en" href="../index.html">')
s = s.replace('.footer-col h4', '.footer-col h4', 1)

if missing:
    print('MISSING (not found in index.html):')
    for m in missing: print('  ', m)
    sys.exit(1)
open('hi/index.html', 'w', encoding='utf-8').write(s)
print('hi/index.html written,', len(s), 'bytes')
