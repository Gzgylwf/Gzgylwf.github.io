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

def create_new_resume():
    resume = Resume()
    resume.save_to("data")

def open_resume():
    pass


st.set_page_config(
    page_title=f"Personal Page Manager",
    layout="wide"
)

# Session variable
st.session_state.setdefault("resume_path", None)

resume_list = get_all_resumes()
st.sidebar.selectbox("Select Resume", options=resume_list, key="resume_path")
if st.sidebar.button("Open Resume", use_container_width=True): open_resume()
if st.sidebar.button("Create New Resume", use_container_width=True): create_new_resume()
    
st.text_area("Text:")