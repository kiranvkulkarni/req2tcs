
import json
from llm.prompts import SEMANTIC_PROMPT
from llm.ollama_client import call_llm
def enrich(screen):
    labels=sorted({c.label for s in screen.states for c in s.components})
    try:
        screen.semantics=call_llm(SEMANTIC_PROMPT.format(components=json.dumps(labels)))
    except Exception:
        screen.semantics={}
    return screen
