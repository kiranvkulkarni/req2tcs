import json
from llm.prompts import SEMANTIC_PROMPT
from llm.ollama_client import call_llm


def enrich_screen(screen):
    labels = sorted(
        {c.label for s in screen.states for c in s.components}
    )

    if not labels:
        return screen

    try:
        prompt = SEMANTIC_PROMPT.format(
            components=json.dumps(labels)
        )
        screen.semantics = call_llm(prompt)
    except Exception:
        # Fail-safe: semantics optional
        screen.semantics = {}

    return screen
