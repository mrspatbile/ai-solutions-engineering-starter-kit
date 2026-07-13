install:
	uv sync --extra development

run-api:
	uv run --extra development uvicorn app.main:app --reload

run-ui:
	uv run --extra development streamlit run ui/streamlit_app.py

test:
	uv run --extra development pytest

lint:
	uv run --extra development ruff check .

typecheck:
	uv run --extra development mypy app evaluation

evaluate:
	uv run --extra development python evaluation/run_evaluation.py
