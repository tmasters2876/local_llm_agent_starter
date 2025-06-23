# 🚀 Local LLM Agent Orchestrator

## ✅ What this is

- Runs open-weight LLMs (Mistral, Llama 3) locally via Ollama.
- Provides a FastAPI server with a `/api/ask` endpoint.
- Uses LangGraph nodes for orchestration logic.
- React front-end for prompt submission, temperature, tokens, and model selection.
- Robust fallback: Handles invalid model, timeouts, or empty prompt safely.
- Docker Compose: spins up **Ollama** + **Orchestrator** together.

---

## ⚙️ How to Run Locally (Manual Dev)

```bash
# 1️⃣ Clone and set up Python venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2️⃣ Pull an LLM model
ollama pull mistral

# 3️⃣ Start FastAPI
uvicorn main:app --reload

# 4️⃣ Start React Frontend
cd frontend
npm install
npm start


# One command to build and run:
docker-compose up --build
