# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is a **Cookiecutter template**, not a runnable application. The repo root only builds and validates the template; the actual FastAPI/Streamlit application code, docs, and tests live under the literal directory `{{cookiecutter.project_slug}}/` and only become a real project once Cookiecutter renders the Jinja placeholders (`{{ cookiecutter.* }}`) during generation.

Two very different codebases coexist here:
- **Root** (`pyproject.toml`, `Makefile`, `hooks/`, `playbook/`, `cookiecutter.json`): the template machinery itself.
- **`{{cookiecutter.project_slug}}/`**: the Jinja-templated project that gets stamped out for each new AI solutions engineering project. Ruff excludes this directory at the root level (`tool.ruff.exclude`) because its Python is not valid until rendered.

When asked to change "the app," "the API," or "the Streamlit UI," the work belongs inside `{{cookiecutter.project_slug}}/`, not the root.

## Commands

### Working on the template itself (repo root)
```bash
make lint        # ruff check . (root only; template dir is excluded)
make generate     # cookiecutter . --output-dir ~/Documents/ai-solutions
```
There is no root-level test suite — validation means generating a sample project and running its checks (see CONTRIBUTING.md: "Run checks against a generated sample project before opening a pull request").

### Working on a generated project (inside `{{cookiecutter.project_slug}}/`, or a project already generated from it)
```bash
uv sync --extra development   # install deps (uv-managed, Python 3.11+)
make run-api                  # uvicorn app.main:app --reload  (localhost:8000, /docs for OpenAPI)
make run-ui                   # streamlit run ui/streamlit_app.py (localhost:8501)
make test                     # pytest (config in pyproject.toml: -q --cov=app --cov-report=term-missing)
make lint                     # ruff check .
make typecheck                # mypy app evaluation (strict = true)
make evaluate                 # python evaluation/run_evaluation.py
```
Run a single test with `uv run --extra development pytest tests/test_health.py::test_name`.

### Testing the cookiecutter hook logic
`hooks/post_gen_project.py` runs after rendering and conditionally deletes files based on cookiecutter answers (e.g. `include_fastapi`, `include_docker`) and writes the chosen `LICENSE` file. To verify changes to it, actually generate a project (`make generate`) and inspect the output — there's no unit test harness for the hook itself.

## Architecture of the generated project

The template's core idea is **provider-independent service interfaces**: every AI capability is defined as a `Protocol` in `app/services/`, with a deterministic local/mock implementation shipped by default so the generated project runs and passes tests with zero paid API keys. Swapping in a real provider means writing a new class that satisfies the same Protocol — call sites in `app/api/routes.py` don't change.

- `app/services/llm_service.py` — `LLMService` protocol + `LocalMockLLMService` (keyword-based mock classification, e.g. flags "risk"/"fraud" text as `needs_review`). Real implementations (Ollama, Hugging Face, OpenAI-compatible) get added here.
- `app/services/retrieval_service.py` — `RetrievalService` protocol + `InMemoryRetrievalService`. Real FAISS/Chroma implementations go here.
- `app/services/embedding_service.py`, `app/services/evaluation_service.py` — same pattern for embeddings and eval scoring.
- `app/services/foundation_service.py` — `FoundationDataService` protocol + `LocalMockFoundationDataService`, same pattern again. Only present when the project was generated with `depends_on_foundation: yes` (see below); a real implementation wraps the pinned external "foundation" data package (e.g. a package like `sec_holdings` fetching SEC EDGAR fund holdings) behind this Protocol without call sites ever importing that package directly.
- `app/schemas.py` — Pydantic models shared across services and API (e.g. `ExampleRequest`/`ExampleResponse`/`EvidenceItem`).
- `app/config.py` — `pydantic_settings.BaseSettings`, env-prefixed `APP_`, loaded from `.env` via `get_settings()` (lru_cached).
- `app/main.py` — `create_app()` factory wires health + `/api/v1` routers; the module-level `app` is what uvicorn serves.
- `evaluation/run_evaluation.py` — standalone deterministic evaluation runner (not wired to the FastAPI app) that reads `evaluation/dataset.example.json`, scores with `evaluation/metrics.py`, and writes `evaluation/results/sample_results.json`. `mock_predict()` is the seam to replace with the real pipeline.
- `ui/streamlit_app.py` — separate process from the API; talks to it over HTTP (not in-process imports).


**Note on the trailing `# TODO` in each service file:**

- Every service in `app/services/` (`llm_service.py`, `retrieval_service.py`, `embedding_service.py`, `foundation_service.py`) ships a Protocol plus a deterministic, network-free mock implementation as the default, so generated projects run and pass tests with zero credentials or installed packages.
- Each file ends with a trailing `# TODO` comment marking where a real implementation goes. This is intentional and expected, not unfinished work — do not "complete" these TODOs automatically or flag them as bugs in a future session.
- To wire in a real implementation: write a new class satisfying the same Protocol (e.g. `SecHoldingsFoundationService` for `foundation_service.py`), then swap it in at the dependency-injection point where the mock is currently instantiated. Call sites depend on the Protocol, not the concrete class, so nothing else in the app changes.
- For `foundation_service.py` specifically: the real implementation should import the installed foundation package directly (e.g. `from sec_holdings import database`) inside that class, not read `foundation_package_name`/`foundation_git_url`/`foundation_version_tag` at runtime — those remain generation-time-only values used to pin the `pyproject.toml` dependency.

### Documentation-first workflow

The template treats documentation as a first-class, sequenced deliverable, not an afterthought — this is the main differentiator vs. a typical scaffold. Each generated project ships `docs/01-discovery.md` through `docs/11-reflection.md`, meant to be filled in **in order**: discovery → problem definition → requirements → user stories → solution design → architecture → evaluation plan → risk/privacy/cost → deployment plan → results → reflection. The root `playbook/` directory holds the authoring guidance behind each doc stage (project discovery, AI use-case selection, requirements framework, solution design framework, evaluation framework, risk/privacy/cost framework, deployment framework, interview storytelling) — consult these when writing or reviewing a generated project's docs. Requirements should carry IDs traceable to tests and evaluation metrics; docs should separate stated assumptions from actual evidence (never present fictional stakeholder interviews as real).

`checklists/` (portfolio-readiness, deployment-readiness, evaluation-readiness, ai-design-review, project-kickoff) are gate documents for those same stages, and `examples/` (`financial-document-assistant.md`, `financial-investigation-agent.md`, `transaction-intelligence-api.md`) are worked reference projects covering the RAG, agent, and structured-output-API patterns respectively.

## Editing conventions specific to this template

- Any new file inside `{{cookiecutter.project_slug}}/` may need conditional removal logic added to `hooks/post_gen_project.py` if it should only exist for certain cookiecutter answers (follow the existing `remove(...)` pattern keyed off `cookiecutter.json` fields like `include_fastapi`, `include_streamlit`, `include_docker`, `include_evaluation`, `include_github_actions`, `depends_on_foundation`). `depends_on_foundation` removes both `app/services/foundation_service.py` and `tests/test_foundation_service.py` as a pair when `no`, so the whole feature disappears cleanly rather than leaving dead code.
- `cookiecutter.json` is the single source of truth for prompts/choices; keep `README.md` (root) and the generated `README.md` template in sync with any new or renamed option.
- Mock service implementations are intentionally deterministic (no randomness, no network calls) so `make test` and `make evaluate` are reproducible without credentials — preserve that property when extending mocks, and keep real-provider implementations behind the same Protocol rather than replacing it.
- `foundation_package_name`, `foundation_git_url`, and `foundation_version_tag` are generation-time-only inputs: they exist solely to render the pinned git dependency once into `pyproject.toml`'s `foundation` optional-dependency group (`foundation_git_url` is stored without a `git+` prefix; the prefix is added at render time). They are deliberately **not** threaded into `app/config.py`/`Settings` or `.env.example` — unlike `model_provider`/`vector_store`, which are genuine runtime configuration, these three values have no runtime meaning once the dependency is pinned, and the real service implementation should import the installed foundation package directly rather than re-deriving it from its own source location at runtime. Do not treat their absence from `Settings` as a gap to fill in.
