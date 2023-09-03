import pathlib

PROMPTS_DIR = pathlib.Path(__file__).parent / "prompts"
PERSONAS_DIR = PROMPTS_DIR / pathlib.Path("personas")


def available_personas():
    path = PERSONAS_DIR
    return [f.stem for f in path.iterdir() if f.suffix == ".md"]


def load_persona(name):
    path = PERSONAS_DIR / f"{name}.md"

    if not path.exists():
        raise FileNotFoundError(f"Persona '{name}' does not exist.")

    with path.open() as file:
        prompt = file.read()

    return prompt
