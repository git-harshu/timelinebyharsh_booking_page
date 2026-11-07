# Handoff: 2026-11-08

## 1. Goal
Make the Timeline by Harsh booking site visual first, calm and conversion focused: no repeated sections, first-person copy, Hindu symbols and micro-interactions that are different per section, plus the legal pages. Payment code untouched.

## 2. Current state
Update (design-r11): two languages. English at /, Hinglish (everyday Hindi written in English letters, language label 'Hinglish') at /hi/. hi/ pages are GENERATED: run `python3 tools/build_hi.py` after any change to index.html (it stops if an English string is missing from the map) and `python3 tools/build_legal_hi.py` for about/privacy/terms/refund/cookies. Language switch is in every header. Mobile: hero order is heading, graphic, description, buttons; text centred; the three moments stack as sticky cards (tint, orange, tint); finder detail opens under the chosen choice with a full-width Book button; all cards use a 12px radius. Three hero options for desktop are in hero-options/ (option-a/b/c.html), waiting for Harsh to pick one; then apply it to index.html and rebuild hi/. Hinglish and legal translations are drafts for Harsh to review. Shlokas in the strip stay in Devanagari on purpose.

Update (design-r10): Cal events clarity-call-30, dincharya-45, deep-dive-60 now have confirmationPolicy always + blockUnconfirmedBookingsInBooker (set through the API). After a booking, a UPI popup (QR, amount, UTR form) opens via the embed event bookingSuccessfulV2; api/upi-claim.js emails Harsh. SITE.upiId in index.html is EMPTY, so the popup shows only a thank-you until it is filled. Header Book a call is static on desktop; the transparent bottom bar is mobile only. Arrows removed everywhere. Finder detail card matches the choices height. Marquee uses plain white Om. Not tested with a real Cal booking or a real email send.

Update (design-r9): page order is now problem first: hero (problem) > shlokas > It is rarely a lack of discipline > Which one sounds like you? > What changes after one honest conversation > How a session goes > Pick the length that fits > Choose a time > Common questions > Books I Recommend > closing Hindi quote > footer. Hero CTA is soft (What is weighing on you?); header Book a call appears after the hero button scrolls away; mobile gets a bottom Book a call bar (hidden on desktop and while the booking section is on screen). Om scroll button removed. Session buttons are full width. Booking tabs and both panels share one 760px column. Copy follows problem-aware awareness (Schwartz), problem then reframe then relief then offer; all copy is a draft for Harsh to approve, no testimonials or stats invented.

Update (design-r5): proper dark 4-column footer on all pages; priority form is now 3 steps (Session, About you, Your question) with per-step validation, submit handler untouched; booking tabs are a segmented control with a sliding thumb; journey bars removed and top line greyed; quote has curly quotes and a ~ attribution, diyas removed; FAQ is two columns. Pay button text is now "Pay ₹X securely".

index.html restructured (tag design-r4): header with Instagram profile picture as logo and 4 clean links; split hero (copy left, mandala right); shloka marquee; light Hindi quote with diya row; Clarity Finder as master-detail (choices left, detail right); 3 session cards with orange Book buttons; "How a session goes" with duration bars; "Choose a time" with left-aligned tab bar; Common questions (7); Books I Recommend. Sections alternate white and tint. Om button bottom-right appears after scrolling, ring shows progress, click returns to top. New pages: about, privacy, terms, refund, cookies (+ legal.css). Footer links to all. Admin link removed from public footer (page still at /bookings.html behind ADMIN_TOKEN).

## 3. Active files
- index.html: all of the above.
- legal.css, about.html, privacy.html, terms.html, refund.html, cookies.html: new, plain static pages.
- assets/logo.jpg: Instagram profile picture, 150x150.
- .env.local (gitignored): CAL_API_KEY. api/*.js edits from before this work are still uncommitted and not mine.

## 4. Changes made
- a7cfa42 / design-r2, 4ff8c62 / design-r3, then design-r4 (this session's commit).
- Cal.com events created via API: clarity-call-30, dincharya-45, deep-dive-60 (see earlier handoff).
- Display names changed (Clarity Call, Dincharya Reset, Deep Dive); data-service and option values unchanged so booking JS and api/_lib.js pricing still match.
- "Sounding board" finder choice now maps to the Clarity Call track (it mapped to a track that had no option).
- Removed the unverified "1,200+ conversations" claim.

## 5. Failed attempts
- First batch edit script aborted: the success-modal h3 used `font-weight:700` (no space) so the pattern missed. Nothing was written (asserts run before write). Fixed the pattern and reran.
- `.book-art { display:none }` placed before the later `.book-art` rule was overridden. Fixed with the `.book-card .book-art` selector.
- r3: first Cal.com embed pointed at username "timelinebyharsh" and event "30min". Both 404: the real username is harsh-upadhyay-tsgoiw and the account had zero event types. Fixed by creating events through the Cal API.
- Fetching dalialane.yoga with firecrawl returned 390K chars; had to probe the saved JSON with python instead of reading it.
- r4/r5: a regex that replaced the favicon `<link ... >` stopped at the first `>` inside the SVG data URL and leaked SVG text onto the page top-left. Caught in a screenshot, fixed. Lesson: after regex edits on HTML, screenshot the top of the page.
- unavatar.io returned 403 and firecrawl refuses instagram.com. The profile picture came from the og:image tag of the public Instagram page (150x150, so logo-size only).

## 6. Next steps
1. Harsh to approve: the 6 shlokas in the marquee, the first-person copy, and the About text (written from public facts only: name, handle, Hindu religious content creator, session format).
2. Harsh or a lawyer to review privacy, terms, refund and cookies pages. They are drafts based on how the site works (Razorpay, Cal.com, Google, WhatsApp, no analytics) and the existing 6 hour reschedule rule. Refund rules are my proposal.
3. Add a dedicated contact email to the legal pages (they currently point to Instagram and the booking email/WhatsApp).
4. Rotate the Cal API key (pasted in chat), update .env.local and Vercel.
5. Higher resolution profile picture for the logo, real book covers.
6. bookings.html still has the old look. Decide on the uncommitted api/ edits. Optional: server route using CAL_API_KEY to list Cal bookings.
