import pathlib

PROMPTS_PATH = pathlib.Path("prompts")


def load_prompt(name, system_prompt=False):
    if system_prompt:
        name = f"{name}-system-prompt"

    path = PROMPTS_PATH / f"{name}.md"
    with open(path) as file:
        prompt = file.read()

    return prompt
