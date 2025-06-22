from fastapi import FastAPI, Request  # ✅ fixed
from pydantic import BaseModel
from orchestrator import run_orchestration

from fastapi.middleware.cors import CORSMiddleware  # ✅ already good

app = FastAPI()

# ✅ CORS — keep as-is
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later if you wish
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str
    temperature: float = 0.7
    num_predict: int = 100
    model: str = "mistral"

@app.post("/api/ask")
async def ask(request: Request):
    body = await request.json()
    result = run_orchestration(body)
    return {"result": result}

@app.get("/")
def root():
    return {"message": "Local LLM Agent Orchestrator is running!"}
