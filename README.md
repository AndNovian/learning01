# learning01

A practical **blank-canvas software engineering workspace**.

Instead of decorative content, this repo now starts as a buildable foundation for iterative learning:
- one executable entry point,
- one test suite,
- one clear roadmap,
- and room to grow with real features.

## What I would build here

If this were my personal engineering sandbox, I would build a **Learning Lab CLI**:

- Track learning goals as small projects.
- Capture experiments and outcomes quickly.
- Keep strict iteration loops (plan → build → test → reflect).
- Evolve into a portfolio of tiny, high-quality utilities.

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
PYTHONPATH=src python -m learning01.cli
pytest -q
```

## Roadmap

### Phase 1 — Foundation (current)
- [x] Basic CLI entrypoint.
- [x] Smoke tests for output stability.
- [x] Defined project direction.

### Phase 2 — Core utility
- [ ] Add commands (`init`, `add-goal`, `list-goals`, `reflect`).
- [ ] Persist goals in a local JSON file.
- [ ] Add input validation + user-friendly errors.

### Phase 3 — Engineering quality
- [ ] Add linting + formatting automation.
- [ ] Add CI workflow for tests and style checks.
- [ ] Add typed interfaces and richer unit tests.

### Phase 4 — Portfolio polish
- [ ] Add examples of completed learning tracks.
- [ ] Generate a summary report from tracked goals.
- [ ] Publish a versioned release.

## Engineering principles for this repo

1. **Small, shippable increments** over big rewrites.
2. **Tests with every behavior change**.
3. **Readable defaults** over clever abstractions.
4. **Document decisions** so future-you moves faster.
