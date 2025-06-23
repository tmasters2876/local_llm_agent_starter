import os
import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

def query_ollama(prompt, model="mistral", temperature=0.7, num_predict=100):
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "temperature": temperature,
                "num_predict": num_predict,
                "stream": False  # force one JSON block
            },
            timeout=120  # ✅ more room for slow local CPU
        )
        response.raise_for_status()
        result = response.json()["response"]
        return result
    except Exception as e:
        print(f"[query_ollama fallback] Error: {e}")
        return "Standard fallback: Unable to process your request at the moment."
