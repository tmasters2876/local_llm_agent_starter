import requests

def query_ollama(prompt, model="mistral", temperature=0.7, num_predict=100):
    url = "http://ollama:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        try:
            result = response.json()
            print("🧪 Raw Ollama response:", result)  # ✅ LOG HERE
            if "message" in result and "content" in result["message"]:
                return result["message"]["content"]
            else:
                return "Standard fallback: Missing 'message' or 'content' field."

        except Exception as json_err:
            print("[query_ollama] JSON decode failed. Raw response:")
            print(response.text)
            print("Error:", json_err)
            return "Standard fallback: Ollama returned invalid JSON."

    except Exception as e:
        print("[query_ollama fallback] HTTP error:", e)
        return "Standard fallback: Unable to process your request at the moment."
