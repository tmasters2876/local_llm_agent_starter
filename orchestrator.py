from ollama_connector import query_ollama

# Example orchestration: just echo for now
async def orchestrate_task(prompt: str) -> str:
    # Here you could add LangGraph agent steps
    result = query_ollama(prompt)
    return result
