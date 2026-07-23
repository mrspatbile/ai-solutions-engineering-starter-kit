# Data Consumer Application

## Business Problem

Users need timely insight from a specialized dataset without the team building and maintaining its own ingestion, parsing, or refresh pipeline for that data.

## Target User

Analyst, researcher, or operations team member who needs answers grounded in a specific external dataset (e.g. SEC EDGAR fund holdings).

## AI Role

Summarization, comparison, and natural-language querying over records returned by a foundation data package. The application adds interpretation and workflow value; it does not originate the underlying data.

## Deterministic Components

Foundation package client calls, response schema validation, caching of foundation query results, and version pinning of the foundation dependency.

## Proposed Architecture

FastAPI endpoint, Pydantic schemas, a `FoundationDataService` interface wrapping the pinned foundation package, optional model layer for summarization, evaluation dataset, and CI tests that run against a local mock so the real package and its network access are never required for the test suite.

## Success Metrics

Query success rate, foundation package staleness (time since last refresh), answer groundedness against foundation records, latency, and cost per query.

## Risks

Foundation package version drift, upstream schema changes, foundation data staleness or gaps, blind trust in foundation data without validation, and licensing or rate-limit constraints on the foundation source.

## Suggested Free-First Stack

Python, FastAPI, a pinned git-installed foundation package, Pydantic, pytest, Ruff, Docker, and GitHub Actions.
