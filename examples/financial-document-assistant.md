# Financial Document Assistant

## Business Problem

Analysts spend too much time searching policies, invoices, statements, and memos for evidence-backed answers.

## Target User

Finance operations analyst or audit support specialist.

## AI Role

RAG, document retrieval, evidence-backed answers, and source references.

## Deterministic Components

File parsing, access checks, source IDs, citation formatting, confidence thresholds, and audit logs.

## Proposed Architecture

Streamlit or FastAPI front end, document ingestion script, local embeddings, FAISS or Chroma index, answer service, and evaluation runner.

## Success Metrics

Retrieval recall@k, citation accuracy, answer groundedness, abstention accuracy, latency, and user review time.

## Risks

Poor retrieval, stale documents, hallucinated citations, sensitive data leakage, and overtrust.

## Suggested Free-First Stack

Python, FastAPI, Streamlit, Sentence Transformers, FAISS, Ollama, Docker, and GitHub Actions.
