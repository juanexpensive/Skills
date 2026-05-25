# QA Checklist

Use this checklist for phase reviews. Select only the relevant items for the task.

## Core Checks

- Functionality: Is the implementation functionally correct? Does it handle the main path, edge cases, and failure cases correctly?
- Completeness: Is the stated phase actually complete?
- Consistency: Does the code and documentation match the surrounding project style and patterns? Does anything feel hacky?
- Clarity: Is anything unnecessarily complex, redundant, or missing an obvious reusable abstraction?
- Guesswork: Is the implementation free of unverified assumptions such as guessed schema details, guessed API names, or invented file paths?
- Documentation: Do `implementation.md`, `implementation_details.md`, inline comments, and user-facing docs match the code?
- Testing: Do tests cover primary flows, edge cases, and likely failure modes?
- Other: Does anything else seem off that would not naturally fit the categories above?
- Review Risk: What is most likely to get flagged during code review?

## Severity Guidance

- Critical: Data loss, security issues, broken deploys, or behavior that invalidates the phase.
- Major: A correctness, completeness, or maintainability issue that should usually be fixed before the next phase.
- Minor: A polish or refactor item that can be deferred if documented.

## Suggested Review Output

Prefer this structure:

1. Findings ordered by severity
2. Open questions or assumptions
3. Recommended fixes before the next phase
4. Residual risks if moving forward anyway
