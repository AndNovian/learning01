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


def test_update_status_and_reflect_counts(tmp_path: Path) -> None:
    db = tmp_path / "goals.json"

    run(["--db", str(db), "init"])
    run(["--db", str(db), "add-goal", "Write tests"])
    update_output = run(["--db", str(db), "update-status", "1", "done"])
    reflection = run(["--db", str(db), "reflect"])

    assert "[todo] -> [done]" in update_output
    assert "Total goals: 1" in reflection
    assert "Done: 1" in reflection
    assert "Doing: 0" in reflection
    assert "Todo: 0" in reflection
    assert "Completion: 100%" in reflection


def test_update_status_rejects_bad_id_and_status(tmp_path: Path) -> None:
    db = tmp_path / "goals.json"

    run(["--db", str(db), "init"])
    run(["--db", str(db), "add-goal", "First goal"])

    bad_id = run(["--db", str(db), "update-status", "9", "done"])
    bad_status = run(["--db", str(db), "update-status", "1", "blocked"])

    assert "Invalid goal id" in bad_id
    assert "Invalid status 'blocked'" in bad_status


def test_export_markdown_generates_snapshot(tmp_path: Path) -> None:
    db = tmp_path / "goals.json"
    out = tmp_path / "snapshot.md"

    run(["--db", str(db), "init"])
    run(["--db", str(db), "add-goal", "Build MVP"])
    run(["--db", str(db), "update-status", "1", "doing"])

    export_output = run(["--db", str(db), "export-markdown", str(out)])
    content = out.read_text()

    assert out.exists()
    assert "Exported markdown snapshot" in export_output
    assert "# learning01 Weekly Snapshot" in content
    assert "**[doing]** Build MVP" in content
