from fastapi import FastAPI
from .models import EvaluationRequest
from .policies import load_default_policy
from .service import GovernanceService

app = FastAPI(title="GoodShyt Governance", version="0.1.0")
service = GovernanceService()

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "goodshyt-governance"}

@app.get("/policies/default")
def default_policy() -> dict[str, object]:
    return load_default_policy().model_dump()

@app.post("/evaluate")
def evaluate(payload: EvaluationRequest) -> dict[str, object]:
    return service.evaluate(payload).model_dump()
