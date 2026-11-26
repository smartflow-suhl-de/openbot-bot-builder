# Agent design principles

> Derived from the `bot-architect` skill in this repo on 2026-11-26. This is a
> reconstruction, not the author's original file. Sources are listed so every
> principle can be checked and dated.

Read before the first audit of a conversation, and again before rewriting a
profile.

## 1. One agent, one job

A bot should own a single outcome. Two jobs in one instruction set means
context switching, diluted criteria and no clear owner for a failure. If a
project needs several functions, create several bots (Lead, Dev, Security) and
connect them through handoffs.

Source: role design in O*NET/ESCO; Anthropic, *Building effective agents*
(<https://www.anthropic.com/engineering/building-effective-agents>).

## 2. Instructions are policy, not prose

Write rules the agent can follow and a reviewer can check:

- one sentence per rule, imperative;
- a trigger ("when a PR exists") and an action ("read the diff first");
- an output contract (sections, table, JSON);
- an explicit boundary ("never merge without written approval").

Remove marketing language, origin stories and duplicated platform rules.
OpenBot already enforces approvals, sending, secrets and browser limits; repeat
them only where this agent's behaviour must be stricter.

## 3. Knowledge goes where it is used

- **Profile** (name, title, description): who the bot is, in ≤ 2,000
  characters.
- **AGENTS.md**: durable rules for this workspace, repos, paths, approvals.
- **Skills**: a procedure for one kind of task, loaded on demand.
- **References**: background, rubrics, templates, sources.
- **Memory**: facts learned from the user, never procedures.
- **Routines**: time-based or event-based triggers with a no-update rule.

A procedure copied into three skills will drift. Keep one copy and link to it.

## 4. Least privilege

Give the bot the access its job needs and no more:

- file access limited to its workspace and the shared folder it really uses;
- MCP servers granted per agent, credentials with the smallest scope;
- `computerUse`, full access and auto-approve are the user's decision;
- a read-only stage (spec, review, RCA) must be configured read-only, not just
  asked to behave.

Source: OWASP LLM Top 10, *Excessive Agency*
(<https://owasp.org/www-project-top-10-for-large-language-model-applications/>);
NIST CSF 2.0, Protect function (<https://www.nist.gov/cyberframework>).

## 5. Human gates on irreversible actions

Merge, deploy, publish, send, delete and spend are gated by an explicit
written approval from the owner in the conversation. An approval from another
agent does not count. The bot prepares, shows the evidence, and waits.

Source: incident-response practice; NIST CSF 2.0 (Respond).

## 6. Evidence over claims

Every "done" needs an artifact: a file, a commit, a table row, a preview, an
API response, a test exit code. A completion report is a claim; the reviewer
checks the artifact. This applies to the bot and to anyone auditing the bot.

## 7. Deterministic tools before prose

If a shell command or API call can answer the question, the bot should call it
instead of reasoning about it. Prefer `git diff` over "I think the change
touches…", `npm test` over "the tests should pass".

## 8. Context is a budget

Long instructions crowd out the task. Keep the profile short, load skills on
demand, put reference material in files, and summarize long tool output before
reasoning over it.

Source: Anthropic, *Building effective agents*; HumanLayer, *12-Factor Agents*
(<https://github.com/humanlayer/12-factor-agents>).

## 9. Model fits the task

Match model and reasoning effort to the stage: fast models for triage and
routine work, stronger reasoning for specification and review, a different
model family for review than for implementation to avoid blind spots. Always
validate a model ID against the live catalog; never invent one.

Source: OpenAI, *A practical guide to building agents*
(<https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf>).

## 10. Test on real deliverables

A bot is only as good as its last real output. Before/after tests use real
tasks from the role, not synthetic prompts, and are scored against criteria
written down in advance. Declare what was not tested.

## 11. Name by function

Bots are named and titled by what they do (Lead, Dev, Security, Editor), not
by project prefix. A prefix does not inform the function, breaks reuse and
makes a second project create a near-duplicate bot.

## 12. Templates must be proven, not promised

A lead/orchestrator template is only worth recommending when its real state is
verified: `AGENTS.md` exists and fits, routines are paused or active on
purpose, the required CLIs are installed. An unconfigured template is a
promise, not a capability.
