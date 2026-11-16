# YourStudyBuddy

An AI-powered study assistant for CSC 603/803 Generative AI at San Francisco State University.

**Status:** Starter repository. Core AI features are not implemented yet.

## Planned features

- Upload text-based PDFs and extract study material
- Ask questions grounded in uploaded documents using RAG
- Generate study summaries
- Evaluate answers on at least 15 test questions

## Planned stack

- Python + Streamlit (web interface)
- PyMuPDF (PDF text extraction)
- FAISS (document retrieval)
- Hugging Face Inference API (language model)

## Quick start

1. Create a Python 3.10+ virtual environment and activate it.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

To use Hugging Face inference later, copy `.env.example` to `.env` and add your token. Never commit `.env` or real credentials.

## Project structure

```text
app.py                  # Streamlit interface
src/pdf_processing.py   # Planned text extraction and splitting
src/retrieval.py        # Planned embedding/search pipeline
src/generation.py       # Planned answer and summary generation
tests/                  # Future tests
```

## Team

- Michael Arteaga
- Shreya Rameshwar
- Aniket Soni

## Scope

This starter provides a basic running interface only. PDF processing, embeddings, FAISS indexing, LLM inference, source citations, and evaluation are TODOs for later development.
