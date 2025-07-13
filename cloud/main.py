from fastapi import FastAPI, Request
from pydantic import BaseModel
from orchestrator import run_orchestration
from fastapi.middleware.cors import CORSMiddleware
from ollama_connector import query_ollama

# ✅ Create FastAPI app
app = FastAPI()

# ✅ CORS middleware — configured once
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔒 Restrict to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# ✅ Root welcome endpoint
@app.get("/")
def root():
    return {"message": "Local LLM Agent Orchestrator is running!"}

# ✅ Input model (optional but matches expected POST schema)
class PromptRequest(BaseModel):
    prompt: str
    temperature: float = 0.7
    num_predict: int = 100
    model: str = "gemma:2b"

# ✅ Main orchestration endpoint
@app.post("/api/ask")
async def ask(request: Request):
    body = await request.json()
    result = run_orchestration(body)
    return {"result": result}

# ✅ Direct model-only endpoint for debugging
@app.post("/api/ask/test_direct")
async def test_direct(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")
    model = body.get("model", "gemma:2b")
    result = query_ollama(prompt, model=model)
    return {"result": result}
