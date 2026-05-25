# Prompt Patterns

Adapt these prompts to the specific repository and phase.

## Initial Planning Prompt

Create `implementation.md` and `implementation_details.md` for this feature or bugfix. Build a multi-phase plan with clear phase goals, stop points, expected files to touch, validation per phase, and major risks or assumptions.

## Developer Prompt

Implement only phase N from `implementation.md`. Update `implementation_details.md` with decisions, assumptions, tests, and any deviations from plan. Stop after phase N is complete and ready for review.

## Reviewer Prompt

Review the developer's implementation for phase N for major or critical issues. Use the QA checklist in `references/qa-checklist.md`. Focus on correctness, completeness, unverified assumptions, documentation accuracy, and testing gaps. Report findings first.

## Self-Review Prompt

Review the just-completed phase as if you were the strictest reviewer on the team. What is overcomplicated, under-tested, or based on assumptions? What should be fixed before phase N+1?

## Final Honesty Prompt

If you had to be completely honest, on a scale of 1 to 10 how confident are you that this feature or bugfix is complete and free of important bugs? What would you expect to be called out during code review?
