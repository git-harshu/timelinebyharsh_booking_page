// Shared helpers for Razorpay and Form Validation
export const AMOUNT_PAISE = 29900; // ₹299.00 fixed session fee
export const CURRENCY = "INR";

export function rzpAuth() {
  const { RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET } = process.env;
  if (!RAZORPAY_KEY_ID || !RAZORPAY_KEY_SECRET) {
    throw new Error("Razorpay environment variables missing");
  }
  return "Basic " + Buffer.from(`${RAZORPAY_KEY_ID}:${RAZORPAY_KEY_SECRET}`).toString("base64");
}

export async function rzp(path, init = {}) {
  const r = await fetch("https://api.razorpay.com/v1" + path, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      Authorization: rzpAuth(),
      ...(init.headers || {})
    }
  });
  const j = await r.json();
  if (!r.ok) throw new Error(j?.error?.description || `Razorpay ${r.status}`);
  return j;
}

// Clean and sanitize form data for Razorpay notes (max 15 keys, each max 256 chars)
export function cleanNotes(input = {}) {
  const pick = [
    "name",
    "email",
    "whatsapp",
    "age",
    "city",
    "handle",
    "track",
    "preferred_date",
    "preferred_time",
    "question",
    "birth_details",
    "jaap_vrat"
  ];
  const out = {};
  for (const k of pick) {
    const v = input[k];
    if (v !== undefined && v !== null && String(v).trim() !== "") {
      out[k] = String(v).trim().slice(0, 250);
    }
  }
  return out;
}

export function validate(n) {
  const bad = [];
  if (!n.name || n.name.trim().length < 2) bad.push("name");
  if (!n.email || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(n.email)) bad.push("email");
  if (!n.whatsapp || !/^[6-9]\d{9}$/.test(String(n.whatsapp).replace(/\D/g, "").slice(-10))) bad.push("whatsapp");
  if (!n.age || !/^\d{1,2}$/.test(String(n.age)) || +n.age < 13 || +n.age > 99) bad.push("age");
  if (!n.city || n.city.trim().length < 2) bad.push("city");
  if (!n.handle || n.handle.trim().length < 2) bad.push("handle");
  if (!n.track) bad.push("track");
  if (!n.question || n.question.trim().length < 5) bad.push("question");
  return bad;
}
