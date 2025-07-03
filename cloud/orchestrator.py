import requests
from langgraph_nodes import intake_node, classifier_node, summarizer_node, WorkflowState

# ✅ PATCHED: Correct Ollama query to avoid 404 errors + safe fallback
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
            return result.get("message", {}).get("content", "[Ollama returned no content]")
        except Exception as json_err:
            print("[query_ollama] JSON decode failed. Raw response:")
            print(response.text)
            print("Error:", json_err)
            return "Standard fallback: Ollama returned invalid JSON."

    except Exception as e:
        print("[query_ollama fallback] HTTP error:", e)
        return "Standard fallback: Unable to process your request at the moment."


# ✅ Core orchestration logic
def run_orchestration(payload):
    print("🛠️ Received payload:", payload)

    # Build initial state
    state = WorkflowState(
        prompt=payload.get("prompt", ""),
        temperature=payload.get("temperature", 0.7),
        num_predict=payload.get("num_predict", 100),
        model=payload.get("model", "mistral")
    )

    # Step 1: Intake
    state = intake_node(state)

    # Step 2: Classifier
    state = classifier_node(state)
    print("[Classifier Node] Routing to:", state.route)

    # Step 3: Route to summarizer or generator (not used yet)
    if state.route == "summarizer":
        state = summarizer_node(state)
    elif state.route == "generator":
        from langgraph_nodes import generator_node
        state = generator_node(state)
    else:
        state.result = "Standard fallback: Unknown route."

    return state.result or "Standard fallback: No result produced."
