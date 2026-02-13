# learning01

A practical **blank-canvas software engineering workspace**.

This is now a creative lab for building tiny, real tools with strong engineering habits.
Think of it as a place where ideas become shippable experiments in hours—not months.

## What I would build here

If this were my space, I’d build a **Learning Lab CLI** that helps me:
- capture goals,
- turn goals into small deliverables,
- and reflect on progress with data.

## Current capabilities

The CLI currently supports:
- `banner` — project intent snapshot.
- `init` — initialize a local workspace DB.
- `add-goal` — add a goal to the backlog.
- `list-goals` — show tracked goals.
- `reflect` — summarize progress.

## Initial project layout

```text
learning01/
├── README.md
├── pyproject.toml
├── src/
│   └── learning01/
│       ├── __init__.py
│       └── cli.py
└── tests/
    └── test_cli.py
```

## Quick start

```bash
# Show the project banner
PYTHONPATH=src python -m learning01.cli banner

# Use a local goals file
PYTHONPATH=src python -m learning01.cli --db .learning01/goals.json init
PYTHONPATH=src python -m learning01.cli --db .learning01/goals.json add-goal "Build first prototype"
PYTHONPATH=src python -m learning01.cli --db .learning01/goals.json list-goals
PYTHONPATH=src python -m learning01.cli --db .learning01/goals.json reflect

# Run tests
pytest -q
```

## Next creative engineering moves

1. Add status transitions (`todo` → `doing` → `done`).
2. Add deadlines and priority scoring.
3. Add markdown export for weekly review notes.
4. Add CI + linting + type checking.

## Engineering principles for this repo

1. **Small, shippable increments** over big rewrites.
2. **Tests with every behavior change**.
3. **Readable defaults** over clever abstractions.
4. **Document decisions** so future-you moves faster.
