from .models import EvaluationRequest, EvaluationResponse
from .policies import load_default_policy
from .rules import run_rules

class GovernanceService:
    def evaluate(self, payload: EvaluationRequest) -> EvaluationResponse:
        findings = run_rules(payload, load_default_policy())
        risk = min(1.0, round(sum(0.45 if f.severity == "high" else 0.2 for f in findings), 3))
        approved = risk < 0.5
        recommendations: list[str] = []
        if findings:
            recommendations.append("Revise wording to remove risky or prohibited phrases.")
        if any(f.code == "missing_disclosure" for f in findings):
            recommendations.append("Add a clear disclosure statement.")
        if not findings:
            recommendations.append("No governance blockers detected.")
        return EvaluationResponse(approved=approved, risk_score=risk, findings=findings, recommendations=recommendations)
