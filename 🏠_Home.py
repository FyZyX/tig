import openai
import streamlit

import config
import llm.prompt

openai.api_key = config.OPENAI_API_KEY


def get_completion(system_prompt, message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )

    return completion.choices[0].message["content"]


def main():
    persona_names = llm.prompt.available_personas()
    persona_name = streamlit.selectbox("Persona", options=persona_names)
    persona = llm.prompt.load_persona(persona_name)

    text = streamlit.chat_input()

    if not text:
        return

    with streamlit.chat_message("user"):
        streamlit.markdown(text)

    system_prompt = persona

    with streamlit.chat_message("assistant"):
        with streamlit.spinner("Thinking..."):
            response = get_completion(system_prompt, text)
        streamlit.markdown(response)


if __name__ == '__main__':
    main()
