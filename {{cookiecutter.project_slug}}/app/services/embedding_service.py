from typing import Protocol


class EmbeddingService(Protocol):
    def embed(self, text: str) -> list[float]:
        """Return an embedding vector for text."""


class LocalHashEmbeddingService:
    def embed(self, text: str) -> list[float]:
        values = [float((ord(char) % 31) / 31) for char in text[:16]]
        return values + [0.0] * (16 - len(values))


# TODO: Replace with Sentence Transformers or provider embeddings when needed.
