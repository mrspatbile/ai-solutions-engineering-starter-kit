import shutil
from pathlib import Path


PROJECT = Path.cwd()


def remove(path: str) -> None:
    target = PROJECT / path
    if target.is_dir():
        shutil.rmtree(target)
    elif target.exists():
        target.unlink()


# Keep option handling explicit so template users can edit it safely.
if "{{ cookiecutter.include_fastapi }}".lower() not in {"yes", "true", "1"}:
    remove("app/api")
    remove("app/main.py")
    remove("tests/test_health.py")

if "{{ cookiecutter.include_streamlit }}".lower() not in {"yes", "true", "1"}:
    remove("ui")

if "{{ cookiecutter.include_docker }}".lower() not in {"yes", "true", "1"}:
    remove("Dockerfile")
    remove("docker-compose.yml")

if "{{ cookiecutter.include_evaluation }}".lower() not in {"yes", "true", "1"}:
    remove("evaluation")
    remove("docs/07-evaluation-plan.md")
    remove("checklists/evaluation-readiness.md")

if "{{ cookiecutter.include_github_actions }}".lower() not in {"yes", "true", "1"}:
    remove(".github")
