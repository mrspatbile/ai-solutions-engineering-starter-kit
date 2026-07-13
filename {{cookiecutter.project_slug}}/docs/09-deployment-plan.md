# Deployment Plan

## Target Environment

| Environment | Purpose | Owner |
| --- | --- | --- |
| Local Docker | Demo and development | TODO |
| Cloud app platform | Optional hosted portfolio demo | TODO |

## Configuration

- Use `.env` for local settings.
- Use platform secrets for hosted deployments.
- Never commit API keys.

## Release Steps

1. Run tests, linting, and type checks.
2. Build Docker image.
3. Smoke test `/health`.
4. Record version and known limitations.

## Rollback

Describe how to return to the previous working image or commit.

## Monitoring

Track latency, error rate, validation failures, retrieval misses, and estimated cost.

