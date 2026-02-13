from pathlib import Path

from learning01.cli import build_banner, run


def test_build_banner_contains_project_name() -> None:
    banner = build_banner()
    assert "learning01" in banner


def test_build_banner_has_three_focus_lines() -> None:
    banner = build_banner().splitlines()
    assert len(banner) == 4


def test_init_creates_db_file(tmp_path: Path) -> None:
    db = tmp_path / "goals.json"
    output = run(["--db", str(db), "init"])

    assert db.exists()
    assert "Initialized learning workspace" in output


def test_add_and_list_goals(tmp_path: Path) -> None:
    db = tmp_path / "goals.json"

    run(["--db", str(db), "init"])
    add_output = run(["--db", str(db), "add-goal", "Ship tiny feature"])
    list_output = run(["--db", str(db), "list-goals"])

    assert "Added goal #1" in add_output
    assert "[todo] Ship tiny feature" in list_output


def test_reflect_shows_counts(tmp_path: Path) -> None:
    db = tmp_path / "goals.json"

    run(["--db", str(db), "init"])
    run(["--db", str(db), "add-goal", "Write tests"])
    reflection = run(["--db", str(db), "reflect"])

    assert "Total goals: 1" in reflection
    assert "Done: 0" in reflection
    assert "Todo: 1" in reflection
