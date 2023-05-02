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


def extract_snippet(input_string):
    start_tag = "<SNIPPET>"
    end_tag = "</SNIPPET>"
    start_index = input_string.find(start_tag) + len(start_tag)
    end_index = input_string.find(end_tag)
    if start_index == -1 or end_index == -1:
        return ""
    else:
        return input_string[start_index:end_index].strip()


def apply_commit(code, commit_message: str) -> str:
    messages = [
        {"role": "system", "content": Prompt("context").render()},
        {"role": "user", "content": Prompt("generate-code").render(
            code=code,
            commit=commit_message,
        )},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    content = response.choices[0]["message"]["content"]
    return extract_snippet(content)
