import asyncio
from pathlib import Path

import codebase.file
import codebase.project


async def test():
    code_file = await codebase.file.chunk_file(__file__)
    print(code_file)


def main():
    path = Path("~/Projects/github/justin-time").expanduser()
    if not path.is_dir():
        print(f"{codebase} is not a directory.")
        return

    project = codebase.project.Project(path)

    project.structure(depth=2)


if __name__ == '__main__':
    asyncio.run(test())
