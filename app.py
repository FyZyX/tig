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
def init():
    pass


@app.command()
def commit(
        target: str = typer.Option(..., "--target", "-t", help="Target file"),
        commit_message: str = typer.Option(..., "--message", "-m",
                                           help="Commit message"),
        api_key: Optional[str] = typer.Option(None, envvar="OPENAI_API_KEY"),
):
    if api_key is None:
        typer.echo(
            "Please provide an API key or set the appropriate environment variable."
        )
        raise typer.Exit(code=1)

    original_code = get_original_code(target)
    snippet = apply_commit(original_code, commit_message)
    splice_new_code(target, snippet)
    typer.echo(f"Updated {target}")


@app.command()
def status():
    pass


@app.command()
def diff():
    pass


@app.command()
def apply():
    pass


if __name__ == "__main__":
    app()
