from pathlib import Path


def main() -> None:
    Path("data/sample").mkdir(parents=True, exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    print("Project folders are ready.")


if __name__ == "__main__":
    main()

