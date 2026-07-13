# User Workflow

```mermaid
flowchart TD
    A[Open app] --> B[Submit input]
    B --> C[Review structured result]
    C --> D{Needs human review?}
    D -->|Yes| E[Escalate]
    D -->|No| F[Use result]
```
