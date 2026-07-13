from typing import Protocol

from app.schemas import EvidenceItem, ExampleRequest, ExampleResponse


class LLMService(Protocol):
    def generate_structured_response(self, request: ExampleRequest) -> ExampleResponse:
        """Return validated structured output for an application request."""


class LocalMockLLMService:
    def generate_structured_response(self, request: ExampleRequest) -> ExampleResponse:
        normalized = request.text.strip()
        if not normalized:
            raise ValueError("text must not be empty")

        risky_terms = ["risk", "fraud"]
        label = (
            "needs_review"
            if any(term in normalized.lower() for term in risky_terms)
            else "general"
        )
        evidence = []
        if request.include_evidence:
            evidence.append(
                EvidenceItem(
                    source="local-mock",
                    excerpt=normalized[:160],
                )
            )

        return ExampleResponse(
            answer=f"Mock response for: {normalized}",
            confidence=0.72,
            label=label,
            evidence=evidence,
            requires_human_review=label == "needs_review",
        )


# TODO: Add an Ollama, Hugging Face, or OpenAI-compatible implementation here.
