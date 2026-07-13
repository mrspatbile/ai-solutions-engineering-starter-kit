# Requirements

## Business Requirements

| ID | Requirement | Priority |
| --- | --- | --- |
| BR-01 | The solution must reduce time spent on the target workflow. | Must |

## Functional Requirements

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-01 | Users can submit text for analysis. | Must |

## Non-Functional Requirements

| ID | Requirement | Target |
| --- | --- | --- |
| NFR-01 | API returns a response within an acceptable latency budget. | TODO seconds |

## AI-Specific Requirements

| ID | Requirement | Rationale |
| --- | --- | --- |
| AIR-01 | The model output must be validated against a schema. | Prevent malformed responses |

## Data Requirements

| ID | Requirement | Source |
| --- | --- | --- |
| DR-01 | Example data must be anonymized or synthetic. | Security |

## Security Requirements

| ID | Requirement | Control |
| --- | --- | --- |
| SR-01 | No API keys are committed. | `.env` and secret scanning |

## Deployment Requirements

| ID | Requirement | Notes |
| --- | --- | --- |
| DEP-01 | The application can run locally with Docker. | Optional |

## Traceability

| Requirement ID | Test | Evaluation Metric | Evidence Artifact |
| --- | --- | --- | --- |
| FR-01 | `tests/test_health.py` and API tests | Request success rate | Test output |
| AIR-01 | `tests/test_schemas.py` | Schema validity rate | Evaluation output |
| SR-01 | Manual review | Secret leakage count | Security checklist |

