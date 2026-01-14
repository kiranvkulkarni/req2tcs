
On-Prem LLM: Llama 3 via Ollama

Install:
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3
ollama run llama3

Endpoint:
POST http://localhost:11434/api/generate
