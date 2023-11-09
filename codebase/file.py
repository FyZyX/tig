import json
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


def read_lines(path: pathlib.Path):
    with open(path, "r") as file:
        lines = file.readlines()
    return lines


def display_code_file(lines: list[str]):
    total_lines = len(lines)
    max_padding = len(str(total_lines))

    source_code = ""
    for line_number, line in enumerate(lines, 1):
        source_code += f"{line_number:>{max_padding}} | {line}"

    return source_code


async def chunk_file(path: pathlib.Path):
    lines = read_lines(path)
    code_file = display_code_file(lines)
    print(code_file)

    system_prompt = llm.prompt.load_prompt("code-chunker", system_prompt=True)
    response = await llm.query.get_json_completion(
        system_prompt=system_prompt,
        message=code_file,
    )
    print(response)
    chunks = json.loads(response)["chunks"]
    code_chunks = []
    print("-" * 80)
    for chunk in chunks:
        # line numbers start at 1, not 0
        start = chunk["start"] - 1
        end = chunk["end"]
        chunk_lines = lines[start:end]
        code_chunk = "".join(chunk_lines)
        print(code_chunk)
        print("-" * 80)
        code_chunks.append(code_chunk)
    return code_chunks
