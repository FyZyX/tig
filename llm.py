import os
import string

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")


class Prompt:
    _template_dir = "prompts"

    def __init__(self, name):
        self._name = name

    def _read(self):
        with open(f"{self._template_dir}/{self._name}.md") as prompt_file:
            return prompt_file.read()

    def render(self, **kwargs):
        prompt = self._read()
        if not kwargs:
            return prompt
        template = string.Template(prompt)
        return template.substitute(**kwargs)


async def apply_commit(code, commit_message: str) -> str:
    messages = [
        {"role": "system", "content": Prompt("context").render()},
        {"role": "user", "content": Prompt("generate-code").render(
            code=code,
            commit=commit_message,
        )},
    ]

    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return response.choices[0]["message"]["content"]
