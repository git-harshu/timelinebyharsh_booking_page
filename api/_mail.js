// Gmail SMTP email sender (Nodemailer)
// Requires: GMAIL_USER, GMAIL_APP_PASSWORD, OWNER_EMAIL
import nodemailer from "nodemailer";

function transport() {
  const { GMAIL_USER, GMAIL_APP_PASSWORD } = process.env;
  if (!GMAIL_USER || !GMAIL_APP_PASSWORD) {
    throw new Error("Gmail environment variables missing");
  }
  return nodemailer.createTransport({
    host: "smtp.gmail.com",
    port: 465,
    secure: true,
    auth: { user: GMAIL_USER, pass: GMAIL_APP_PASSWORD }
  });
}

const esc = (v) =>
  String(v ?? "-").replace(/[<>&"]/g, (c) => ({ "<": "&lt;", ">": "&gt;", "&": "&amp;", '"': "&quot;" }[c]));

const row = (k, v) => `<tr>
  <td style="padding:10px 14px;border-bottom:1px solid #E4E7EF;color:#5E687A;font-size:14px;white-space:nowrap;font-weight:600">${k}</td>
  <td style="padding:10px 14px;border-bottom:1px solid #E4E7EF;color:#1A2332;font-size:14px">${esc(v)}</td>
</tr>`;

function shell(title, inner) {
  return `<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:580px;margin:24px auto;background:#FFFFFF;border:1px solid #E2E6EE;border-radius:12px;padding:28px 24px;color:#2D3748">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
      <div style="width:40px;height:40px;border-radius:8px;background:#21252B;color:#FF6F1E;display:grid;place-items:center;font-weight:bold;font-size:18px;text-align:center;line-height:40px">H</div>
      <div>
        <h2 style="color:#21252B;font-size:20px;margin:0;font-weight:600">${title}</h2>
        <p style="margin:2px 0 0;font-size:13px;color:#686E78">@timelinebyharsh · 1:1 Guidance Session</p>
      </div>
    </div>
    <div style="height:3px;background:linear-gradient(90deg, #FF6F1E, #FF9E66);border-radius:2px;margin:0 0 20px"></div>
    ${inner}
    <div style="margin-top:28px;padding-top:16px;border-top:1px solid #E2E6EE;text-align:center;font-size:12px;color:#94A3B8">
      <p style="margin:0">Have questions? Reply directly to this email or reach out on Instagram <b>@timelinebyharsh</b></p>
    </div>
  </div>`;
}

// 1) Notification sent to Harsh
function ownerMail(n, p) {
  const table = `<table style="border-collapse:collapse;width:100%;background:#FAF8F5;border:1px solid #E7E2D9;border-radius:8px;overflow:hidden">
    ${row("Full Name", n.name)}
    ${row("WhatsApp", "+91 " + (n.whatsapp || ""))}
    ${row("Email", n.email)}
    ${row("Age / City", `${n.age || "-"} yrs · ${n.city || "-"}`)}
    ${n.handle ? row("Instagram / Handle", n.handle) : ""}
    ${row("Consultation Topic", n.track)}
    ${row("Preferred Time", `${n.preferred_date || "-"} @ ${n.preferred_time || "-"}`)}
    ${row("Question / Dilemma", n.question)}
    ${n.birth_details ? row("Birth Details", n.birth_details) : ""}
    ${n.jaap_vrat ? row("Current Jaap / Vrat", n.jaap_vrat) : ""}
    ${row("Amount Paid", "₹" + (p.amount / 100))}
    ${row("Payment Method", p.method)}
    ${row("Payment ID", p.id)}
  </table>`;
  return {
    subject: `⚡ New 1:1 Booking — ${n.name || "Client"} (${n.track || "Consultation"})`,
    html: shell("New 1:1 Session Booked!", table)
  };
}

// 2) Confirmation sent to Client
function clientMail(n, p) {
  const inner = `
    <p style="font-size:16px;line-height:1.6;color:#21252B">Namaste <b>${esc(n.name)}</b>,</p>
    <p style="font-size:15px;line-height:1.6;color:#686E78">
      Thank you for scheduling a 1:1 session with Harsh. Your payment has been received and your booking is confirmed.
    </p>
    <table style="border-collapse:collapse;width:100%;background:#FAF8F5;border:1px solid #E7E2D9;border-radius:8px;margin:18px 0;overflow:hidden">
      ${row("Session Type", "30-Minute 1:1 Private Guidance Call")}
      ${row("Consultation Topic", n.track)}
      ${row("Preferred Slot", `${n.preferred_date || "-"} @ ${n.preferred_time || "-"}`)}
      ${row("Amount Paid", "₹" + (p.amount / 100))}
      ${row("Payment ID", p.id)}
    </table>
    <div style="background:#FFF5EE;border-left:4px solid #FF6F1E;padding:14px 16px;border-radius:6px;margin:20px 0">
      <h4 style="margin:0 0 6px;color:#B45309;font-size:14px;text-transform:uppercase;letter-spacing:0.05em">What Happens Next?</h4>
      <p style="margin:0;font-size:14px;color:#78350F;line-height:1.6">
        Harsh will message you on WhatsApp (<b>+91 ${esc(n.whatsapp)}</b>) within 24 hours with your Google Meet link and confirm your exact slot.
      </p>
    </div>
    <p style="font-size:13px;color:#686E78;line-height:1.5">
      <b>Rescheduling policy:</b> If you need to change your time, please notify at least 6 hours in advance so we can reschedule without any problem.
    </p>`;
  return {
    subject: "✅ Booking Confirmed — 1:1 Session with Harsh (@timelinebyharsh)",
    html: shell("Booking Confirmed!", inner)
  };
}

export async function sendBookingEmails(notes, payment) {
  const t = transport();
  const from = `"Harsh | Timeline by Harsh" <${process.env.GMAIL_USER}>`;
  const owner = process.env.OWNER_EMAIL || process.env.GMAIL_USER;

  const jobs = [];
  const o = ownerMail(notes, payment);
  jobs.push(t.sendMail({ from, to: owner, replyTo: notes.email, subject: o.subject, html: o.html }));

  if (notes.email) {
    const c = clientMail(notes, payment);
    jobs.push(t.sendMail({ from, to: notes.email, replyTo: owner, subject: c.subject, html: c.html }));
  }
  return Promise.allSettled(jobs);
}


// 3) UPI payment claim: the visitor says they paid and gives the UTR. Harsh checks his bank app, then accepts the booking in Cal.com.
export async function sendPaymentClaim({ email, utr, amount, session, slot }) {
  const t = transport();
  const from = `"Harsh | Timeline by Harsh" <${process.env.GMAIL_USER}>`;
  const owner = process.env.OWNER_EMAIL || process.env.GMAIL_USER;

  const table = `<table style="border-collapse:collapse;width:100%;background:#FAF8F5;border:1px solid #E7E2D9;border-radius:8px;overflow:hidden">
    ${row("Booked with email", email)}
    ${row("Session", session)}
    ${row("Slot", slot)}
    ${row("Amount to check", "\u20B9" + amount)}
    ${row("UTR / reference", utr)}
  </table>
  <p style="font-size:14px;line-height:1.6;color:#5E6470;margin-top:16px">
    Check this payment in your bank or UPI app. If it matches, accept the booking in Cal.com (Bookings, Unconfirmed). If it does not, reply to this email.
  </p>`;

  const jobs = [
    t.sendMail({ from, to: owner, replyTo: email, subject: `UPI payment to verify: \u20B9${amount} (${session})`, html: shell("UPI payment to verify", table) })
  ];
  const ack = `<p style="font-size:15px;line-height:1.6;color:#21252B">Thank you. I have your payment reference <b>${esc(utr)}</b> for <b>${esc(session)}</b>.</p>
    <p style="font-size:14px;line-height:1.6;color:#5E6470">I will check it and confirm your booking. Cal.com will email you the Google Meet link once it is confirmed. If you do not hear from me within a few hours, reply to this email.</p>`;
  jobs.push(t.sendMail({ from, to: email, replyTo: owner, subject: "I received your payment reference", html: shell("Payment reference received", ack) }));
  return Promise.allSettled(jobs);
}


// 4) Early-access list signup (guides, live sessions, puja preparation). Mails Harsh the lead and thanks the subscriber.
export async function sendSignup({ email, whatsapp, interests }) {
  const t = transport();
  const from = `"Harsh | Timeline by Harsh" <${process.env.GMAIL_USER}>`;
  const owner = process.env.OWNER_EMAIL || process.env.GMAIL_USER;
  const list = interests && interests.length ? interests.join(", ") : "-";

  const table = `<table style="border-collapse:collapse;width:100%;background:#FAF8F5;border:1px solid #E7E2D9;border-radius:8px;overflow:hidden">
    ${row("Email", email)}
    ${row("WhatsApp", whatsapp ? "+91 " + whatsapp : "-")}
    ${row("Interested in", list)}
    ${row("Consent", "Agreed to receive messages about these resources")}
  </table>`;
  const jobs = [
    t.sendMail({ from, to: owner, replyTo: email, subject: `New early-access signup: ${email}`, html: shell("New early-access signup", table) })
  ];
  const ack = `<p style="font-size:15px;line-height:1.6;color:#21252B">Thank you for joining the list.</p>
    <p style="font-size:14px;line-height:1.6;color:#5E6470">I will write to you when the first guide is ready. You asked about: <b>${esc(list)}</b>. To stop these messages at any time, just reply to this email.</p>`;
  jobs.push(t.sendMail({ from, to: email, replyTo: owner, subject: "You are on the list", html: shell("You are on the list", ack) }));
  return Promise.allSettled(jobs);
}
