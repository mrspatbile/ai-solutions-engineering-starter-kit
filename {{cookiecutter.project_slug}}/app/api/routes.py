import logging

from fastapi import APIRouter, HTTPException

from app.schemas import ExampleRequest, ExampleResponse
from app.services.llm_service import LocalMockLLMService

logger = logging.getLogger(__name__)
router = APIRouter(tags=["example"])


@router.post("/example", response_model=ExampleResponse)
def example(request: ExampleRequest) -> ExampleResponse:
    try:
        service = LocalMockLLMService()
        return service.generate_structured_response(request)
    except ValueError as exc:
        logger.exception("Validation error while processing request")
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        logger.exception("Unexpected error while processing request")
        raise HTTPException(status_code=500, detail="Unexpected processing error") from exc
