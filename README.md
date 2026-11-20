# gavari-os

**The systems behind a small one-person AI practice.**

Gavari AI is a small one-person AI practice — the workshop where this work
was learned by shipping it for real businesses.
The work a small team would do — sourcing, outreach, audits, follow-up,
partner operations, reporting — runs on systems built and operated with AI
coding agents (Claude Code, Muse) working from skills, scheduled tasks,
and connectors.

This repository is the public blueprint: the architecture, one production
skill, the scoring and self-audit scripts, and the partner-program spec.
Client data, credentials, and live prospect lists are never in this repo.

## The systems

| System | What it does |
|---|---|
| **Lead Radar** | Scrapes public signals (permits, ads, hiring posts, social profiles) and ranks thousands of businesses. Every record carries the evidence for its score — nothing on the list is a guess. |
| **Audit Product** | Questions ChatGPT, Perplexity, and Gemini directly in their own interfaces, tests the business's front door for real, and produces a finished narrated video report + PDF in minutes. |
| **Voice Agents** | AI receptionists on real business phone lines: answer after hours, qualify the caller, book the appointment, trigger a missed-call text-back. Every agent is test-called live before it reaches a customer. |
| **Outreach Engine** | LinkedIn, Facebook, email, and voicemail running on schedules. It **audits itself every morning** and reports what actually sent — not what was supposed to send. A lane that didn't fire gets caught the same morning. |
| **Partner Program** | Referral partners earn 20% of referred revenue. Sourcing, onboarding, status tracking, and milestone pings run on the same machinery (see `partner-program/`). |
| **The Brain** | A private AI installed inside a client's business, trained on their real operation, that staff can talk to in plain language — answers come from the business's own data, with evidence attached. |

## Operating principles

1. **Evidence or it didn't happen.** Every claim a system makes — a lead's
   score, an audit finding, a sent message — links to the artifact that
   proves it.
2. **Systems report actuals, not intentions.** Dashboards read the send log,
   not the schedule.
3. **Humans approve what leaves the building.** Agents draft, prepare, and
   verify. A person approves external sends.
4. **Verify the way the customer experiences it.** Forms are test-submitted,
   agents are test-called, pages are opened on a phone before they are
   called done.

## Repo layout

- `docs/architecture.md` — how the pieces connect
- `skills/ai-visibility-audit/SKILL.md` — a production skill, as written for the agent that runs it
- `scripts/lead_scoring.py` — the Radar's scoring pass (public-signal version)
- `scripts/morning_send_audit.py` — the outreach engine's self-audit
- `partner-program/README.md` — the partner program operating spec

## Stack

Claude Code · Muse · MCP servers & connectors · skills · scheduled tasks ·
Apify (sourcing) · Bland AI & Telnyx (voice) · Cloudflare (hosting) ·
Greenhouse/Ashby/Lever are where the forms live, not the stack.

---

Built and run by **Gregory St Clair** — Miami, Florida.
Interactive resume: https://resume.gavariai.net
