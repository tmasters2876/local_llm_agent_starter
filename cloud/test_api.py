import requests
import json

url = "http://localhost:8000/api/ask"
payload = {
    "prompt": "Summarize LangGraph",
    "model": "llama3",
    "temperature": 0.7,
    "num_predict": 100
}

response = requests.post(url, json=payload)
print(f"Status Code: {response.status_code}")

# Print raw text to debug
print("Raw Text:", response.text)

try:
    result = response.json()
    print("Parsed JSON:", result)
except json.JSONDecodeError as e:
    print("JSON parse error:", e)

input("Press Enter to exit...")
