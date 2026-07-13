# Agent Flow

```mermaid
flowchart TD
    Request[Request] --> Plan[Plan steps]
    Plan --> Tool{Select tool}
    Tool --> Calc[Calculator]
    Tool --> Lookup[Lookup]
    Calc --> Final[Validated answer]
    Lookup --> Final
```
