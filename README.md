# Timeline by Harsh (@timelinebyharsh) — Official Website

Official website and booking platform for creator **Harsh Upadhyay (@timelinebyharsh)**.

Instagram: [https://www.instagram.com/timelinebyharsh/](https://www.instagram.com/timelinebyharsh/)

---

## What is Included

1. **Two 1:1 Consultation Paths (Ek Call, Do Raaste)**:
   - **Track A: Social Media & Creator Growth**: Reel hooks, profile audit, retention fixes, posting schedule, and 30-day plan.
   - **Track B: Spiritual Guidance & Daily Sadhana (Aadhyatmik Margdarshan)**: Rudraksh recommendations by Rashi, mantra jaap rules, pooja & temple setup, and sustainable 10-minute daily dincharya.
2. **Dual Booking Engine**:
   - **Cal.com Integration**: Free, automatic scheduling directly synced with Google Calendar and Google Meet.
   - **Priority Booking + Razorpay**: Direct payment checkout (₹299 commitment fee) with WhatsApp confirmation.
3. **Curated Shop & Affiliate Hub**:
   - Spiritual items (certified 5-Mukhi Rudraksh Mala, Sphatik Mala, pure copper water bottles, organic dhoop).
   - Sacred & transformative books (*Bhagavad Gita As It Is*, *Atomic Habits*, etc.).
   - Creator gear (wireless lapel mic for reels, overhead tripod with ring light, Sony ANC headphones).
   - Amazon Associates tags (`tag=timelineharsh-21`) and FTC disclosure.
4. **Admin Bookings Dashboard (`/bookings.html`)**:
   - Protected dashboard using `ADMIN_TOKEN` to view all bookings, clients, and WhatsApp quick message links.

---

## Quick Setup & Local Development

```bash
# 1. Install dependencies
npm install

# 2. Run local server
vercel dev --local --listen 3000
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## Configuring Cal.com (Free Google Meet Booking)

1. Sign up for a free account on [Cal.com](https://cal.com).
2. Connect your Google Calendar (under **Settings → Calendars**).
3. Create an event type (e.g. `30min` or `consultation`).
4. In `index.html`, update the `CAL_CONFIG` block around line 1330:
   ```javascript
   const CAL_CONFIG = {
     username: "your-cal-username", // e.g. timelinebyharsh
     eventSlug: "30min",            // e.g. 30min
     get calLink() { return `${this.username}/${this.eventSlug}`; }
   };
   ```
The embed and popup buttons will automatically update.

---

## Environment Variables (.env.local)

```ini
# Razorpay Credentials (from Dashboard -> Settings -> API Keys)
RAZORPAY_KEY_ID=rzp_test_...
RAZORPAY_KEY_SECRET=...
RAZORPAY_WEBHOOK_SECRET=...

# Admin token to access /bookings.html & /api/bookings
ADMIN_TOKEN=your_secret_admin_token

# Gmail SMTP for notifications
GMAIL_USER=timelinebyharsh@gmail.com
GMAIL_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
OWNER_EMAIL=timelinebyharsh@gmail.com
```
