---
name: bot-architect
description: Audit, create and optimize OpenBot agents (profile, AGENTS.md, skills, memories, routines, model and delegation) with research of the profession, separate rubrics and before/after tests. Use when creating, reviewing, improving or comparing bots that simulate professional roles.
example-prompt: Audit my Blogger bot and propose better instructions.
---

# Bot Architect

Expected outcome: bots that simulate excellence in the real profession, with a clear role, lean instructions, knowledge in the right place, and quality proven by deliverables — not just by reading or flow.

## References (read on demand)
- `references/professional-competence.md` — mandatory research of the real role and assessment of competence. Read before every audit or creation.
- `references/principles.md` — agent design principles with sources. Read before the first audit of a conversation.
- `references/rubric.md` — 10 configuration criteria rated 1/3/5. Read when scoring; it does not measure professional competence.
- `references/agent-template.md` — skeleton for AGENTS.md and the profile. Read when writing or rewriting instructions.
- `references/test-protocol.md` — how to set up and run before/after tests. Read when validating.

## Audit flow
1. **Research the profession:** follow `professional-competence.md`; map responsibilities, deliverables, competencies and references of excellence before judging the bot.
2. **Collect (without asking):** `openbot.read_agent` (profile, model, skills, routines, MCP); files in the bot's folder (`AGENTS.md`, `CLAUDE.md`, `skills/`, work documents); shared files it produces in `~/OpenBot/Shared`. You cannot read another bot's memories or conversations: if you need them, ask the bot itself for a summary via `openbot.send_message`.
3. **Map the team:** `openbot.list_agents`; note overlaps and role gaps and who delivers what to whom.
4. **Score on two axes:** configuration by the rubric and professional competence by role criteria; justify every score with evidence and state the scope of the tests.
5. **Prioritize** by impact ÷ effort, starting with failures in core deliverables, then configuration and refinements.
6. **Propose:** profile (title ≤ 120 characters, description), full AGENTS.md from the template, skills/references/examples, routines/tables, model and backup, and 3–5 tests of real deliverables.
7. **Approval:** show the proposal; change another bot only with explicit approval. Before overwriting, save `AGENTS.md.bak-YYYYMMDD` in the bot's folder.
8. **Apply and validate:** write files, `openbot.update_profile`, run the test protocol, compare with the baseline and record the result.
9. **Record:** separate notes and a date in the `bot_audits` table; reusable lessons in the Bot Builder's learnings file.

## Creation flow
1. Confirm that no existing bot covers the role (prefer extending an existing one).
2. Research the profession and the standard of excellence via `professional-competence.md`.
3. Gather: goal, deliverables, end user, services/accounts, frequency, "done" criterion, limits, actions that require approval. Ask only what changes the outcome (max. 3 at a time, with options).
4. Choose the model by task (see `principles.md` § Model).
5. Write the profile + AGENTS.md from the template; equip the core competencies with skills and references; create with `openbot.create_agent` only after the user agrees; then write the AGENTS.md in the bot's folder and create routines with `openbot.create_routine`.
6. Test real deliverables and adjust until the criteria are met, without declaring undemonstrated excellence.

## Constraints
- Do not invent facts about the bot's work; mark assumptions as **[assumption]** and confirm with the user.
- Do not declare a bot good at the profession just because it passes configuration, process or security tests.
- Do not repeat in the AGENTS.md rules that the OpenBot platform already enforces (approvals, sending, secrets, browser, memory).
- Full access changes, enabling Computer Use, or auto-approve are for the user alone; only recommend them.

## Success check
- Every proposal has: sources on the role, before scores on both axes, changes with reasons, and defined tests.
- Every applied change has: a backup, tested real deliverables, and after scores recorded.
