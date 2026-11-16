"""Minimal Streamlit shell for YourStudyBuddy."""

import streamlit as st


st.set_page_config(page_title="YourStudyBuddy", page_icon="📚")
st.title("📚 YourStudyBuddy")
st.caption("AI-powered study assistant | CSC 603/803")
st.info("Project starter: document-based AI features are coming soon.")

uploaded_file = st.file_uploader("Upload a text-based PDF", type=["pdf"])
question = st.text_input("Ask a question about your material")

if uploaded_file is not None:
    st.success(f"Selected: {uploaded_file.name}")
    st.caption("PDF extraction and retrieval are not implemented yet.")

if st.button("Ask", disabled=not (uploaded_file and question.strip())):
    st.warning("Question answering will be added in a future milestone.")

if st.button("Generate summary", disabled=uploaded_file is None):
    st.warning("Summarization will be added in a future milestone.")
