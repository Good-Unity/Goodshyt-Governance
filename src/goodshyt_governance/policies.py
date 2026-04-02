import yaml
from .models import PolicyBundle

DEFAULT_POLICY_YAML = '''
prohibited_phrases:
  - guaranteed returns
  - no risk
  - impossible to fail
risky_phrases:
  - guaranteed
  - risk free
  - secret trick
  - exploit
  - bypass
require_disclosure_for:
  - sponsored
  - affiliate
  - ad
'''

def load_default_policy() -> PolicyBundle:
    data = yaml.safe_load(DEFAULT_POLICY_YAML)
    return PolicyBundle.model_validate(data)
