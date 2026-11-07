// POST /api/subscribe { email, whatsapp?, interests[], consent, website } -> { ok: true }
// Early-access list. Emails Harsh the lead; there is no database. "website" is a honeypot for bots.
import { sendSignup } from "./_mail.js";

const INTERESTS = new Set(["Festival and vrat guide", "Live sessions", "Puja preparation session", "Gita study circle"]);
const clean = (v, n) => String(v ?? "").replace(/[\r\n]+/g, " ").trim().slice(0, n);

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed. Use POST." });

  try {
    const b = typeof req.body === "string" ? JSON.parse(req.body || "{}") : (req.body || {});
    if (clean(b.website, 50)) return res.status(200).json({ ok: true }); // bot: pretend success

    const email = clean(b.email, 120);
    const digits = String(b.whatsapp ?? "").replace(/\D/g, "").slice(-10);
    const interests = (Array.isArray(b.interests) ? b.interests : []).map((x) => clean(x, 40)).filter((x) => INTERESTS.has(x)).slice(0, 4);

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return res.status(400).json({ error: "Please enter a valid email address." });
    if (digits && !/^[6-9]\d{9}$/.test(digits)) return res.status(400).json({ error: "Please enter a valid 10-digit WhatsApp number, or leave it empty." });
    if (b.consent !== true) return res.status(400).json({ error: "Please tick the box to agree." });

    await sendSignup({ email, whatsapp: digits, interests });
    return res.status(200).json({ ok: true });
  } catch (e) {
    return res.status(500).json({ error: "Could not save your details. Please try again in a moment." });
  }
}
