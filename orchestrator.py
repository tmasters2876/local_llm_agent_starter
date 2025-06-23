from langgraph_nodes import build_graph, WorkflowState

def run_orchestration(payload):
    graph = build_graph()
    state = WorkflowState(
        prompt=payload["prompt"],
        temperature=payload.get("temperature", 0.7),
        num_predict=payload.get("num_predict", 100),
        model=payload.get("model", "mistral")
    )
    output = graph.invoke(state)
    return output["result"]  # ✅ Correct and robust
