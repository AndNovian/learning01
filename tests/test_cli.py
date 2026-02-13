from learning01.cli import build_banner


def test_build_banner_contains_project_name() -> None:
    banner = build_banner()
    assert "learning01" in banner


def test_build_banner_has_three_focus_lines() -> None:
    banner = build_banner().splitlines()
    assert len(banner) == 4
