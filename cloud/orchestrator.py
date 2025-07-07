from langgraph_nodes import intake_node, classifier_node, summarizer_node, WorkflowState
from ollama_connector import query_ollama  # ✅ now using canonical version

# ✅ Core orchestration logic
def run_orchestration(payload):
    print("🛠️ Received payload:", payload)

    # Build initial state
    state = WorkflowState(
        prompt=payload.get("prompt", ""),
        temperature=payload.get("temperature", 0.7),
        num_predict=payload.get("num_predict", 100),
        model=payload.get("model", "llama3")
    )

    # Step 1: Intake
    state = intake_node(state)

    # Step 2: Classifier
    state = classifier_node(state)
    print("[Classifier Node] Routing to:", state.route)

    # Step 3: Route to summarizer or generator
    if state.route == "summarizer":
        state = summarizer_node(state)
    elif state.route == "generator":
        from langgraph_nodes import generator_node
        state = generator_node(state)
    else:
        state.result = "Standard fallback: Unknown route."

    return state.result or "Standard fallback: No result produced."
