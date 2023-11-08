import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
COHERE_API_KEY = os.environ.get("COHERE_API_KEY")

DEFAULT_EXCLUDES = [
    "*.git",
    "__pycache__",
    "*.pyc",
    ".idea",
    "venv",
    ".env*",
]
