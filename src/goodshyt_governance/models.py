from pydantic import BaseModel, Field

class EvaluationRequest(BaseModel):
    subject: str = Field(min_length=1)
    content: str = Field(min_length=1)
    context: str = ""

class PolicyBundle(BaseModel):
    prohibited_phrases: list[str]
    risky_phrases: list[str]
    require_disclosure_for: list[str]

class Finding(BaseModel):
    code: str
    severity: str
    message: str

class EvaluationResponse(BaseModel):
    approved: bool
    risk_score: float = Field(ge=0.0, le=1.0)
    findings: list[Finding]
    recommendations: list[str]
