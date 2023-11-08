from pathlib import Path

import codebase.project


def main():
    path = Path("~/Projects/github/justin-time").expanduser()
    if not path.is_dir():
        print(f"{codebase} is not a directory.")
        return

    project = codebase.project.Project(path)

    project.structure(depth=2)


if __name__ == '__main__':
    main()
