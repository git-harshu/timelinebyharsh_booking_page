// One Worker: static site from ./dist, plus the same /api handlers that run on Vercel.
// The handlers are written as (req, res); this file gives them a tiny req/res on top of fetch().
import upiClaim from "../api/upi-claim.js";
import subscribe from "../api/subscribe.js";

const ROUTES = {
  "/api/upi-claim": upiClaim,
  "/api/subscribe": subscribe,
};

async function run(handler, request) {
  const url = new URL(request.url);
  const method = request.method;
  const raw = method === "GET" || method === "HEAD" ? new Uint8Array() : new Uint8Array(await request.arrayBuffer());
  const text = new TextDecoder().decode(raw);
  const headers = {};
  request.headers.forEach((v, k) => { headers[k] = v; });
  let body;
  if (text) { try { body = JSON.parse(text); } catch { body = text; } }

  const req = {
    method, headers, body,
    query: Object.fromEntries(url.searchParams),
    async *[Symbol.asyncIterator]() { yield raw; },
  };
  let status = 200, payload = null;
  const outHeaders = new Headers();
  const res = {
    status(c) { status = c; return this; },
    setHeader(k, v) { outHeaders.set(k, v); return this; },
    json(o) { outHeaders.set("content-type", "application/json"); payload = JSON.stringify(o); return this; },
    send(x) { payload = typeof x === "string" ? x : JSON.stringify(x); return this; },
    end(x) { if (x !== undefined) payload = x; return this; },
  };
  await handler(req, res);
  outHeaders.set("cache-control", "no-store");
  return new Response(payload, { status, headers: outHeaders });
}

export default {
  async fetch(request, env) {
    const { pathname } = new URL(request.url);
    const handler = ROUTES[pathname];
    if (!handler) return env.ASSETS.fetch(request);
    try {
      return await run(handler, request);
    } catch (e) {
      return new Response(JSON.stringify({ error: "Server error" }), { status: 500, headers: { "content-type": "application/json" } });
    }
  },
};
