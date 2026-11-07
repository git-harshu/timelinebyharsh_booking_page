// POST /api/create-order { form: {...} } -> { order_id, key_id, amount }
import { AMOUNT_PAISE, CURRENCY, rzp, cleanNotes, validate, getAmountForTrack } from "./_lib.js";

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed. Use POST." });
  }

  try {
    const body = typeof req.body === "string" ? JSON.parse(req.body || "{}") : (req.body || {});
    const notes = cleanNotes(body.form || body.notes || body);
    const bad = validate(notes);
    if (bad.length) {
      return res.status(400).json({
        error: "Please complete all required fields: " + bad.join(", "),
        fields: bad
      });
    }

    const amount = getAmountForTrack(notes.track);
    const order = await rzp("/orders", {
      method: "POST",
      body: JSON.stringify({
        amount,
        currency: CURRENCY,
        receipt: "call_" + Date.now(),
        notes
      })
    });

    return res.status(200).json({
      order_id: order.id,
      amount: order.amount,
      currency: order.currency,
      key_id: process.env.RAZORPAY_KEY_ID
    });
  } catch (e) {
    return res.status(500).json({ error: e.message || "Unable to create order. Please check Razorpay keys." });
  }
}
