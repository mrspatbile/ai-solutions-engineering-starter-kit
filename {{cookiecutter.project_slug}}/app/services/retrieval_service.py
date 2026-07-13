from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class RetrievedDocument:
    source: str
    text: str
    score: float


class RetrievalService(Protocol):
    def search(self, query: str, limit: int = 3) -> list[RetrievedDocument]:
        """Return relevant documents for a query."""


class InMemoryRetrievalService:
    def __init__(self) -> None:
        self._documents = [
            RetrievedDocument(
                source="sample",
                text="Replace this with indexed project data.",
                score=0.5,
            )
        ]

    def search(self, query: str, limit: int = 3) -> list[RetrievedDocument]:
        if not query.strip():
            return []
        return self._documents[:limit]


# TODO: Connect FAISS or Chroma after the project has real documents.
