from pathlib import Path


def project_structure(root, indent='', depth=1):
    root_path = Path(root).expanduser()

    if not root_path.is_dir():
        print(f"{root_path} is not a directory.")
        return

    if depth <= 0:
        return

    depth -= 1

    for entry in sorted(root_path.iterdir(), key=lambda e: e.name):
        print(f"{indent}{entry.name}")
        if entry.is_dir():
            project_structure(entry, indent + '    ', depth)


if __name__ == '__main__':
    codebase = "~/Projects/github/justin-time"
    # Set the depth to whatever level of recursion you want, e.g., 2 levels deep
    project_structure(codebase, depth=2)
