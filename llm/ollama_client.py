import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


class LLMError(Exception):
    pass


def call_llm(prompt: str) -> dict:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
    except requests.RequestException as e:
        raise LLMError(f"Ollama request failed: {e}")

    raw = response.json().get("response", "").strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        raise LLMError(f"Invalid JSON from LLM:\n{raw}")
