
SEMANTIC_PROMPT = '''
Return ONLY valid JSON.
Schema:
{
  "screen_purpose": "",
  "primary_actions": [],
  "secondary_actions": [],
  "mandatory_components": [],
  "negative_conditions": [
    {"component":"","condition":"","expected_behavior":""}
  ]
}
Components:
{components}
'''
