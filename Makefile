generate:
	mkdir -p ~/Documents/ai-solutions
	cookiecutter . --output-dir ~/Documents/ai-solutions

lint:
	ruff check .
