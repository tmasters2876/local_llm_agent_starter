from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import orchestrate_task

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    temperature: float = 0.7  # default if not provided
    num_predict: int = 100    # default if not provided

@app.post("/api/ask")
async def ask(request: PromptRequest):
    output = await orchestrate_task(
        prompt=request.prompt,
        temperature=request.temperature,
        num_predict=request.num_predict
    )
    return {"result": output}

@app.get("/")
def root():
    return {"message": "Local LLM Agent Orchestrator is running!"}
