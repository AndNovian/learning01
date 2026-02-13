"""Learning Lab CLI for small, testable engineering iterations."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_DB = Path(".learning01/goals.json")


@dataclass
class Goal:
    title: str
    status: str
    created_at: str


def build_banner() -> str:
    """Return a concise description of the project intent."""
    return (
        "learning01: engineering sandbox\n"
        "- Build tiny projects\n"
        "- Test every iteration\n"
        "- Document what you learn"
    )


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_goals(db_path: Path) -> list[dict[str, Any]]:
    """Load goals from disk, returning an empty list if uninitialized."""
    if not db_path.exists():
        return []
    return json.loads(db_path.read_text())


def save_goals(db_path: Path, goals: list[dict[str, Any]]) -> None:
    """Persist goals to disk, creating parent directories as needed."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db_path.write_text(json.dumps(goals, indent=2) + "\n")


def cmd_init(db_path: Path) -> str:
    if db_path.exists():
        return f"Workspace already initialized at {db_path}"
    save_goals(db_path, [])
    return f"Initialized learning workspace at {db_path}"


def cmd_add_goal(db_path: Path, title: str) -> str:
    goals = load_goals(db_path)
    new_goal = Goal(title=title, status="todo", created_at=_now_iso())
    goals.append(asdict(new_goal))
    save_goals(db_path, goals)
    return f"Added goal #{len(goals)}: {title}"


def cmd_list_goals(db_path: Path) -> str:
    goals = load_goals(db_path)
    if not goals:
        return "No goals yet. Add one with: add-goal \"your goal\""

    lines = ["Learning goals:"]
    for idx, goal in enumerate(goals, start=1):
        lines.append(f"{idx}. [{goal['status']}] {goal['title']}")
    return "\n".join(lines)


def cmd_reflect(db_path: Path) -> str:
    goals = load_goals(db_path)
    if not goals:
        return "Reflection: No goals yet. Start by adding your first goal."

    total = len(goals)
    done = sum(1 for g in goals if g["status"] == "done")
    todo = total - done
    return (
        "Reflection:\n"
        f"- Total goals: {total}\n"
        f"- Done: {done}\n"
        f"- Todo: {todo}\n"
        "- Next step: complete one small goal today."
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="learning01 Learning Lab CLI")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="Path to goals JSON")

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("banner", help="Show project banner")
    subparsers.add_parser("init", help="Initialize learning workspace")

    add_goal_parser = subparsers.add_parser("add-goal", help="Add a new learning goal")
    add_goal_parser.add_argument("title", help="Goal title")

    subparsers.add_parser("list-goals", help="List current goals")
    subparsers.add_parser("reflect", help="Show simple progress reflection")

    return parser.parse_args(argv)


def run(argv: list[str] | None = None) -> str:
    args = parse_args(argv)

    if args.command is None or args.command == "banner":
        return build_banner()
    if args.command == "init":
        return cmd_init(args.db)
    if args.command == "add-goal":
        return cmd_add_goal(args.db, args.title)
    if args.command == "list-goals":
        return cmd_list_goals(args.db)
    if args.command == "reflect":
        return cmd_reflect(args.db)

    raise ValueError(f"Unknown command: {args.command}")


def main() -> None:
    """Run the CLI."""
    print(run())


if __name__ == "__main__":
    main()
