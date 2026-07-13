# Transaction Intelligence API

## Business Problem

Transaction descriptions are inconsistent, making reporting, support, and risk review slower.

## Target User

Payments analyst, product operations analyst, or customer support tooling team.

## AI Role

Structured classification, merchant normalization, confidence scoring, and human-review routing.

## Deterministic Components

Known merchant dictionary, amount/date validation, schema validation, routing thresholds, and audit logging.

## Proposed Architecture

FastAPI endpoint, Pydantic schemas, deterministic normalization rules, optional model classifier, evaluation dataset, and CI tests.

## Success Metrics

Classification F1, schema validity, review precision, latency, and cost per 1,000 transactions.

## Risks

Misclassification, bias in training examples, sensitive transaction text, model drift, and public-demo abuse.

## Suggested Free-First Stack

Python, FastAPI, Pydantic, Pandas, pytest, Ruff, Docker, and GitHub Actions.
