FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /template
COPY . .
RUN uv pip install --system --no-cache cookiecutter
CMD ["cookiecutter", "."]
