import typer
import os
import streamlit as st
from relic.resume import Resume, Profile

# Global variable
resume = None               # Open resume file

def get_all_resumes() -> list[str]:
    ret = []
    root = os.path.join(os.getcwd(), "data")
    for folder in os.listdir(root):
        if os.path.isdir(os.path.join(root, folder)): ret.append(folder)
    return ret

@st.experimental_dialog("Create new resume")
def create_new_resume():
    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    if st.button("Create", use_container_width=True, type="primary"):
        profile = Profile(first_name=first_name, last_name=last_name)
        resume = Resume(profile=profile)
        resume.save(f"data/{first_name}_{last_name}")
        st.success(f"Created new resume: {first_name} {last_name}")
        st.rerun()

def open_resume():
    pass

def run_resume():
    st.set_page_config(
        page_title=f"Personal Page Manager",
        layout="wide"
    )

    st.sidebar.selectbox("Select Resume", options=get_all_resumes())
    if st.sidebar.button("Open Resume", use_container_width=True): open_resume()
    if st.sidebar.button("Create New Resume", use_container_width=True): create_new_resume()
    


if __name__ == "__main__":
    typer.run(run_resume)