import requests

def query_ollama(prompt: str, model: str = "mistral") -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt
        },
        stream=True
    )
    # Ollama streams JSON lines
    chunks = []
    for line in response.iter_lines():
        if line:
            chunk = line.decode("utf-8")
            # each line is a JSON object; extract the 'response' field
            import json
            chunk_json = json.loads(chunk)
            if 'response' in chunk_json:
                chunks.append(chunk_json['response'])
    return ''.join(chunks)
