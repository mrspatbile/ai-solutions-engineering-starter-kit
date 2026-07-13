from __future__ import annotations

import json
from pathlib import Path

from metrics import exact_match, label_accuracy

DATASET_PATH = Path(__file__).with_name("dataset.example.json")
RESULTS_PATH = Path(__file__).parent / "results" / "sample_results.json"


def mock_predict(item: dict[str, str]) -> dict[str, str]:
    text = item["input"].lower()
    label = "needs_review" if "risk" in text or "fraud" in text else "general"
    return {"answer": item["expected_answer"], "label": label}


def main() -> None:
    dataset = json.loads(DATASET_PATH.read_text(encoding="utf-8"))
    rows = []
    expected_labels = []
    actual_labels = []
    exact_scores = []

    for item in dataset:
        prediction = mock_predict(item)
        expected_labels.append(item["expected_label"])
        actual_labels.append(prediction["label"])
        exact_scores.append(exact_match(item["expected_answer"], prediction["answer"]))
        rows.append({"id": item["id"], "prediction": prediction, "expected": item})

    result = {
        "exact_match": sum(exact_scores) / len(exact_scores),
        "label_accuracy": label_accuracy(expected_labels, actual_labels),
        "rows": rows,
        "notes": "Sample deterministic output. Replace mock_predict with the real pipeline.",
    }
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
