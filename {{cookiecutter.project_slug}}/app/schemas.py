from pydantic import BaseModel, Field


class ExampleRequest(BaseModel):
    text: str = Field(min_length=1, examples=["Summarize the invoice payment risk."])
    include_evidence: bool = True


class EvidenceItem(BaseModel):
    source: str
    excerpt: str


class ExampleResponse(BaseModel):
    answer: str
    confidence: float = Field(ge=0, le=1)
    label: str
    evidence: list[EvidenceItem] = []
    requires_human_review: bool
