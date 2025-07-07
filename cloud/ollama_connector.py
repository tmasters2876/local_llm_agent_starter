import requests

def query_ollama(prompt, model="llama3", temperature=0.7, num_predict=100):
    url = "http://ollama:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        # Chat format returns .message.content
        if "message" in result and "content" in result["message"]:
            return result["message"]["content"]
        else:
            print("[query_ollama] Unexpected chat response:", result)
            return "Standard fallback: Invalid chat format."

    except Exception as e:
        print("[query_ollama fallback] HTTP error:", e)
        return "Standard fallback: Unable to process your request at the moment."


