// Replaces `nodemailer` inside the Cloudflare Worker bundle (see "alias" in wrangler.jsonc).
// api/_mail.js keeps calling nodemailer.createTransport(...).sendMail(...); here that goes over Cloudflare TCP sockets.
import { WorkerMailer } from "worker-mailer";

function parseAddress(v) {
  const m = String(v || "").match(/^\s*"?([^"<]*?)"?\s*<([^>]+)>\s*$/);
  return m ? { name: m[1].trim() || undefined, email: m[2].trim() } : { email: String(v || "").trim() };
}

export default {
  createTransport(cfg) {
    return {
      async sendMail(m) {
        await WorkerMailer.send(
          {
            host: cfg.host,
            port: cfg.port,
            secure: !!cfg.secure,
            startTls: false,
            authType: "plain",
            credentials: { username: cfg.auth.user, password: cfg.auth.pass },
          },
          {
            from: parseAddress(m.from),
            to: parseAddress(m.to),
            reply: m.replyTo ? parseAddress(m.replyTo) : undefined,
            subject: m.subject,
            html: m.html,
            text: m.text,
          }
        );
        return { accepted: [m.to] };
      },
    };
  },
};
