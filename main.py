from pathlib import Path
import fnmatch


def parse_gitignore(gitignore_path):
    excludes = []
    with open(gitignore_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            excludes.append(line)
    return excludes


def should_exclude(entry: Path, excludes: list[str]) -> bool:
    return any(fnmatch.fnmatch(entry.name, pattern) for pattern in excludes)


def project_structure(
        path: Path,
        indent: str = "",
        depth: int | None = None,
        excludes: list[str] = None,
):
    if depth is not None:
        if depth <= 0:
            return
        depth -= 1

    excludes = excludes or []
    for entry in sorted(path.iterdir(), key=lambda e: e.name):
        if should_exclude(entry, excludes):
            continue

        print(f"{indent}{entry.name}")
        if entry.is_dir():
            project_structure(entry, indent + "\t", depth, excludes)


def main():
    codebase = Path("~/Projects/github/justin-time").expanduser()
    if not codebase.is_dir():
        print(f"{codebase} is not a directory.")
        return

    excludes = ["*.git", "__pycache__", "*.pyc", ".idea", "venv", ".env*"]

    gitignore_path = codebase / ".gitignore"
    if gitignore_path.is_file():
        ignored = parse_gitignore(gitignore_path)
        excludes.extend(ignored)

    project_structure(codebase, depth=2, excludes=excludes)


if __name__ == '__main__':
    main()
