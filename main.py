from pathlib import Path
import fnmatch


def project_structure(root, indent='', depth=1, excludes=None):
    root_path = Path(root).expanduser()

    if not root_path.is_dir():
        print(f"{root_path} is not a directory.")
        return

    if depth <= 0:
        return

    excludes = excludes or []

    depth -= 1

    for entry in sorted(root_path.iterdir(), key=lambda e: e.name):
        if any(fnmatch.fnmatch(entry.name, pattern) for pattern in excludes):
            continue

        print(f"{indent}{entry.name}")
        if entry.is_dir():
            project_structure(entry, indent + '    ', depth, excludes)


if __name__ == '__main__':
    codebase = "~/Projects/github/justin-time"
    excludes = ["*.git", "__pycache__", "*.pyc", ".idea", "venv"]
    project_structure(codebase, depth=2, excludes=excludes)
