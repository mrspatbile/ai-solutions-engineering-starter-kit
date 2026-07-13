def exact_match(expected: str, actual: str) -> float:
    return 1.0 if expected.strip().lower() == actual.strip().lower() else 0.0


def label_accuracy(expected: list[str], actual: list[str]) -> float:
    if not expected:
        return 0.0
    matches = sum(1 for exp, act in zip(expected, actual, strict=False) if exp == act)
    return matches / len(expected)
