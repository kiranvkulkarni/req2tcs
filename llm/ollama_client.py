
import requests, json
OLLAMA_URL='http://localhost:11434/api/generate'
MODEL='llama3'
def call_llm(prompt):
    r=requests.post(OLLAMA_URL,json={'model':MODEL,'prompt':prompt,'stream':False},timeout=60)
    r.raise_for_status()
    return json.loads(r.json()['response'])
