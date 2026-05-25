#!/usr/bin/env python3
"""Create phased implementation tracking documents for a feature or bugfix."""

from __future__ import annotations

import argparse
from pathlib import Path


IMPLEMENTATION_TEMPLATE = """# {title}

## Objective

- Describe the user-facing goal.

## Scope

- In scope:
- Out of scope:

## Phases

### Phase 1: Discovery and design

- Goal:
- Expected files or systems:
- Validation:
- Review gate:

### Phase 2: Core implementation

- Goal:
- Expected files or systems:
- Validation:
- Review gate:

### Phase 3: Integration and cleanup

- Goal:
- Expected files or systems:
- Validation:
- Review gate:

### Phase 4: Verification and handoff

- Goal:
- Expected files or systems:
- Validation:
- Review gate:
"""


DETAILS_TEMPLATE = """# {title} Details

## Repository Context

- Relevant files:
- Existing patterns to follow:
- Constraints:

## Assumptions To Verify

- 

## Phase Notes

### Phase 1

- Detailed tasks:
- Findings:
- Tests:
- Review notes:
- Status:

### Phase 2

- Detailed tasks:
- Findings:
- Tests:
- Review notes:
- Status:

### Phase 3

- Detailed tasks:
- Findings:
- Tests:
- Review notes:
- Status:

### Phase 4

- Detailed tasks:
- Findings:
- Tests:
- Review notes:
- Status:

## Deferred Work

- 

## Final Confidence Check

- Confidence score:
- Likely code review callouts:
- Residual risks:
"""


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists. Re-run with --force to overwrite.")
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create implementation.md and implementation_details.md templates."
    )
    parser.add_argument("title", help="Feature or bugfix title used in document headings.")
    parser.add_argument(
        "--dir",
        default=".",
        help="Target directory for the generated files. Defaults to the current directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files.",
    )
    args = parser.parse_args()

    target_dir = Path(args.dir).resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    implementation_path = target_dir / "implementation.md"
    details_path = target_dir / "implementation_details.md"

    write_file(
        implementation_path,
        IMPLEMENTATION_TEMPLATE.format(title=args.title.strip()),
        args.force,
    )
    write_file(
        details_path,
        DETAILS_TEMPLATE.format(title=args.title.strip()),
        args.force,
    )

    print(f"Created {implementation_path}")
    print(f"Created {details_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
