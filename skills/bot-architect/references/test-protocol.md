# Test protocol (before / after)

> Derived from the `bot-architect` skill in this repo on 2026-11-26. This is a
> reconstruction, not the author's original file.

Read when validating a change. The point is to prove the change improved real
work, not that the new instructions read better.

## 1. Build the baseline first

Before changing anything, run **3–5 real tasks** from the role:

- one routine task the bot does often;
- one task with an edge case or missing input;
- one task that requires a tool (file, API, test, preview);
- one refusal or boundary case (the bot should stop and ask);
- optionally one task where the bot must hand off to another bot.

Record for each:

| Task | Prompt / source | Output artifact | Pass/fail | Evidence | Notes |
|---|---|---|---|---|---|

Evidence means a file, a table row, a commit, a preview URL, an API response
or an exit code — not the bot's own summary.

If there is no baseline, you cannot claim improvement. Say so.

## 2. Write the criteria before the run

For each task, write the criterion in advance:

- what must be present (sections, sources, files);
- what must not happen (invented facts, silent scope change, unapproved
  merge);
- how a reviewer decides pass or fail without interpretation.

A criterion added after seeing the output is not a test.

## 3. Change one thing

Apply the proposed change (profile, `AGENTS.md`, a skill, a routine, a
permission). Do not bundle unrelated changes: you will not know what caused a
difference.

Keep a backup (`AGENTS.md.bak-YYYYMMDD`) and note the diff.

## 4. Run the same tasks

Same prompts, same inputs, same tools. New tasks are allowed only as
additional cases, never as replacements.

Score each task against the criteria from step 2. Record:

| Task | Before (pass/fail) | After (pass/fail) | What changed | Evidence |
|---|---|---|---|---|

## 5. Check the side effects

- **Tools**: did the bot use the right tool, or did it start browsing or
  guessing?
- **Tone**: did the voice change unintentionally?
- **Context**: did the instructions become so long that the bot ignores parts?
- **Scope**: did the bot expand what it does without approval?
- **Cost/time**: did the run get much longer or more expensive?

## 6. Delegation: verify, do not trust

When the test run is delegated to another bot, the completion report is not
proof. Check the artifacts yourself:

- the rows the bot says it wrote — open the table;
- the files it cites — open them, check the path and the timestamp;
- the commits or diffs — `git status`, `git log`, `git diff`;
- the preview — open it, exercise the flow.

If any artifact is missing or does not match the report, the test is **not
passed**, regardless of the summary.

## 7. Decide and record

- **Improved**: after ≥ 3 tasks pass and no side effect is worse than the
  baseline. Keep the change.
- **Mixed**: some tasks better, some worse. Keep the change only behind a
  scope limit, or revert the part that caused the regression.
- **No effect / worse**: revert to the backup.

Record in `bot_audits`:

- date, bot, change (one line);
- before/after table;
- side effects;
- **what was not tested** and why;
- decision.

## 8. Minimum bar for a rewrite

Do not call an audit successful when:

- the baseline is missing;
- fewer than three real tasks ran;
- the only evidence is the bot's own report;
- untested parts are not named;
- the change was applied without a backup.
