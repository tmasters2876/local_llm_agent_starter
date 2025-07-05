import requests

def query_ollama(prompt, model="mistral", temperature=0.7, num_predict=100):
    url = "http://ollama:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        try:
            result = response.json()
            if "response" in result:
                return result["response"]
            else:
                print("[query_ollama] Unexpected response format:", result)
                return "Standard fallback: Missing 'response' key."
        except Exception as json_err:
            print("[query_ollama] JSON decode failed. Raw response:")
            print(response.text)
            print("Error:", json_err)
            return "Standard fallback: Ollama returned invalid JSON."

    except Exception as e:
        print("[query_ollama fallback] HTTP error:", e)
        return "Standard fallback: Unable to process your request at the moment."

