from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import orchestrate_task

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/api/ask")
async def ask(request: PromptRequest):
    output = await orchestrate_task(request.prompt)
    return {"result": output}

@app.get("/")
def root():
    return {"message": "Local LLM Agent Orchestrator is running!"}
