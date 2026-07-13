# Api Sequence

```mermaid
sequenceDiagram
    participant Client
    participant API
    participant Service
    Client->>API: Request
    API->>Service: Process
    Service-->>API: Result
    API-->>Client: Response
```
