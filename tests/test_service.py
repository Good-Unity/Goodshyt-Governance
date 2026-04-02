from goodshyt_governance.models import EvaluationRequest
from goodshyt_governance.service import GovernanceService

def test_risky_language_gets_flagged() -> None:
    service = GovernanceService()
    response = service.evaluate(EvaluationRequest(subject="ad copy", content="This is guaranteed and risk free", context="sponsored post"))
    assert response.approved is False
    assert response.risk_score > 0
    assert response.findings
