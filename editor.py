import streamlit as st
import typer

def editor():
    st.set_page_config(
        page_title="Resume Editor",
        layout="wide"
    )

if __name__ == "__main__":
    typer.run(editor)