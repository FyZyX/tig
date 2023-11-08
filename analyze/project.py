from pathlib import Path
import fnmatch

_DEFAULT_EXCLUDES = [
    "*.git",
    "__pycache__",
    "*.pyc",
    ".idea",
    "venv",
    ".env*",
]


def _parse_gitignore(gitignore_path):
    excludes = []
    with open(gitignore_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            excludes.append(line)
    return excludes


def exclusion_patterns(codebase_root: Path):
    gitignore_path = codebase_root / ".gitignore"
    if not gitignore_path.is_file():
        return
    ignored = _parse_gitignore(gitignore_path)
    _DEFAULT_EXCLUDES.extend(ignored)
    return _DEFAULT_EXCLUDES


def _should_exclude(entry: Path, excludes: list[str]) -> bool:
    return any(fnmatch.fnmatch(entry.name, pattern) for pattern in excludes)


def structure(
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
        if _should_exclude(entry, excludes):
            continue

        print(f"{indent}{entry.name}")
        if entry.is_dir():
            structure(entry, indent + "\t", depth, excludes)
