# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Project Snapshot

| Field | Value |
| --- | --- |
| Author | {{ cookiecutter.author_name }} |
| Business domain | {{ cookiecutter.business_domain }} |
| Target user | {{ cookiecutter.target_user }} |
| AI pattern | {{ cookiecutter.ai_pattern }} |
| Interface | {{ cookiecutter.interface_type }} |
| Model provider | {{ cookiecutter.model_provider }} |
| Vector store | {{ cookiecutter.vector_store }} |

## Getting Started

Requires [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`).

```bash
uv venv
source .venv/bin/activate
uv sync --extra development
cp .env.example .env
make test
make run-api
```

Run the Streamlit UI with:

```bash
make run-ui
```

## Documentation Workflow

1. Complete [discovery](docs/01-discovery.md).
2. Define the problem and success criteria.
3. Trace requirements to tests and evaluation metrics.
4. Document architecture and risk controls.
5. Run the evaluation workflow and record results.
6. Capture reflection and interview talking points.

## API

- `GET /health`: service health
- `POST /api/v1/example`: deterministic sample structured-output endpoint

Open `http://localhost:8000/docs` after starting the API.

## Evaluation

```bash
make evaluate
```

The default runner uses deterministic predictions so it works without paid model access.

## Portfolio Evidence

Use `docs/10-results.md`, `docs/11-reflection.md`, test output, screenshots, and API examples to demonstrate judgment beyond a happy-path demo.
