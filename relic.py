import typer
import os
import streamlit as st
from relic.soul import RELIC

def run_relic(soul_name: str):
    st.set_page_config(
        page_title=f"{soul_name}'s RELIC",
        layout="wide"
    )

    soul_folder = os.path.join("souls", soul_name)
    if os.path.exists(soul_folder):
        soul = RELIC.load(soul_folder)
        # soul = RELIC.parse_file(soul_file)
        # st.sidebar.subheader(f"{soul.name}'s RELIC")
        st.title(f"{soul.first_name} {soul.last_name}'s RELIC")

        # st.sidebar.page_link(page="pages/1_Home.py", label="Home")
        # st.sidebar.page_link(page="pages/2_Setting.py", label="Setting")
    else:
        with st.form("my_form"):
            first_name = st.text_input("First name")
            last_name = st.text_input("Last name")
            # Every form must have a submit button.
            submitted = st.form_submit_button("CREATE")
            if submitted:
                soul = RELIC(root=soul_folder, first_name=first_name, last_name=last_name)
                soul.save()

if __name__ == "__main__":
    typer.run(run_relic)