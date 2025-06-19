from ollama_connector import query_ollama

async def orchestrate_task(prompt: str, temperature: float, num_predict: int, model: str) -> str:
    result = query_ollama(
        prompt=prompt,
        temperature=temperature,
        num_predict=num_predict,
        model=model  # ✅ pass through
    )
    return result
