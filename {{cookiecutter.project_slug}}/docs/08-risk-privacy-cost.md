# Risk, Privacy, And Cost

## Risk Register

| Risk | Likelihood | Effect | Control | Owner | Residual risk |
| --- | --- | --- | --- | --- | --- |
| Hallucinations | Medium | Misleading answer | Evidence requirement and abstention | Product/Eng | Medium |
| Poor retrieval | Medium | Wrong context | Retrieval evaluation and relevance thresholds | Eng | Medium |
| Prompt injection | Medium | Instruction override | Context isolation and refusal rules | Eng | Medium |
| Data leakage | Low | Sensitive exposure | Redaction and access controls | Security | Low |
| Sensitive information | Medium | Compliance issue | Minimize data sent to model | Product/Security | Medium |
| Numerical errors | Medium | Bad decisions | Deterministic calculators | Eng | Low |
| Model availability | Medium | Downtime | Local fallback or graceful degradation | Eng | Medium |
| Latency | Medium | Poor UX | Timeouts and smaller context | Eng | Medium |
| Cost overruns | Medium | Budget impact | Request limits and monitoring | Product | Low |
| Public-demo abuse | Medium | Resource exhaustion | Rate limits and no secrets in demo | Eng | Medium |

## Free-First Cost Plan

| Layer | Free-first choice | Notes |
| --- | --- | --- |
| Language | Python | Broad ecosystem |
| Local model | Ollama | Optional local inference |
| Embeddings | Sentence Transformers | Optional local embeddings |
| Vector store | FAISS or Chroma | Local development |
| API | FastAPI | Lightweight |
| UI | Streamlit | Fast portfolio demo |
| Packaging | Docker | Reproducible local run |
| Publishing | GitHub | Source, issues, CI |

## Optional Paid-Model Comparison

Fixed budget: TODO, for example USD 10.

| Provider | Use case | Budget guardrail | What to compare |
| --- | --- | --- | --- |
| OpenAI-compatible API | Higher quality generation | Hard monthly cap | Accuracy, latency, cost |
| Hosted embeddings | Better retrieval | Batch only | Recall@k and cost |

