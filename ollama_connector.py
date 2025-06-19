import requests
import json

def query_ollama(prompt: str, model: str = "mistral",
                  temperature: float = 0.7, num_predict: int = 100) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "options": {
                "temperature": temperature,
                "num_predict": num_predict
            }
        },
        stream=True
    )

    chunks = []
    for line in response.iter_lines():
        if line:
            chunk = line.decode("utf-8")
            chunk_json = json.loads(chunk)
            if 'response' in chunk_json:
                chunks.append(chunk_json['response'])
    return ''.join(chunks)
