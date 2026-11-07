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
      <div style="width:40px;height:40px;border-radius:8px;background:#2563EB;color:#FFFFFF;display:grid;place-items:center;font-weight:bold;font-size:18px;text-align:center;line-height:40px">H</div>
      <div>
        <h2 style="color:#0F172A;font-size:20px;margin:0;font-weight:700">${title}</h2>
        <p style="margin:2px 0 0;font-size:13px;color:#64748B">@timelinebyharsh · 1:1 Personal Sessions</p>
      </div>
    </div>
    <div style="height:3px;background:linear-gradient(90deg, #2563EB, #60A5FA);border-radius:2px;margin:0 0 20px"></div>
    ${inner}
    <div style="margin-top:28px;padding-top:16px;border-top:1px solid #E2E6EE;text-align:center;font-size:12px;color:#94A3B8">
      <p style="margin:0">Have questions? Reply directly to this email or reach out on Instagram <b>@timelinebyharsh</b></p>
    </div>
  </div>`;
}

// 1) Notification sent to Harsh
function ownerMail(n, p) {
  const table = `<table style="border-collapse:collapse;width:100%;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:8px;overflow:hidden">
    ${row("Full Name", n.name)}
    ${row("WhatsApp", "+91 " + (n.whatsapp || ""))}
    ${row("Email", n.email)}
    ${row("Age / City", `${n.age || "-"} yrs · ${n.city || "-"}`)}
    ${row("Social Handle", n.handle)}
    ${row("Session Track", n.track)}
    ${row("Preferred Time", `${n.preferred_date || "-"} @ ${n.preferred_time || "-"}`)}
    ${row("Topic / Question", n.question)}
    ${n.birth_details ? row("Birth Details", n.birth_details) : ""}
    ${n.jaap_vrat ? row("Current Jaap / Vrat", n.jaap_vrat) : ""}
    ${row("Amount Paid", "₹" + (p.amount / 100))}
    ${row("Payment Method", p.method)}
    ${row("Payment ID", p.id)}
  </table>`;
  return {
    subject: `⚡ New 1:1 Booking — ${n.name || "Client"} (${n.track || "General"})`,
    html: shell("New 1:1 Session Booked!", table)
  };
}

// 2) Confirmation sent to Client
function clientMail(n, p) {
  const inner = `
    <p style="font-size:16px;line-height:1.6;color:#1E293B">Hello <b>${esc(n.name)}</b>,</p>
    <p style="font-size:15px;line-height:1.6;color:#334155">
      Thank you for booking a 1:1 session with Harsh. Your payment has been received and your booking is confirmed!
    </p>
    <table style="border-collapse:collapse;width:100%;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:8px;margin:18px 0;overflow:hidden">
      ${row("Session Type", "45-Minute 1:1 Private Guidance Call")}
      ${row("Selected Track", n.track)}
      ${row("Preferred Slot", `${n.preferred_date || "-"} @ ${n.preferred_time || "-"}`)}
      ${row("Amount Paid", "₹" + (p.amount / 100))}
      ${row("Payment ID", p.id)}
    </table>
    <div style="background:#EFF6FF;border-left:4px solid #2563EB;padding:14px 16px;border-radius:6px;margin:20px 0">
      <h4 style="margin:0 0 6px;color:#1E40AF;font-size:14px;text-transform:uppercase;letter-spacing:0.05em">What Happens Next?</h4>
      <p style="margin:0;font-size:14px;color:#1E3A8A;line-height:1.6">
        Harsh will message you on WhatsApp (<b>+91 ${esc(n.whatsapp)}</b>) within 24 hours to confirm the exact time and send your Google Meet invite link.
      </p>
    </div>
    <p style="font-size:13px;color:#64748B;line-height:1.5">
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
