# Local LLM Agent Orchestrator (Milestone v1)

## ✅ What this is
- Runs open-weight Mistral & Llama 3 locally via Ollama.
- FastAPI server with `/api/ask` endpoint.
- Handles streamed JSON properly.
- Ready to plug in LangGraph agent orchestration.

## ⚡ How to run
```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Pull a model
ollama pull mistral

# Run FastAPI
uvicorn main:app --reload
end


# Local LLM Agent Orchestrator

## ✅ What this does
- Runs Mistral/Llama 3 locally via Ollama
- FastAPI server for orchestration
- React front-end with dynamic temperature & token control

## ⚡ How to run

### 1️⃣ Backend
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
ollama pull mistral
uvicorn main:app --reload


cd frontend
npm install
npm start



---

### ✅ **5️⃣ Double-check your Git status**
In VS Code sidebar or terminal:
```bash
git status
