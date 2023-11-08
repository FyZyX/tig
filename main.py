from pathlib import Path

from analyze import project


def main():
    codebase = Path("~/Projects/github/justin-time").expanduser()
    if not codebase.is_dir():
        print(f"{codebase} is not a directory.")
        return

    excludes = project.exclusion_patterns(codebase)

    project.structure(
        codebase,
        depth=2,
        excludes=excludes,
    )


if __name__ == '__main__':
    main()
