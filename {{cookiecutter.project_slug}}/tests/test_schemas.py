from app.schemas import ExampleRequest, ExampleResponse


def test_example_request_accepts_text() -> None:
    request = ExampleRequest(text="hello")
    assert request.text == "hello"


def test_example_response_schema() -> None:
    response = ExampleResponse(
        answer="ok",
        confidence=0.5,
        label="general",
        requires_human_review=False,
    )
    assert response.model_dump()["confidence"] == 0.5
