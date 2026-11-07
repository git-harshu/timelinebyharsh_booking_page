# Handoff: 2026-11-08

## 1. Goal
Make the Timeline by Harsh booking site (index.html) visual first, living (micro-interactions) and spiritually grounded (Hindu symbols), inspired by dalialane.yoga. Design only, plus wiring the Cal.com booking embed. Payment flow code untouched.

## 2. Current state
r3 applied to index.html: mandala hero, shloka marquee, dark Om quote block, icon-led diagnostic cards, collapsed "What is included" accordions, self-drawing journey line, colour-block book covers, scroll reveal. Hover lift removed everywhere (colour change only). Cal.com embed now loads harsh-upadhyay-tsgoiw/clarity-call-30. bookings.html still old (Poppins, gradients). Sanskrit shlokas and "1,200+" not yet approved.

## 3. Active files
- index.html: all design + Cal wiring (embed link, service switcher script at end of body).
- .env.local (gitignored): now holds CAL_API_KEY. .env.example has an empty CAL_API_KEY line.
- HANDOFF.md, *.bak-2026-11-08 backups.
- api/_lib.js, create-order.js, verify.js: uncommitted edits from BEFORE this work, not mine.

## 4. Changes made
- a7cfa42 / tag design-r2: first de-slop pass.
- r3 (commit after a7cfa42, tag design-r3): see Current state. Cal events created on Harsh's Cal account through the API: clarity-call-30 (id 7816740), dincharya-45 (7816741), deep-dive-60 (7816742), all with Google Meet location.
- Embed switches event when a "Reserve Slot" button for 45 or 60 min is clicked.

## 5. Failed attempts
- First batch edit script aborted: the success-modal h3 used `font-weight:700` (no space) so the pattern missed. Nothing was written (asserts run before write). Fixed the pattern and reran.
- `.book-art { display:none }` placed before the later `.book-art` rule was overridden. Fixed with the `.book-card .book-art` selector.
- r3: first Cal.com embed pointed at username "timelinebyharsh" and event "30min". Both 404: the real username is harsh-upadhyay-tsgoiw and the account had zero event types. Fixed by creating events through the Cal API.
- Fetching dalialane.yoga with firecrawl returned 390K chars; had to probe the saved JSON with python instead of reading it.


## 6. Next steps
1. Harsh to approve the 6 shlokas in the marquee (Devanagari, index.html marquee block) and confirm "1,200+ conversations".
2. Rotate the Cal API key (it was pasted in a chat), then update CAL_API_KEY in .env.local and in Vercel env.
3. In Cal: confirm Google Calendar is connected so Google Meet links generate, set availability, and add the paid/priority rules if wanted.
4. Optional: add a server route using CAL_API_KEY so bookings.html lists Cal bookings, and so the paid Priority Slot creates a Cal booking.
5. Apply the same fonts and flat buttons to bookings.html.
6. Real photo of Harsh and real book covers; decide on uncommitted api/ edits.
