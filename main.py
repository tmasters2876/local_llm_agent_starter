from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import orchestrate_task

from fastapi.middleware.cors import CORSMiddleware  # ✅ Add this

app = FastAPI()

# ✅ Add CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str
    temperature: float = 0.7
    num_predict: int = 100
    model: str = "mistral"  # ✅ NEW: allow passing model name

@app.post("/api/ask")
async def ask(request: PromptRequest):
    output = await orchestrate_task(
        prompt=request.prompt,
        temperature=request.temperature,
        num_predict=request.num_predict,
        model=request.model
    )
    return {"result": output}

@app.get("/")
def root():
    return {"message": "Local LLM Agent Orchestrator is running!"}
