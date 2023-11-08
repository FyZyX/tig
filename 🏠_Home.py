import streamlit

import llm.prompt
import llm.query


def main():
    text = streamlit.chat_input()

    if not text:
        return

    with streamlit.chat_message("user"):
        streamlit.markdown(text)

    variables = {
        "project_structure": "",
        "commit_message": text,
    }
    system_prompt = llm.prompt.render_template("plan", variables)

    with streamlit.chat_message("assistant"):
        with streamlit.spinner("Thinking..."):
            response = llm.query.get_completion(system_prompt, text)
        streamlit.markdown(response)


if __name__ == '__main__':
    main()
