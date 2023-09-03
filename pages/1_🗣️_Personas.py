import streamlit

import llm.prompt


def main():
    tabs = streamlit.tabs(["Update Persona", "Create Persona"])

    with tabs[0]:
        persona_names = llm.prompt.available_personas()
        persona_name = streamlit.selectbox("Persona", options=persona_names)
        persona = llm.prompt.load_persona(persona_name)

        updated_persona = streamlit.text_area("Persona", value=persona)
        if streamlit.button("Update"):
            pass

    with tabs[1]:
        persona = streamlit.text_area("Persona")
        if streamlit.button("Create"):
            pass


if __name__ == '__main__':
    main()
