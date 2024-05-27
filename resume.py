import typer
import os
import streamlit as st
from relic.soul import RELIC

# Global variable
resume = None               # Open resume file

def get_all_resumes() -> list[str]:
    ret = []
    root = os.path.join(os.getcwd(), "data")
    for folder in os.listdir(root):
        if os.path.isdir(os.path.join(root, folder)): ret.append(folder)
    return ret

def run_relic(soul_name: str):
    st.set_page_config(
        page_title=f"{soul_name}'s RELIC",
        layout="wide"
    )

    if resume is None:
        get_all_resumes()
        st.sidebar.selectbox("Select Resume")
    else:
        pass

if __name__ == "__main__":
    typer.run(run_relic)