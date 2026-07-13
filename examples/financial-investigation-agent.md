# Financial Investigation Agent

## Business Problem

Investigators need to compare documents, normalize facts, and decide which cases require deeper review.

## Target User

Fraud analyst, compliance analyst, or finance operations lead.

## AI Role

Tool calling, workflow planning, document comparison, and calculator or structured tools.

## Deterministic Components

Calculations, rule checks, thresholds, date comparisons, tool schemas, and final validation.

## Proposed Architecture

API orchestrator, approved tools, document comparison service, calculation utility, structured output schema, and human-review queue.

## Success Metrics

Correct tool selection, calculation accuracy, review routing precision, latency, and explanation quality.

## Risks

Unsafe tool calls, numerical mistakes, missing evidence, prompt injection, and false confidence.

## Suggested Free-First Stack

Python, FastAPI, local mock tools, Pandas, Ollama for optional reasoning, pytest, and Docker.
