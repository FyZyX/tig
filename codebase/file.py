import pathlib

import llm.prompt
import llm.query


def parse_gitignore(gitignore_path):
    excludes = []
    with open(gitignore_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            excludes.append(line)
    return excludes


def chunk_file(path: pathlib.Path):
    system_prompt = llm.prompt.load_prompt("code-chunker", system_prompt=True)
    response = llm.query.get_json_completion(
        system_prompt=system_prompt,
        message="",
    )
    return system_prompt


if __name__ == '__main__':
    print(chunk_file(""))
