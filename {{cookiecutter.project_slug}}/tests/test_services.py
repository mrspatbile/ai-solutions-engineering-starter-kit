from app.schemas import ExampleRequest
from app.services.embedding_service import LocalHashEmbeddingService
from app.services.llm_service import LocalMockLLMService
from app.services.retrieval_service import InMemoryRetrievalService


def test_llm_service_returns_review_label_for_risk() -> None:
    response = LocalMockLLMService().generate_structured_response(
        ExampleRequest(text="payment risk")
    )
    assert response.requires_human_review is True


def test_embedding_length() -> None:
    assert len(LocalHashEmbeddingService().embed("abc")) == 16


def test_retrieval_returns_documents() -> None:
    assert InMemoryRetrievalService().search("query")
