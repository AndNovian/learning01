"""Minimal CLI for the learning workspace."""


def build_banner() -> str:
    """Return a concise description of the project intent."""
    return (
        "learning01: engineering sandbox\n"
        "- Build tiny projects\n"
        "- Test every iteration\n"
        "- Document what you learn"
    )


def main() -> None:
    """Run the CLI."""
    print(build_banner())


if __name__ == "__main__":
    main()
