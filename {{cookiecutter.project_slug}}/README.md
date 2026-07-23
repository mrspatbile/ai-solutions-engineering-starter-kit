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
| Foundation dependency | {{ cookiecutter.depends_on_foundation }} ({{ cookiecutter.foundation_package_name }} @ {{ cookiecutter.foundation_version_tag }}) |

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

## Replacing the Mock Services

Every service in `app/services/` ships with a deterministic, network-free
mock as the default, so this project runs and passes tests with zero
credentials or installed packages. Each file ends with a `# TODO`
marking where a real implementation goes — this is expected, not
unfinished work.

To wire in a real implementation: write a new class satisfying the same
Protocol and swap it in at the point where the mock is currently
instantiated. Call sites depend on the Protocol, not the concrete
class, so nothing else in the app changes.

{% if cookiecutter.depends_on_foundation == "yes" -%}
This project depends on `{{ cookiecutter.foundation_package_name }}`
(pinned to `{{ cookiecutter.foundation_version_tag }}`). See the
`# TODO` in `app/services/foundation_service.py` — the real
implementation should import the installed package directly, not read
`foundation_package_name`/`foundation_git_url`/`foundation_version_tag`
at runtime; those are generation-time-only values used to pin the
dependency in `pyproject.toml`.
{%- endif %}

## Evaluation

```bash
make evaluate
```

The default runner uses deterministic predictions so it works without paid model access.

## Portfolio Evidence

Use `docs/10-results.md`, `docs/11-reflection.md`, test output, screenshots, and API examples to demonstrate judgment beyond a happy-path demo.
