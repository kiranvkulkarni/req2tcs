SEMANTIC_PROMPT = """
You are a senior smartphone camera QA engineer.

Return ONLY valid JSON matching this schema:
{
  "screen_purpose": "",
  "primary_actions": [],
  "secondary_actions": [],
  "mandatory_components": [],
  "negative_conditions": [
    {
      "component": "",
      "condition": "",
      "expected_behavior": ""
    }
  ]
}

Components:
{components}
"""
