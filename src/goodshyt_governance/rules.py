from .models import EvaluationRequest, Finding, PolicyBundle

def run_rules(payload: EvaluationRequest, policy: PolicyBundle) -> list[Finding]:
    lowered = payload.content.lower()
    findings: list[Finding] = []

    for phrase in policy.prohibited_phrases:
        if phrase in lowered:
            findings.append(Finding(code="prohibited_phrase", severity="high", message=f"Content includes prohibited phrase: {phrase}"))

    for phrase in policy.risky_phrases:
        if phrase in lowered:
            findings.append(Finding(code="risky_phrase", severity="medium", message=f"Content includes risky phrase: {phrase}"))

    context_lower = payload.context.lower()
    if any(marker in context_lower for marker in policy.require_disclosure_for):
        if "disclosure" not in lowered and "sponsored" not in lowered and "affiliate" not in lowered:
            findings.append(Finding(code="missing_disclosure", severity="medium", message="Context suggests disclosure should be present."))

    return findings
