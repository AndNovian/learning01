# learning01

A practical **blank-canvas software engineering workspace**.

This repo is a creative lab for building tiny, useful tools with strong engineering habits.

## What’s new in this update

The Learning Lab CLI now includes:
- Goal status transitions (`todo`, `doing`, `done`).
- Reflection metrics with completion percent.
- Markdown snapshot export for weekly reviews.

## CLI commands

- `banner` — project intent snapshot.
- `init` — initialize a local workspace DB.
- `add-goal <title>` — add a goal to the backlog.
- `list-goals` — show tracked goals.
- `update-status <goal_id> <status>` — move goal between `todo|doing|done`.
- `reflect` — summarize progress.
- `export-markdown <output>` — generate a weekly snapshot markdown file.

## Quick start

```bash
# Initialize and add goals
PYTHONPATH=src python -m learning01.cli --db .learning01/goals.json init
PYTHONPATH=src python -m learning01.cli --db .learning01/goals.json add-goal "Build first prototype"
PYTHONPATH=src python -m learning01.cli --db .learning01/goals.json update-status 1 doing
PYTHONPATH=src python -m learning01.cli --db .learning01/goals.json list-goals
PYTHONPATH=src python -m learning01.cli --db .learning01/goals.json reflect

# Export weekly markdown summary
PYTHONPATH=src python -m learning01.cli --db .learning01/goals.json export-markdown .learning01/weekly.md

# Run tests
pytest -q
```

## Next creative engineering moves

1. Add due dates and priority levels.
2. Add a `complete` shortcut command.
3. Add CSV export.
4. Add CI + linting + type checks.
