from pathlib import Path
import fnmatch


def project_structure(
        path: Path,
        indent: str = '',
        depth: int = 1,
        excludes: list[str] = None,
):
    if depth <= 0:
        return

    excludes = excludes or []

    depth -= 1

    for entry in sorted(path.iterdir(), key=lambda e: e.name):
        if any(fnmatch.fnmatch(entry.name, pattern) for pattern in excludes):
            continue

        print(f"{indent}{entry.name}")
        if entry.is_dir():
            project_structure(entry, indent + '    ', depth, excludes)


def main():
    codebase = Path("~/Projects/github/justin-time").expanduser()
    if not codebase.is_dir():
        print(f"{codebase} is not a directory.")
        return
    excludes = ["*.git", "__pycache__", "*.pyc", ".idea", "venv"]
    project_structure(codebase, depth=2, excludes=excludes)


if __name__ == '__main__':
    main()
