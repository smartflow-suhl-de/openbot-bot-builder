---
name: astro-delivery
description: Implement and validate changes in Astro sites with diagnosis, minimal scope, build and preview. Use to fix bugs, change components/pages or prepare a delivery in an Astro project.
example-prompt: Implement this spec in the Astro site and validate the result before delivering.
---

# Astro delivery

Outcome: the smallest change that meets the criteria, with evidence of build and behavior. Read the project's real scripts before running commands.

## 1. Turn the request into acceptance
- List what must work and what must not change.
- If the spec is ambiguous, state the simplest interpretation and its assumptions.
- Locate affected pages, layouts, components, styles and content before editing.

## 2. Diagnose bugs
1. Reproduce with the given command or page.
2. Keep the message and the relevant file/line.
3. Identify whether the cause is content (MDX), component, style, configuration or dependency.
4. Fix the cause, not just the symptom; if it is editorial, return it to the owner with evidence.

## 3. Implement
- Make the smallest change consistent with existing patterns.
- Do not add a dependency without a demonstrated need.
- Preserve frontmatter, URLs and public components where possible.
- Review the diff to remove accidental changes.

## 4. Validate
1. Run the real build, usually `npm run build` if that script exists.
2. Open the preview and exercise the affected flow, not just check that the page opens.
3. Check desktop and mobile, interactive states, contrast and layout changes when applicable.
4. If the project has tests, run them; a build does not replace a behavior test.
5. Deliver changed files, commands run, observed evidence and open items.

## 5. Publication
- Deploy, hosting changes and irreversible actions follow the approvals in AGENTS.md.
- After an authorized deploy, verify the published URL and production behavior.

## Check
Do not declare done if the build was not run, the preview was not observed, or a criterion still lacks evidence. State exactly what was validated and what was not.
