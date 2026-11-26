# AGENTS.md and profile template

> Derived from the `bot-architect` skill in this repo on 2026-11-26. This is a
> reconstruction, not the author's original file. Adapt it; do not fill it with
> generalities.

Read when writing or rewriting instructions. Use it for a new bot and for an
audit rewrite. Keep the result short enough that the agent reads it every
turn.

## Profile

The profile is what other agents and the user see. Keep it under OpenBot's
limits.

- **Name (≤ 80):** function, no project prefix.
  Good: `Editor`, `Security Review`, `Support Triage`.
  Bad: `Acme Project Editor 2026`.
- **Title (≤ 120):** one line, what the bot owns.
  Example: `Reviews copy for accuracy, sources and voice before publishing`.
- **Description (≤ 2,000):** the operating contract in compact prose:
  - one job;
  - inputs it reads;
  - pipeline or steps;
  - output format;
  - hard boundaries;
  - voice.

Start the description with "You are <Role>." Follow the pattern used by the
marketplace agents: job, inputs, how you work, output, never, voice.

## AGENTS.md skeleton

```markdown
# <Role> — workspace rules

## Scope
- Repos / paths this bot owns:
- Files it may read:
- Files it may write:
- Systems it may call (GitHub, tracker, Sentry, CMS):
- Explicitly out of scope:

## Inputs
- Where the work arrives (issue, PR, channel message, shared folder):
- What must be read before acting:
- What to do when an input is missing:

## Workflow
1. <first step, with the check that starts it>
2. <second step>
3. <output step>

## Output contract
- Format (sections, table, JSON):
- Where it is written:
- What evidence must be attached:

## Approval gates
- Actions that need the owner's written OK in chat:
- Actions that are always forbidden:
- What to show before asking:

## Handoffs
- To <other bot>: input, output, done criterion.
- From <other bot>: what to verify before accepting the result.

## Routines
- <name>: <schedule>, <scope>, <no-update rule>.

## Voice
- <3–5 traits, one line each>.

## When blocked
- What to report, to whom, and what not to do while waiting.
```

## Filling rules

- **One rule per line.** If a line has two "and", split it.
- **Trigger + action.** "When a PR is opened, read the diff before commenting."
- **Name the tool.** "Read the PR with `gh pr diff`", not "review the PR".
- **No platform repetition.** Do not restate approvals, secrets, browser or
  memory rules that OpenBot already enforces; only state stricter rules.
- **No adjectives without a measure.** Replace "high quality" with a criterion
  a reviewer can check.
- **No project prefix in names.** Name by function; the workspace path already
  says the project.
- **Keep it current.** Every rule gets a date when it changes, and stale rules
  are removed rather than left as history.

## Rewrite procedure

1. Read the current profile and `AGENTS.md`; list every rule.
2. Mark each rule: keep, rewrite, move to a skill, move to a reference, delete.
3. Write the new version in the skeleton.
4. Save `AGENTS.md.bak-YYYYMMDD` before overwriting.
5. Run the test protocol (`test-protocol.md`) and compare with the baseline.
