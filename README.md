![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/github/license/mrspatbile/ai-solutions-engineering-starter-kit)
![Cookiecutter](https://img.shields.io/badge/built%20with-cookiecutter-orange)
![uv](https://img.shields.io/badge/dependency%20manager-uv-purple)


# AI Solutions Engineering Starter Kit

An opinionated template for planning and building AI applications with full reasoning from business problem through deployment, covering RAG, tool-calling agents, document extraction, classification, structured-output APIs, and finance-focused workflows.


## What It Generates

- A Python 3.11+ FastAPI starter with health and example endpoints
- A Streamlit starter UI
- Provider-independent interfaces for LLM, embedding, retrieval, and evaluation services
- An optional, version-pinned dependency on an external "foundation" data package (`depends_on_foundation`), with a deterministic mock service by default
- Documentation templates from discovery through reflection
- Mermaid architecture diagrams
- Evaluation dataset, metrics, and a deterministic evaluation runner
- Docker, Docker Compose, Makefile, Ruff, mypy, pytest, and GitHub Actions
- Portfolio-oriented examples and readiness checklists

## Install uv And Cookiecutter

This template uses [uv](https://docs.astral.sh/uv/) for dependency management. Install it first if you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install Cookiecutter as a uv tool:

```bash
uv tool install cookiecutter
```

## Generate A New Project

New projects live in `~/Documents/ai-solutions/<new-repo>`. From this repository root, run:

```bash
mkdir -p ~/Documents/ai-solutions
cookiecutter . --output-dir ~/Documents/ai-solutions
```

Answer the prompts. The generated project will appear at `~/Documents/ai-solutions/your-project-slug`.

## Create The Remote And Make The First Commit

Initialize git inside the generated project and make the first commit:

```bash
cd ~/Documents/ai-solutions/your-project-slug
git init -b main
git add .
git commit -m "Initial commit from ai-solutions-engineering-starter-kit"
```

Then create the GitHub remote and push. With the [GitHub CLI](https://cli.github.com/) (`gh auth login` first if needed):

```bash
gh repo create your-project-slug --private --source . --remote origin --push
```

Without `gh`, create an empty repository on github.com (no README, license, or .gitignore — the project already has them), then:

```bash
git remote add origin git@github.com:<your-github-username>/your-project-slug.git
git push -u origin main
```

## Run The Generated Project Locally

```bash
cd ~/Documents/ai-solutions/your-project-slug
uv venv
source .venv/bin/activate
uv sync --extra development
cp .env.example .env
make run-api
```

In a second terminal:

```bash
make run-ui
```

## Run Tests And Checks

```bash
make lint
make typecheck
make test
```

## Use Docker

```bash
docker compose up --build
```

The API listens on `http://localhost:8000`. Streamlit listens on `http://localhost:8501` when included.

## Customize The Documentation

Start with `docs/01-discovery.md`, then work forward. Each document is a template with TODOs, example tables, and evidence prompts. Replace sample assumptions with your own evidence. Do not present fictional stakeholder assumptions as real interviews.

## Replace Mock AI Services

The generated code intentionally uses deterministic local implementations. Replace them incrementally:

- `app/services/llm_service.py`: connect Ollama, Hugging Face, or an OpenAI-compatible API.
- `app/services/embedding_service.py`: connect Sentence Transformers or provider embeddings.
- `app/services/retrieval_service.py`: connect FAISS or Chroma.
- `app/services/foundation_service.py` (present only when `depends_on_foundation` is `yes`): connect the pinned foundation package named at generation time (`foundation_package_name`, `foundation_git_url`, `foundation_version_tag` in `cookiecutter.json`).
- `evaluation/run_evaluation.py`: replace mock predictions with your application pipeline.

Keep validation, logging, error handling, and test coverage in place as you add real providers.

## From Business Problem To Portfolio Evidence

```text
Discovery
→ Problem definition
→ Requirements
→ Solution design
→ Implementation
→ Evaluation
→ Deployment
→ Reflection
```

The template answers demo, reason about users, requirements, cost, risk, quality, and deployment tradeoffs.

## Example Project Types This Template Supports

- Financial Document Assistant (RAG pattern)
- Financial Investigation Agent (agent pattern)
- Transaction Intelligence API (structured-output pattern)
- Data Consumer Application (foundation-package pattern)

## Projects Built From This Template

- [Equity vs Debt Analysis](../equity-vs-debt-analysis)

## Template Maintenance

Use the root `Makefile` to inspect the template and run checks against a generated sample project.
