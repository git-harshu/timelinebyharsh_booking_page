// POST /api/upi-claim { email, utr, amount, session, slot } -> { ok: true }
// Emails Harsh a payment to verify (and acknowledges the visitor). It does not confirm anything by itself.
import { sendPaymentClaim } from "./_mail.js";

const AMOUNTS = new Set([299, 499, 699]);
const clean = (v, n) => String(v ?? "").replace(/[\r\n]+/g, " ").trim().slice(0, n);

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed. Use POST." });

  try {
    const b = typeof req.body === "string" ? JSON.parse(req.body || "{}") : (req.body || {});
    const email = clean(b.email, 120);
    const utr = clean(b.utr, 30);
    const amount = Number(b.amount);
    const session = clean(b.session, 80);
    const slot = clean(b.slot, 80) || "-";

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return res.status(400).json({ error: "Please enter the email you booked with." });
    if (!/^[A-Za-z0-9]{8,24}$/.test(utr)) return res.status(400).json({ error: "Please enter the UTR or reference number from your UPI app." });
    if (!AMOUNTS.has(amount)) return res.status(400).json({ error: "Invalid amount." });
    if (!session) return res.status(400).json({ error: "Missing session." });

    await sendPaymentClaim({ email, utr, amount, session, slot });
    return res.status(200).json({ ok: true });
  } catch (e) {
    return res.status(500).json({ error: "Could not send your payment reference. Please reply to your booking email instead." });
  }
}
