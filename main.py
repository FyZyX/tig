from pathlib import Path


def project_structure(root, indent=''):
    root_path = Path(root).expanduser()

    if not root_path.is_dir():
        print(f"{root_path} is not a directory.")
        return

    for entry in sorted(root_path.iterdir(), key=lambda e: e.name):
        print(f"{indent}{entry.name}")
        if entry.is_dir():
            project_structure(entry, indent + '    ')


if __name__ == '__main__':
    codebase = "~/Projects/github/justin-time"
    project_structure(codebase)
