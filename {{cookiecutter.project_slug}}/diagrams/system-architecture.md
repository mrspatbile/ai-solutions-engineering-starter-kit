# System Architecture

```mermaid
flowchart LR
    User[User] --> UI[Streamlit UI]
    UI --> API[FastAPI]
    API --> Services[AI Services]
    Services --> Store[(Vector Store)]
    Services --> Model[Model Provider]
```
