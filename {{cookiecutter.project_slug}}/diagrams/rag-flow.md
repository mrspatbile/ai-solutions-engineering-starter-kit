# Rag Flow

```mermaid
flowchart TD
    Docs[Documents] --> Chunk[Chunk text]
    Chunk --> Embed[Create embeddings]
    Embed --> Index[(Index)]
    Query[Question] --> Search[Similarity search]
    Index --> Search
    Search --> Answer[Grounded answer]
```
