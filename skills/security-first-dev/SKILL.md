---
name: security-first-dev
description: Security-first development for internet-facing features. Use when implementing any public surface, new integration, form, API or deploy; covers DDoS, quota exhaustion, headers, secrets and dependencies.
example-prompt: Implement a contact form on the site with protection against abuse.
---

# Security-first development

Expected outcome: public features that resist automated abuse and DDoS, with no exposed secrets and intact dependencies.

## When to use
- Any endpoint, page or form reachable from the internet.
- A new integration with an external service (third-party API, webhook, plugin).
- A deploy or a change of hosting/CDN.

## Risk assessment at design time (before coding)
- Surface: what becomes public, what accepts input from anyone, what costs money per call.
- Limits: API quotas, build minutes, bandwidth, database queries — what does an exhaustion attack take down first?
- Data: what leaks if the feature is abused or the log is exposed?
- Record in the technical plan, in one line: main risk + chosen protection.

## Default protections against abuse and DDoS
- Aggressive caching of static content and public pages (CDN/Netlify); never route an anonymous request through expensive rendering when a cache can serve it.
- Rate limiting per IP/session on endpoints that write, call paid APIs or send email; progressive blocking, not just an error.
- Forms: honeypot + server-side validation + minimum fill-in time; do not rely on a third-party widget alone.
- Fail-closed: a backend error never opens access; restrictive defaults.
- Mandatory headers: Content-Security-Policy, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Strict-Transport-Security (if HTTPS is managed).
- Minimal surface: turn off unused endpoints and debuggers; do not expose versions and stack in headers or error pages.

## Secrets and data
- A secret never goes into code, a commit, a log or a URL; only a local `.env` outside the repo (check `.gitignore` before the first commit).
- Tokens get the minimum scope; if exposed, revoke and reissue — deleting the file is not enough, Git history keeps the value.
- Personal data: collect the minimum; nothing sensitive without a real need and adequate protection.

## Dependency hygiene
- Before adding: active maintainer, adoption, known vulnerabilities (`npm audit` / advisories).
- On delivery: `npm audit` with no high/critical vulnerabilities; update with the smallest possible bump.

## Pre-deploy checklist
- Security headers present and validated in the real response of the published URL.
- Rate limit and cache active on the critical public path.
- Secrets outside the repo and outside CI/deploy logs.
- `npm audit` clean; build without security warnings.
- Rollback plan: how to switch the feature off quickly if it is abused.

## References
- OWASP Cheat Sheet Series (rate limiting, headers, input validation): https://cheatsheetseries.owasp.org/
- NIST CSF 2.0 (Protect, Detect, Respond functions): https://www.nist.gov/cyberframework
