import os
import string

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")


class ChatMessages:
    def __init__(self):
        self._messages = []

    def add_message(self, role: str, content: str):
        self._messages.append({"role": role, "content": content})

    def add_system_message(self, content: str):
        self.add_message("system", content)

    def add_user_message(self, content: str):
        self.add_message("user", content)

    def all(self):
        return self._messages


class LLM:
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        self._model_name = model_name

    def submit(self, messages: ChatMessages, **kwargs):
        response = openai.ChatCompletion.create(
            model=self._model_name,
            messages=messages.all(),
            **kwargs,
        )
        return response.choices[0]["message"]["content"]


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


def extract_snippet(response: str, start_tag="<SNIPPET>", end_tag="</SNIPPET>"):
    response = response.removeprefix(start_tag).removesuffix(end_tag)
    start_index = response.find(start_tag) + len(start_tag)
    end_index = response.find(end_tag)
    if start_index == -1 or end_index == -1:
        return ""
    return response[start_index:end_index].strip()


def apply_commit(code, commit_message: str) -> str:
    messages = ChatMessages()
    messages.add_system_message(Prompt("context").render())
    messages.add_user_message(Prompt("generate-code").render(
        code=code,
        commit=commit_message,
    ))

    llm = LLM()
    content = llm.submit(messages)
    return extract_snippet(content)
