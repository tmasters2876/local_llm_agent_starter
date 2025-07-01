import requests
import json
import logging

def query_ollama(prompt: str, model: str = "llama3", temperature: float = 0.7, num_predict: int = 100) -> str:
    try:
        url = "http://ollama:11434/api/generate"
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": num_predict
            }
        }

        response = requests.post(url, headers=headers, json=payload)

        # ✅ Add raw text fallback print for debugging (optional)
        logging.info(f"[Ollama Raw Text] {response.text}")

        # ✅ Handle no content
        if not response.text.strip():
            logging.warning("Empty response from Ollama.")
            return "Standard fallback: Ollama returned empty response."

        try:
            # Preferred: parse as single JSON
            parsed = response.json()
            return parsed.get("response", "Standard fallback: Missing 'response' key.")
        except json.JSONDecodeError:
            # Fallback: try parsing line-by-line
            for line in response.text.splitlines():
                try:
                    data = json.loads(line)
                    if "response" in data:
                        return data["response"]
                except json.JSONDecodeError:
                    continue

        logging.warning("Ollama returned unparseable content.")
        return "Standard fallback: Failed to parse Ollama response."

    except Exception as e:
        logging.error(f"[query_ollama fallback] Unexpected error: {e}")
        return "Standard fallback: An unexpected error occurred."
