import streamlit

import llm.prompt
import llm.query


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
            response = llm.query.get_completion(system_prompt, text)
        streamlit.markdown(response)


if __name__ == '__main__':
    main()
