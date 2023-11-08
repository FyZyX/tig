import os
import pathlib

CODEBASE_ROOT = pathlib.Path(__file__) / "code"

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
COHERE_API_KEY = os.environ.get("COHERE_API_KEY")
