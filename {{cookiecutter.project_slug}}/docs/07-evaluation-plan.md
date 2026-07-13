# Evaluation Plan

## Evaluation Questions

- Does the system return schema-valid outputs?
- Does it retrieve relevant evidence?
- Does it abstain when evidence is missing?
- Does it route risky cases to human review?

## Test Dataset Design

| Slice | Example | Minimum count |
| --- | --- | --- |
| Happy path | Clear answer in context | TODO |
| Ambiguous | Missing or conflicting context | TODO |
| Adversarial | Prompt injection or unsafe request | TODO |

## Baseline

Manual workflow or deterministic keyword rules.

## Experiment Configurations

| Config | Model | Retrieval | Prompt | Notes |
| --- | --- | --- | --- | --- |
| A | Local mock | None | Starter | Smoke test |

## Metrics

| Category | Metric | Notes |
| --- | --- | --- |
| Retrieval | Recall@k, MRR | Needs labeled relevant chunks |
| Generation | Faithfulness, groundedness | Human or rubric evaluation |
| Structured output | Schema validity rate | Automated |
| Classification | Accuracy, precision, recall, F1 | Automated |
| Abstention | Abstention accuracy | Missing-evidence cases |
| Latency | p50, p95 | API logs |
| Estimated cost | Cost per 100 requests | Fixed budget plan |

## Failure Analysis

| Failure | Example | Root cause | Fix |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Human-Review Criteria

- Low confidence
- Missing evidence
- Sensitive or high-impact decision
- Numerical inconsistency

## Example Evaluation Table

| Case ID | Expected | Actual | Pass | Notes |
| --- | --- | --- | --- | --- |
| case-001 | needs_review | needs_review | Yes | Starter example |

