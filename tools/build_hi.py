#!/usr/bin/env python3
"""Builds hi/index.html (simple everyday Hindi, Devanagari with common English words) from index.html.
Run:  python3 tools/build_hi.py
Every English string must be found or the build stops, so the two versions cannot drift silently."""
import re, sys
src = open('index.html', encoding='utf-8').read()
s = src
missing = []

def node(en, hi):
    global s
    pat = re.compile(r'(>\s*)' + re.escape(en) + r'(\s*<)')
    s, n = pat.subn(lambda m: m.group(1) + hi + m.group(2), s)
    if n == 0: missing.append(('node', en))

def attr(name, en, hi):
    global s
    a = f'{name}="{en}"'
    if a not in s: missing.append((name, en)); return
    s = s.replace(a, f'{name}="{hi}"')

def raw(en, hi):
    global s
    if en not in s: missing.append(('raw', en)); return
    s = s.replace(en, hi)

# ---------- head / meta ----------
node('Timeline by Harsh | Personal guidance calls', 'Timeline by Harsh | पर्सनल गाइडेंस कॉल')
attr('content', 'Overthinking, a routine that will not stick, a decision you cannot make alone? Private one-on-one calls with Harsh Upadhyay to think it through.', 'ज़्यादा सोचना, ऐसा रूटीन जो टिकता नहीं, या ऐसा फैसला जो अकेले नहीं हो पा रहा? हर्ष उपाध्याय के साथ प्राइवेट वन-ऑन-वन कॉल।')
attr('content', 'Timeline by Harsh | Personal guidance calls', 'Timeline by Harsh | पर्सनल गाइडेंस कॉल')
attr('content', "Thirty minutes. Just you, me, and the one problem you can't seem to solve. Private one-on-one calls with Harsh (@timelinebyharsh).", '30 मिनट। बस आप, मैं, और वो एक दिक्कत जो सुलझ नहीं रही। हर्ष (@timelinebyharsh) के साथ प्राइवेट कॉल।')
attr('content', 'Private one-on-one calls with Harsh Upadhyay. Book a time that suits you.', 'हर्ष उपाध्याय के साथ प्राइवेट वन-ऑन-वन कॉल। अपने हिसाब से समय चुनें।')

# ---------- header ----------
node('Find your fit', 'सही सेशन चुनें')
node('How it works', 'कैसे काम करता है')
node('Sessions', 'सेशन')
node('Questions', 'सवाल')
node('Book a call', 'कॉल बुक करें')

# ---------- hero ----------
node('You keep thinking about it. And', 'आप बार-बार सोचते रहते हैं। और')
node('nothing moves.', 'कुछ आगे नहीं बढ़ता।')
node('Overthinking at night, a routine that fades by Thursday, a decision everyone has an opinion on. You do not need another pep talk. You need someone to think it through with.',
     'रात को ज़्यादा सोचना, ऐसा रूटीन जो गुरुवार तक टूट जाता है, ऐसा फैसला जिस पर सबकी अपनी राय है। आपको एक और भाषण नहीं चाहिए। आपको कोई चाहिए जिसके साथ बैठकर आप इसे सुलझा सकें।')
node('What is on your mind?', 'आपके मन में क्या चल रहा है?')
node('Or book a call', 'या सीधे कॉल बुक करें')

# ---------- understand ----------
node('It is rarely a lack of discipline.', 'ये अक्सर अनुशासन की कमी नहीं होती।')
node('At night', 'रात को')
node('The loop', 'वही उलझन')
node('The same thought, again and again. You are tired, and still cannot say what the real problem is.', 'वही बात बार-बार दिमाग में घूमती है। आप थक जाते हैं, फिर भी समझ नहीं आता कि असली दिक्कत क्या है।')
node('By Thursday', 'गुरुवार तक')
node('The fade', 'जोश ठंडा पड़ जाता है')
node('Monday starts strong. By Thursday the plan is gone, and the guilt arrives before the weekend.', 'सोमवार को शुरुआत ज़ोरदार होती है। गुरुवार तक प्लान छूट जाता है, और वीकेंड से पहले ही गिल्ट आ जाता है।')
node('At home', 'घर पर')
node('The advice', 'सबकी सलाह')
node('Everyone has an opinion. The people who love you also want a say in what you choose.', 'सबके पास अपनी राय है। जो लोग आपसे प्यार करते हैं, वो भी चाहते हैं कि आप वही चुनें जो वो कहें।')
node('None of this is weakness. It is a mind with nobody to think out loud with.', 'ये कमज़ोरी नहीं है। ये बस ऐसा मन है जिसके पास खुलकर बात करने के लिए कोई नहीं है।')

# ---------- finder ----------
node('Clarity Finder', 'सही रास्ता')
node('Which one sounds like you?', 'इनमें से कौन सा आप जैसा लगता है?')
node('Tap the one that feels closest. I will show you what usually helps.', 'जो सबसे करीब लगे उस पर टैप करें। मैं बताऊँगा कि आमतौर पर क्या काम आता है।')
node('Overthinking', 'ज़्यादा सोचना')
node('Too many ideas, nothing finished.', 'बहुत सारे आइडिया, पूरा कुछ नहीं।')
node('A routine that keeps slipping', 'रूटीन जो टिकता नहीं')
node('Fresh start Monday, lost by Thursday.', 'सोमवार को नई शुरुआत, गुरुवार तक सब खत्म।')
node('A big decision', 'एक बड़ा फैसला')
node('A big fork and no honest view.', 'दो रास्ते हैं, और सच्ची राय देने वाला कोई नहीं।')
node('Someone to talk to', 'कोई जिससे बात कर सकें')
node('Somewhere safe to say it out loud.', 'एक सुरक्षित जगह जहाँ खुलकर बोल सकें।')
node('Clarity Call', 'क्लैरिटी कॉल')
node('Suggested session', 'सुझाया गया सेशन')
node('₹299 · 30 minutes', '₹299 · 30 मिनट')
node('What helps:', 'क्या काम आता है:')
node('Too many options can feel like a lack of discipline, but it is mostly noise. In thirty minutes we find the one thing that matters and agree three steps for tomorrow.',
     'बहुत सारे ऑप्शन अनुशासन की कमी जैसे लगते हैं, पर असल में वो शोर होते हैं। 30 मिनट में हम वो एक चीज़ ढूँढते हैं जो ज़रूरी है, और कल के लिए तीन कदम तय करते हैं।')
node('Book this session', 'यह सेशन बुक करें')
node('Written summary on WhatsApp within 24 hours', '24 घंटे में WhatsApp पर लिखित समरी')

# ---------- relief ----------
node('What changes after one honest conversation', 'एक सच्ची बातचीत के बाद क्या बदलता है')
node('I cannot promise a new life in thirty minutes. This is what we work towards.', 'मैं 30 मिनट में नई ज़िंदगी का वादा नहीं कर सकता। पर हम इन चीज़ों की तरफ काम करते हैं।')
node('See how a call goes', 'देखें कॉल कैसे चलती है')
node('You can say the problem in one sentence.', 'आप अपनी दिक्कत एक वाक्य में बोल पाते हैं।')
node('A lot of the heaviness comes from not knowing what the real problem is. Naming it is the first relief.', 'बहुत सारा बोझ इसलिए होता है क्योंकि असली दिक्कत पता नहीं होती। उसे नाम देना पहली राहत है।')
node('You leave with three steps, not thirty.', 'आपके पास तीस नहीं, सिर्फ़ तीन कदम होते हैं।')
node('Small enough to start tomorrow morning, and clear enough to know when you are done.', 'इतने छोटे कि कल सुबह से शुरू कर सकें, और इतने साफ़ कि पता चले कब पूरे हुए।')
node('You stop carrying it alone.', 'आप अकेले बोझ नहीं उठाते।')
node('Someone outside your situation has listened and thought it through with you.', 'कोई ऐसा जो आपकी हालत से बाहर है, उसने आपकी बात सुनी और आपके साथ मिलकर सोचा।')

# ---------- journey ----------
node('How a session goes', 'सेशन कैसे चलता है')
node('Thirty minutes. Just you, me, and the one problem you cannot seem to solve.', '30 मिनट। बस आप, मैं, और वो एक दिक्कत जो सुलझ नहीं रही।')
node('You talk', 'आप बोलते हैं')
node('Say it unfiltered.', 'जैसा है वैसा बोलिए।')
node('I ask', 'मैं पूछता हूँ')
node('Direct questions find the root.', 'सीधे सवाल असली जड़ तक पहुँचाते हैं।')
node('We plan', 'हम प्लान बनाते हैं')
node('A plan built on practical wisdom.', 'समझदारी वाला, काम का प्लान।')
node('Next three steps', 'अगले तीन कदम')
node('Three actions for tomorrow morning.', 'कल सुबह के लिए तीन काम।')

# ---------- sessions ----------
node('Pick the length that fits', 'अपने हिसाब से समय चुनें')
node('Every call is one-on-one with me. If you are unsure, start with the Clarity Call.', 'हर कॉल सिर्फ़ मेरे साथ, एक-एक करके होती है। पक्का नहीं पता तो क्लैरिटी कॉल से शुरू करें।')
node('30 minutes · Google Meet', '30 मिनट · Google Meet')
node('For when you feel stuck or overwhelmed. We find the real problem and leave with three rules to follow.', 'जब आप फँसा हुआ या बहुत परेशान महसूस करें। हम असली दिक्कत ढूँढते हैं और आपके पास फॉलो करने के लिए तीन नियम होते हैं।')
node('What is included', 'इसमें क्या मिलता है')
node('5 minutes of you talking, no interruptions', '5 मिनट आप बोलते हैं, बीच में कोई नहीं टोकता')
node('10 minutes of direct questions', '10 मिनट सीधे सवाल')
node('15 minutes to plan tomorrow', '15 मिनट कल का प्लान बनाने के लिए')
node('Book', 'बुक करें')
node('Dincharya Reset', 'दिनचर्या रीसेट')
node('45 minutes · Google Meet', '45 मिनट · Google Meet')
node('For rebuilding focus and calm. A realistic morning and evening routine built around your work hours and energy.', 'फोकस और शांति वापस लाने के लिए। आपके काम के समय और एनर्जी के हिसाब से सुबह-शाम का असली रूटीन।')
node('A morning and evening rhythm that fits your day', 'आपके दिन के हिसाब से सुबह-शाम का रूटीन')
node('A plan to cut mindless phone checking', 'बेकार में फोन देखना कम करने का प्लान')
node('A simple dhyan practice to start with, ten minutes', 'शुरू करने के लिए 10 मिनट का आसान ध्यान')
node('A daily habit tracker in Notion', 'Notion में रोज़ की आदतों का ट्रैकर')
node('Deep Dive', 'डीप डाइव')
node('60 minutes · Google Meet', '60 मिनट · Google Meet')
node('For bigger crossroads such as career, family expectations or a major change. We work through the assumptions and build a 90-day path.', 'बड़े मोड़ के लिए, जैसे करियर, घर की उम्मीदें या कोई बड़ा बदलाव। हम आपकी सोच को परखते हैं और 90 दिन का रास्ता बनाते हैं।')
node('A full hour, no clock watching', 'पूरा एक घंटा, घड़ी देखे बिना')
node('A clear look at what is blocking the decision', 'फैसला कहाँ अटका है, उसकी साफ़ तस्वीर')
node('A written 90-day plan after the call', 'कॉल के बाद 90 दिन का लिखा हुआ प्लान')
node('Seven days of WhatsApp voice-note follow-up', 'सात दिन WhatsApp वॉइस नोट से फॉलो-अप')

# ---------- booking ----------
node('Choose a time', 'समय चुनें')
node('Pick a free slot on the calendar, or book a priority slot with payment.', 'कैलेंडर से खाली स्लॉट चुनें, या पेमेंट करके प्रायोरिटी स्लॉट बुक करें।')
node('Calendar', 'कैलेंडर')
node('Priority slot', 'प्रायोरिटी स्लॉट')
node('Live availability, booked on Google Meet', 'लाइव उपलब्धता, Google Meet पर बुक होगा')
node('Open in new tab', 'नए टैब में खोलें')
node('Pay now to hold your time. I prepare for your question before the call.', 'अभी पेमेंट करके अपना समय पक्का करें। मैं कॉल से पहले आपके सवाल की तैयारी करता हूँ।')
attr('aria-label', 'Booking progress', 'बुकिंग प्रगति')
node('Session', 'सेशन')
node('About you', 'आपके बारे में')
node('Your question', 'आपका सवाल')
node('Which session?', 'कौन सा सेशन?')
node('Clarity Call, 30 min, ₹299', 'क्लैरिटी कॉल, 30 मिनट, ₹299')
node('Dincharya Reset, 45 min, ₹499', 'दिनचर्या रीसेट, 45 मिनट, ₹499')
node('Deep Dive, 60 min, ₹699', 'डीप डाइव, 60 मिनट, ₹699')
node('General Life Guidance & Sounding Board (₹299)', 'आम लाइफ गाइडेंस और बात करने की जगह (₹299)')
node('Preferred date', 'पसंद की तारीख')
node('Time window', 'कौन सा समय ठीक रहेगा')
node('Morning (9 AM – 12 PM)', 'सुबह (9 बजे – 12 बजे)')
node('Afternoon (1 PM – 4 PM)', 'दोपहर (1 बजे – 4 बजे)')
node('Evening (6 PM – 9 PM)', 'शाम (6 बजे – 9 बजे)')
node('Night (9 PM – 11 PM)', 'रात (9 बजे – 11 बजे)')
node('Full name', 'पूरा नाम')
attr('placeholder', 'Rahul Sharma', 'राहुल शर्मा')
node('WhatsApp number', 'WhatsApp नंबर')
attr('placeholder', '10-digit number', '10 अंकों का नंबर')
node('Email address', 'ईमेल')
node('City', 'शहर')
attr('placeholder', 'City', 'शहर')
node('Age', 'उम्र')
attr('placeholder', 'Age', 'उम्र')
node('What is the one problem you want to talk about?', 'वो एक दिक्कत क्या है जिस पर आप बात करना चाहते हैं?')
attr('placeholder', 'A few lines is enough.', 'कुछ लाइनें काफ़ी हैं।')
node('Back', 'पीछे')
node('Continue', 'आगे बढ़ें')
node('Pay ₹299 securely', '₹299 पे करें')
node('Secure checkout via Razorpay. UPI, Cards & Netbanking supported.', 'Razorpay से सुरक्षित चेकआउट। UPI, कार्ड और नेटबैंकिंग चलते हैं।')

# ---------- faq ----------
node('Common questions', 'आम सवाल')
node('Something else on your mind?', 'कुछ और पूछना है?')
node('Message me on Instagram', 'Instagram पर मुझे मैसेज करें')
node('Where does the call happen?', 'कॉल कहाँ होती है?')
node('Privately over Google Meet. After you book, a calendar invite with your Meet link reaches your email and WhatsApp.', 'Google Meet पर, पूरी तरह प्राइवेट। बुक करने के बाद आपके ईमेल और WhatsApp पर Meet लिंक वाला कैलेंडर इनवाइट आ जाता है।')
node('Which session should I pick?', 'मैं कौन सा सेशन चुनूँ?')
node('Start with the Clarity Call. If you need more time after that, we can plan a longer session.', 'क्लैरिटी कॉल से शुरू करें। उसके बाद ज़रूरत हो तो हम लंबा सेशन रख सकते हैं।')
node('Why do the calls have a fee?', 'कॉल की फीस क्यों है?')
node('When calls were free, many people booked and did not show up, which blocked others who needed the time. A small fee keeps slots for people who will attend, and lets me prepare properly for you.', 'जब कॉल फ्री थीं, तो कई लोग बुक करके आते नहीं थे, और जिन्हें सच में ज़रूरत थी उनका समय चला जाता था। छोटी फीस से स्लॉट उन्हीं के लिए रहते हैं जो आएँगे, और मैं आपके लिए ठीक से तैयारी कर पाता हूँ।')
node('Can I reschedule if something comes up?', 'कुछ काम आ जाए तो क्या समय बदल सकता हूँ?')
node('Yes. Tell me at least 6 hours before, on WhatsApp or by replying to your confirmation email, and we will pick another time at no extra cost. More in the', 'हाँ। कम से कम 6 घंटे पहले WhatsApp पर या कन्फर्मेशन ईमेल का जवाब देकर बता दें, हम बिना किसी एक्स्ट्रा खर्च के दूसरा समय तय कर लेंगे। और जानकारी यहाँ:')
node('refund policy', 'रिफंड पॉलिसी')
node('Is what I share kept private?', 'क्या मेरी बात प्राइवेट रहती है?')
node('Yes. What you share stays between you and me. Details are in the', 'हाँ। जो आप बताते हैं वो सिर्फ़ आपके और मेरे बीच रहता है। पूरी जानकारी यहाँ:')
node('privacy policy', 'प्राइवेसी पॉलिसी')
node('Is this therapy or medical advice?', 'क्या ये थेरेपी या मेडिकल सलाह है?')
node('No. These are guidance conversations, not therapy, medical, legal or financial advice. Read the', 'नहीं। ये गाइडेंस वाली बातचीत है, थेरेपी, मेडिकल, कानूनी या पैसों की सलाह नहीं। पढ़ें:')
node('terms', 'नियम और शर्तें')
node('How should I prepare?', 'मैं कैसे तैयारी करूँ?')
node('Keep a pen and paper nearby. Write down your main problem and what you have already tried, so we can start at the root.', 'पेन और कागज़ पास रखें। अपनी मुख्य दिक्कत और अब तक जो कोशिश की है वो लिख लें, ताकि हम सीधे जड़ से शुरू कर सकें।')

# ---------- books ----------
node('Books I Recommend', 'मेरी पसंद की किताबें')
node('Books and tools I use myself. These are Amazon affiliate links: if you buy through them, I earn a small commission at no cost to you.', 'ये किताबें और चीज़ें मैं खुद इस्तेमाल करता हूँ। ये Amazon अफिलिएट लिंक हैं: इनसे खरीदने पर मुझे थोड़ा कमीशन मिलता है, आपको कोई एक्स्ट्रा खर्च नहीं।')
node('Discipline', 'अनुशासन')
node("James Clear's practical framework for breaking destructive loops and building steady daily momentum.", 'जेम्स क्लियर का आसान तरीका, बुरी आदतों का चक्र तोड़ने और रोज़ आगे बढ़ते रहने के लिए।')
node('Philosophy', 'ज़िंदगी की सीख')
node("A timeless manual on duty, detaching from outcome anxiety, and finding clarity in life's battles.", 'कर्तव्य, नतीजे की चिंता छोड़ने और ज़िंदगी की लड़ाइयों में साफ़ सोच पाने की सदाबहार किताब।')
node('Grounding', 'मन की शांति')
node('5-Mukhi Rudraksha Mala', '5 मुखी रुद्राक्ष माला')
node('108+1 certified beads used for daily mantra dhyan and emotional centering during busy workdays.', '108+1 प्रमाणित दाने, रोज़ मंत्र जाप और ध्यान के लिए, और व्यस्त दिन में मन को स्थिर रखने के लिए।')
node('Deep Work', 'गहरा फोकस')
node('A mechanical timer to replace phone timers, eliminating notifications during 30-minute focus blocks.', 'फोन के टाइमर की जगह मैकेनिकल टाइमर, ताकि 30 मिनट के फोकस में नोटिफिकेशन न आएँ।')
node('View on Amazon', 'Amazon पर देखें')

# ---------- footer ----------
node('Private one-on-one calls for overthinking, daily routine and big life decisions.', 'ज़्यादा सोचने, रोज़ के रूटीन और बड़े फैसलों के लिए प्राइवेट वन-ऑन-वन कॉल।')
attr('aria-label', 'Explore', 'देखें')
node('Explore', 'देखें')
node('About', 'परिचय')
attr('aria-label', 'Sessions', 'सेशन')
attr('aria-label', 'Policies', 'पॉलिसी')
node('Policies', 'पॉलिसी')
node('Privacy', 'प्राइवेसी')
node('Terms', 'नियम')
node('Refunds', 'रिफंड')
node('Cookies', 'कुकीज़')
node('© 2026 Timeline by Harsh. All rights reserved.', '© 2026 Timeline by Harsh. सर्वाधिकार सुरक्षित।')
node('Guidance calls are not therapy, medical, legal or financial advice. Book links are Amazon affiliate links.', 'गाइडेंस कॉल थेरेपी, मेडिकल, कानूनी या पैसों की सलाह नहीं हैं। किताबों के लिंक Amazon अफिलिएट लिंक हैं।')

# ---------- payment popup ----------
attr('aria-label', 'Close', 'बंद करें')
node('Booking requested', 'बुकिंग की रिक्वेस्ट मिली')
node('One last step', 'बस एक आखिरी कदम')
node('Pay to confirm your slot. I confirm the booking once I see the payment.', 'अपना स्लॉट पक्का करने के लिए पेमेंट करें। पेमेंट दिखते ही मैं बुकिंग कन्फर्म कर दूँगा।')
attr('aria-label', 'UPI QR code', 'UPI QR कोड')
node('Pay with UPI app', 'UPI ऐप से पे करें')
node('Copy', 'कॉपी')
node('Email you booked with', 'जिस ईमेल से बुक किया')
attr('placeholder', 'you@example.com', 'aap@example.com')
node('UTR or reference number from your UPI app', 'UPI ऐप में दिखने वाला UTR या रेफरेंस नंबर')
attr('placeholder', '12 digit number', '12 अंकों का नंबर')
node('I have paid', 'मैंने पे कर दिया')
node('Thank you. I will check the payment and confirm your booking. Cal.com will email you the Meet link once it is confirmed.', 'धन्यवाद। मैं पेमेंट देखकर आपकी बुकिंग कन्फर्म करूँगा। कन्फर्म होते ही Cal.com आपको Meet लिंक ईमेल कर देगा।')

# ---------- JS strings ----------
J = [
 ('title: "Clarity Call"', 'title: "क्लैरिटी कॉल"'),
 ('title: "Dincharya Reset"', 'title: "दिनचर्या रीसेट"'),
 ('title: "Deep Dive"', 'title: "डीप डाइव"'),
 ('price: "₹299 · 30 minutes"', 'price: "₹299 · 30 मिनट"'),
 ('price: "₹499 · 45 minutes"', 'price: "₹499 · 45 मिनट"'),
 ('price: "₹699 · 60 minutes"', 'price: "₹699 · 60 मिनट"'),
 ('<b>क्या काम आता है:</b> Too many options can feel like a lack of discipline, but it is mostly noise. In thirty minutes we find the one thing that matters and agree three steps for tomorrow.', '<b>क्या काम आता है:</b> बहुत सारे ऑप्शन अनुशासन की कमी जैसे लगते हैं, पर असल में वो शोर होते हैं। 30 मिनट में हम वो एक चीज़ ढूँढते हैं जो ज़रूरी है, और कल के लिए तीन कदम तय करते हैं।'),
 ('<b>क्या काम आता है:</b> A routine borrowed from someone else rarely lasts. We build a simple morning and evening rhythm around your real work hours, one you can keep on a bad day too.', '<b>क्या काम आता है:</b> किसी और से उधार लिया रूटीन कम ही टिकता है। हम आपके असली काम के समय के हिसाब से सुबह-शाम का आसान रूटीन बनाते हैं, जो खराब दिन में भी चल सके।'),
 ('<b>क्या काम आता है:</b> Family and friends give kind advice. You may need an outside view, free of emotional bias, to weigh your options and choose with a calm mind.', '<b>क्या काम आता है:</b> घरवाले और दोस्त प्यार से सलाह देते हैं। आपको शायद एक बाहर की नज़र चाहिए, जो बिना किसी भावना के आपके ऑप्शन तौले और आप शांत मन से चुन सकें।'),
 ('<b>क्या काम आता है:</b> Often you already know the answer, but the noise around you is louder. This is a quiet, judgment-free space to say it out loud.', '<b>क्या काम आता है:</b> अक्सर जवाब आपको पहले से पता होता है, बस आसपास का शोर ज़्यादा होता है। ये एक शांत जगह है जहाँ कोई जज नहीं करेगा, आप खुलकर बोल सकते हैं।'),
 ("'clarity-call-30': 'Clarity Call', 'dincharya-45': 'Dincharya Reset', 'deep-dive-60': 'Deep Dive'", "'clarity-call-30': 'क्लैरिटी कॉल', 'dincharya-45': 'दिनचर्या रीसेट', 'deep-dive-60': 'डीप डाइव'"),
 ('Please enter your full name.', 'कृपया अपना पूरा नाम लिखें।'),
 ('Please enter a valid email address.', 'कृपया सही ईमेल लिखें।'),
 ('Please enter a valid 10-digit Indian WhatsApp number.', 'कृपया 10 अंकों का सही WhatsApp नंबर लिखें।'),
 ('Please describe your question or issue in a few words.', 'कृपया अपना सवाल या दिक्कत कुछ शब्दों में लिखें।'),
 ('Initializing priority slot checkout...', 'चेकआउट खुल रहा है...'),
 ('Failed to initialize order', 'ऑर्डर शुरू नहीं हो पाया'),
 ('Verifying payment...', 'पेमेंट चेक हो रहा है...'),
 ('Payment was cancelled or failed. Please try again.', 'पेमेंट कैंसल या फेल हो गया। कृपया दोबारा कोशिश करें।'),
 ('Razorpay is in test mode. Feel free to pick a time directly on Cal.com!', 'Razorpay अभी टेस्ट मोड में है। आप सीधे Cal.com पर भी समय चुन सकते हैं!'),
 ('Please choose a date.', 'कृपया तारीख चुनें।'),
 ('Please enter your city.', 'कृपया अपना शहर लिखें।'),
 ('Please enter your age (15 to 85).', 'कृपया अपनी उम्र लिखें (15 से 85)।'),
 ('Thank you. Your booking is requested. I will confirm it by email shortly.', 'धन्यवाद। आपकी बुकिंग की रिक्वेस्ट मिल गई है। मैं जल्दी ही ईमेल से कन्फर्म करूँगा।'),
 ('Please enter the email you booked with.', 'कृपया वो ईमेल लिखें जिससे बुक किया था।'),
 ('Please enter the UTR or reference number from your UPI app.', 'कृपया UPI ऐप वाला UTR या रेफरेंस नंबर लिखें।'),
 ('Something went wrong.', 'कुछ गड़बड़ हो गई।'),
 ("Thank you. I will check the payment and confirm your booking. Cal.com will email you the Meet link once it is confirmed.", "धन्यवाद। मैं पेमेंट देखकर आपकी बुकिंग कन्फर्म करूँगा। कन्फर्म होते ही Cal.com आपको Meet लिंक ईमेल कर देगा।"),
 ("btn.disabled = false; btn.textContent = 'I have paid'", "btn.disabled = false; btn.textContent = 'मैंने पे कर दिया'"),
 ("btn.textContent = 'Sending'", "btn.textContent = 'भेज रहे हैं'"),
 ("'Copied'", "'कॉपी हो गया'"),
 ("textContent = 'Copy'", "textContent = 'कॉपी'"),
 ('Payment received', 'पेमेंट मिल गया'),
 ('Session Confirmed', 'सेशन कन्फर्म हो गया'),
 ('Thank you, <b>${escapeHtml(formData.name)}</b>. Your booking is confirmed. I will reach out on your WhatsApp within 24 hours.', 'धन्यवाद, <b>${escapeHtml(formData.name)}</b>। आपकी बुकिंग कन्फर्म हो गई है। मैं 24 घंटे में आपके WhatsApp पर संपर्क करूँगा।'),
 ('<span>Track:</span>', '<span>सेशन:</span>'),
 ('<span>Date:</span>', '<span>तारीख:</span>'),
 ('<span>Fee:</span>', '<span>फीस:</span>'),
 ('<span>Payment ID:</span>', '<span>पेमेंट ID:</span>'),
 ("'Hi Harsh, I just booked my session for '", "'नमस्ते हर्ष, मैंने अभी यह सेशन बुक किया है: '"),
 ("' (Payment ID: '", "' (पेमेंट ID: '"),
 ('Message on WhatsApp', 'WhatsApp पर मैसेज करें'),
 ('Pay ₹${price} securely', '₹${price} पे करें'),
 ("toLocaleString('en-IN'", "toLocaleString('hi-IN'"),
 ("toLocaleDateString('en-IN'", "toLocaleDateString('hi-IN'"),
]
for en, hi in J: raw(en, hi)

# ---------- page shell: lang, paths, language switch, fonts ----------
raw('<html lang="en">', '<html lang="hi">')
s = s.replace('src="assets/', 'src="../assets/').replace('href="assets/', 'href="../assets/').replace('content="assets/', 'content="../assets/')
raw('<a class="lang-switch" href="hi/index.html" hreflang="hi" lang="hi">हिंदी</a>', '<a class="lang-switch" href="../index.html" hreflang="en" lang="en">English</a>')
raw('<link rel="alternate" hreflang="hi" href="hi/index.html">', '<link rel="alternate" hreflang="en" href="../index.html">')
raw('family=Tiro+Devanagari+Hindi&display=swap', 'family=Tiro+Devanagari+Hindi&family=Noto+Sans+Devanagari:wght@400;500;600&display=swap')
hi_css = '''
    /* Hindi version: Devanagari-friendly type */
    :root { --font: 'DM Sans', 'Noto Sans Devanagari', sans-serif; --font-display: 'Newsreader', 'Tiro Devanagari Hindi', Georgia, serif; }
    body { line-height: 1.85; }
    h1, h2, h3, h4, .hero-headline, .section-heading, .truth h3, .relief-item h3, .journey-title, .reveal-title, .reframe, .service-meta h3, .diag-card-body h4, .pay-card h3 { letter-spacing: 0 !important; line-height: 1.4; }
    .hero-headline { font-size: clamp(2.2rem, 4.2vw, 3.7rem); }
    .btn-solid, .form-btn, .mobile-bar-cta, .header-cta { line-height: 1.3; }
    .truth-label, .footer-col h4, .pay-kicker { letter-spacing: 0.04em; text-transform: none; }
  </style>'''
s = s.replace('  </style>\n</head>', hi_css + '\n</head>', 1)

if missing:
    print('MISSING (not found in index.html):')
    for m in missing: print('  ', m)
    sys.exit(1)
open('hi/index.html', 'w', encoding='utf-8').write(s)
print('hi/index.html written,', len(s), 'bytes')
