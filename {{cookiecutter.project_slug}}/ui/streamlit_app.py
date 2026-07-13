import streamlit as st

from app.schemas import ExampleRequest
from app.services.llm_service import LocalMockLLMService

st.set_page_config(page_title="{{ cookiecutter.project_name }}", page_icon="AI")
st.title("{{ cookiecutter.project_name }}")
st.caption(
    "{{ cookiecutter.project_description }}"
)

text = st.text_area(
    "Input text",
    placeholder="Paste a question, document excerpt, or transaction note.",
)
uploaded_file = st.file_uploader("Optional file upload placeholder")
include_evidence = st.checkbox("Include evidence", value=True)

if st.button("Generate sample response"):
    try:
        if uploaded_file is not None:
            st.info(
                "File ingestion is a placeholder. "
                "Add project-specific parsing in scripts/ingest_documents.py."
            )
        response = LocalMockLLMService().generate_structured_response(
            ExampleRequest(
                text=text or "Sample portfolio request",
                include_evidence=include_evidence,
            )
        )
        st.json(response.model_dump())
    except Exception as exc:
        st.error(f"Unable to generate response: {exc}")
