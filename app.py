from typing import Optional

import typer

from llm import apply_commit

app = typer.Typer()


@app.command()
async def commit(
        target: str,
        commit_message: str,
        api_key: Optional[str] = typer.Option(None, envvar="OPENAI_API_KEY"),
):
    if api_key is None:
        typer.echo(
            "Please provide an API key or set the appropriate environment variable."
        )
        raise typer.Exit(code=1)

    code = await apply_commit(target, commit_message)
    typer.echo(f"Generated code:\n{code}")


if __name__ == "__main__":
    app()
