# Bot builder for OpenBot

Importable agent package for a self-hosted OpenBot server: the agent
description and ten skills as one zip that OpenBot reads under
**Server settings → Import**.

One agent, one purpose: design, audit and improve OpenBot agents — profile,
`AGENTS.md`, skills, memories, routines and delegation. It delivers a
diagnosis, rewritten instructions and validation tests; it changes other bots
only with the user's explicit approval.

## Origin

The agent was published as a public share page and taken over from there on
2026-11-26:

- Share page: <https://openbot.run/agents/q0mAYpIXHmcGpR6oIw1rcw>
- Display name: **Bot builder** (creator: "OpenBot user", no profile name)
- Template scope: 10 embedded skills, no routines

The template was entirely in Portuguese. This repo is the **English
version**: description, skill descriptions, example prompts and all skill
texts were translated. Structure, numbering, commands, paths and rules stay
unchanged; only the language and the names of the referenced helper files
were translated (e.g. `competencia-profissional.md` →
`professional-competence.md`).

Portuguese originals (intermediate copy, not part of the repo):
`/tmp/opencode/a2/` — can be pulled again from the share page at any time.

Rights to the text belong to the author; the OpenBot app itself is under
PolyForm Noncommercial 1.0.0. Do not present it as your own product.

Not part of the share page and therefore not here: the creator's private
system prompt, model settings, conversations and workspace files.

## What is inside

| Path | Content |
|---|---|
| `AGENT.md` | the translated agent description (source for `description` in the import) |
| `skills/bot-architect/` | audit and creation flow for bots: research of the profession, two scoring axes, before/after tests |
| `skills/product-priority-flow/` | plan short cycles, track deliverables with owner and verifiable criteria, status reports |
| `skills/sdd-product-requirements/` | requirements for Spec-Driven Development: scope, `REQ`/`NFR`/`AC`, acceptance criteria, traceability |
| `skills/sdd-ux-specification/` | turn SDD requirements into implementable UI/UX specs, UX acceptance, review |
| `skills/sdd-technical-delivery/` | technical plan, traceability matrix, implementation in verifiable slices, validation |
| `skills/ui-spec-review/` | write UI/UX specs and review the implementation against the spec |
| `skills/astro-delivery/` | changes to Astro sites: diagnosis, minimal change, build, preview |
| `skills/security-first-dev/` | security-first for public surfaces: abuse/DDoS, headers, secrets, dependencies |
| `skills/social-content-calendar/` | turn articles and ideas into post drafts and a per-network editorial calendar |
| `skills/voice-calibration/` | build and apply a voice/tone guide from the user's real texts |
| `import/openbot-import.json` | generated manifest of the import package |
| `dist/openbot-bot-builder.zip` | finished import package |
| `scripts/build-import.py` | builds manifest and zip from the files above, checks the format limits |
| `scripts/check-import.py` | checks a finished zip against the import rules |

The source of truth is `AGENT.md` and `skills/`. The manifest and the zip are
built from them and are not maintained by hand.

## Reference files

`skills/bot-architect/` references five helper files under `references/`:

| File | Content |
|---|---|
| `references/professional-competence.md` | research the real profession, competency matrix, scoring competence (0–2) |
| `references/principles.md` | 12 agent design principles with sources |
| `references/rubric.md` | 10 configuration criteria scored 1/3/5, separate from competence |
| `references/agent-template.md` | profile rules and AGENTS.md skeleton, rewrite procedure |
| `references/test-protocol.md` | before/after tests on real deliverables, delegation checks |

These files are **not part of the share page**. They were reconstructed from
the skill text on 2026-11-26 and are marked as such at the top of each file.
The author's originals may score differently; if you get them, replace these
files and note the change.

## Download link

- **Landing page:** `docs/index.html` (ready for GitHub Pages or any static host; GitHub Pages is not available for this private repo on the current plan)
- **Latest release:** <https://github.com/smartflow-suhl-de/openbot-bot-builder/releases/latest>
- **Direct zip:** <https://github.com/smartflow-suhl-de/openbot-bot-builder/releases/latest/download/openbot-bot-builder.zip>

A tag `v*` runs `.github/workflows/release.yml`, builds the zip and attaches
it to the release, so the direct link always points at the newest build. The
repo is private, so the link only works for accounts with access. OpenBot has
no link that installs a zip from a URL: the download plus the three clicks in
**Server settings → Import** stay necessary.

## Building

```bash
./scripts/build-import.sh
./scripts/check-import.py
```

Result: `dist/openbot-bot-builder.zip` with `openbot-import.json` and
`agents/bot-builder/skills/…` at the root, as OpenBot expects.

## Installing in OpenBot

The import runs on the OpenBot machine; nothing is uploaded.

1. Copy `dist/openbot-bot-builder.zip` to the machine that runs OpenBot
   (or download the file there).
2. In OpenBot open **Server settings → Import**.
3. Choose **Select file…**, pick the zip and import the shown agent
   "Bot builder".
4. OpenBot creates a copy: instructions and the ten skills. Conversations,
   memories, model, provider and workspace files of the creator are not taken
   over; the template ships no routines.

A second import of the same file does not overwrite the existing copy but
creates another one (or renames colliding skills). Decide beforehand whether
the old copy should be deleted.

### After the import

1. **Set model and provider.** New agents otherwise tend to start on `codex`;
   without a ChatGPT login the first turn fails. To start, choose
   `provider: opencode` with a model present in the catalog and a suitable
   reasoning effort, plus a backup model.
2. **Grant access, but only what is needed.** The agent reads bots via
   `openbot.read_agent`/`list_agents` and writes only with approval. For
   audits it needs access to the agents' folders; GitHub, trackers or Sentry
   only if it should also check their projects.
3. **Run the first conversation.** A real task ("Audit bot X") is the best
   test: the agent should read first, then score, then deliver a proposal —
   and ask before changing another bot.
4. **Test small.** First audit an existing bot, check the backup
   (`AGENTS.md.bak-YYYYMMDD`), then apply one change and run the before/after
   test.
5. **Confirm the limits.** Full access, Computer Use and auto-approve stay
   with the user; the agent may only recommend them.

### Installing without the zip

1. Clone the repo into the agent's workspace, e.g. to
   `Agents/<name>/openbot-bot-builder`.
2. Use `AGENT.md` as the agent description (text from "You are Bot builder
   …"; max. 2,000 characters).
3. Ask the agent to register the ten folders from `skills/` with its local
   skill tools (`create_skill`). Do not overwrite the installed copies under
   `.agents/skills` by hand.

## Maintenance

- Change a skill text: edit `skills/<name>/SKILL.md` (the frontmatter `name`
  must match the folder name), then run `./scripts/build-import.sh` and
  `./scripts/check-import.py`.
- Roll out a new version: rebuild, import, then test again. No untested
  update into a running channel.
- Translation: technical terms (Spec-Driven Development, owner, handoff,
  fail-closed, rate limiting) stay English; do not add content that is not in
  the template.

Format limits that the script checks: agent description 2,000 characters,
name 80, title 120, 32 skills per agent, 64 routines, 80 characters per
routine name, 200 files per skill folder, no `.env` files, keys or nested
archives in the zip.
