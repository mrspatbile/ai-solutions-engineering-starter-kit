from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class EvaluationResult:
    metric_name: str
    score: float
    notes: str


class EvaluationService(Protocol):
    def evaluate(self, expected: str, actual: str) -> EvaluationResult:
        """Evaluate one expected/actual pair."""


class ExactMatchEvaluationService:
    def evaluate(self, expected: str, actual: str) -> EvaluationResult:
        score = 1.0 if expected.strip().lower() == actual.strip().lower() else 0.0
        return EvaluationResult("exact_match", score, "Deterministic starter metric")
