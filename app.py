import json
from typing import Optional

import typer

from llm import apply_commit

app = typer.Typer()


def get_original_code(filename):
    with open(filename) as file:
        return file.read()


def splice_new_code(filename, code):
    with open(filename, "w") as file:
        file.write(code)


@app.command()
def commit(
        filename: str,
        commit_message: str,
        api_key: Optional[str] = typer.Option(None, envvar="OPENAI_API_KEY"),
):
    if api_key is None:
        typer.echo(
            "Please provide an API key or set the appropriate environment variable."
        )
        raise typer.Exit(code=1)

    original_code = get_original_code(filename)
    code = apply_commit(original_code, commit_message)
    snippet = json.loads(code)["snippet"]
    splice_new_code(filename, snippet)
    typer.echo(f"Updated {filename}")


if __name__ == "__main__":
    app()
