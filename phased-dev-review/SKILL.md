---
name: phased-dev-review
description: Drive phased feature and bug delivery with explicit planning, developer/reviewer handoffs, phase gates, and end-of-task confidence checks. Use when Codex should work in discrete phases, maintain `implementation.md` and `implementation_details.md`, pause after each phase for review, apply a QA checklist, or simulate a developer-agent plus reviewer-agent workflow.
---

# Phased Dev Review

Use this skill to turn a large feature or risky bugfix into a controlled loop:

- plan the work in phases
- track progress in `implementation.md` and `implementation_details.md`
- implement one phase at a time
- stop after each phase for review
- run a structured QA pass
- self-review before moving on
- finish with an honest confidence and code-review-risk assessment

## Quick Start

1. If the docs do not exist yet, initialize them with `scripts/init_phase_docs.py`.
2. Write a short, human-readable plan in `implementation.md`.
3. Write granular notes, assumptions, edge cases, and review findings in `implementation_details.md`.
4. Implement only the current phase.
5. Stop and review before starting the next phase.
6. Repeat until complete.
7. End with a confidence check and expected code-review callouts.

Read [references/qa-checklist.md](references/qa-checklist.md) when preparing or performing a review.
Read [references/prompts.md](references/prompts.md) when you want ready-to-use prompt patterns.

## Workflow

### 1. Build the plan first

Create or update two files:

- `implementation.md`
  Keep this short, readable, and phase-oriented. It is the human-friendly view.
- `implementation_details.md`
  Store detailed notes for Codex: file inventory, assumptions, open questions, edge cases, test plan, review notes, and follow-up items.

Keep both files aligned. When the detailed plan changes materially, reflect the high-level version too.

### 2. Define phases with real gates

Prefer 3-7 phases. Each phase should have:

- a goal
- the files or systems likely to change
- tests or verification for that phase
- an explicit stop point for review

Do not start implementation before the phase boundaries are clear enough that another Codex instance could review phase-by-phase.

### 3. Run the developer/reviewer loop

If the user explicitly wants two agents, use a developer/reviewer split:

- developer:
  implement only the current phase, update docs, stop at the gate
- reviewer:
  review only the completed phase, focusing on major and critical issues first

If separate agents are not available, simulate the same loop yourself:

1. implement the phase
2. switch into review mode
3. check against the QA checklist
4. record findings in `implementation_details.md`
5. fix issues before advancing unless the user asks to defer them

### 4. Review every phase with a checklist

During review, prioritize:

- functionality correctness
- completeness of the phase
- consistency with the existing codebase
- clarity and unnecessary complexity
- guesswork or unverified assumptions
- documentation accuracy
- test coverage and missing edge cases
- anything likely to get flagged in code review

Use [references/qa-checklist.md](references/qa-checklist.md) as the default checklist. Trim it when only a subset is relevant.

### 5. Self-review even after reviewer feedback

Do not skip self-review. Before marking a phase done:

- re-read the diff
- look for obvious simplifications
- verify assumptions against actual code or docs
- check whether tests prove the intended behavior
- update both implementation docs if reality drifted from the plan

### 6. End with an honesty pass

At the end of the whole task, answer at least one of these:

- "On a scale of 1 to 10, how confident are you that this is complete and free of important bugs?"
- "What issues are most likely to be called out during code review?"
- "Which parts of the implementation still rely on assumptions or weak validation?"

Be candid. The point is to surface residual risk, not to sound certain.

## Documentation Rules

- Keep `implementation.md` concise and phase-based.
- Keep `implementation_details.md` granular and current.
- Record major assumptions explicitly.
- Record deferred work explicitly.
- Record review findings with status such as `open`, `fixed`, or `accepted risk`.

## Good Defaults

- Prefer smaller phases when the codebase is unfamiliar.
- Prefer a review stop after any schema, API, auth, or migration change.
- Prefer fixing major review findings before moving on.
- Prefer updating the docs during the work, not at the end.
- Prefer honest uncertainty over silent guessing.

## User Decision Prompts

When a question to the user is necessary, do not ask it in an open-ended way by default.

- Propose 2-4 concrete options that fit the current project and phase scope.
- Put the recommended option first.
- Briefly explain the tradeoff of each option in project terms.
- Invite the user to choose one of the proposed options or explicitly choose another path.
- Use this especially for scope cuts, sequencing decisions, implementation strategies, validation depth, and deferrals between phases.

## Example Trigger Phrases

These are examples of requests that should use this skill:

- "Plan and implement this feature in phases."
- "Create implementation docs before coding."
- "Work like a developer and reviewer pair."
- "Stop after each phase so we can review."
- "Use a QA checklist while coding this bugfix."
- "Track the plan in `implementation.md` and `implementation_details.md`."
