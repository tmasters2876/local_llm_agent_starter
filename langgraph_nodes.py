# langgraph_nodes.py

from langgraph.graph import StateGraph, END
from pydantic import BaseModel

from ollama_connector import query_ollama

# ✅ 1️⃣ Define the State schema
class WorkflowState(BaseModel):
    prompt: str
    result: str | None = None
    route: str | None = None  # For classifier output

# ✅ 2️⃣ Intake Node
def intake_node(state: WorkflowState) -> WorkflowState:
    print(f"[Intake Node] Received: {state.prompt}")
    return state

# ✅ 3️⃣ Classifier Node
def classifier_node(state: WorkflowState) -> WorkflowState:
    if "summarize" in state.prompt.lower():
        state.route = "summarizer"
    else:
        state.route = "generator"
    print(f"[Classifier Node] Routing to: {state.route}")
    return state

# ✅ 4️⃣ Condition Function for conditional edges
def route_condition(state: WorkflowState) -> str:
    return state.route

# ✅ 5️⃣ Summarizer Node
def summarizer_node(state: WorkflowState) -> WorkflowState:
    prompt = f"Please provide a concise summary:\n{state.prompt}"
    print(f"[Summarizer Node] Prompt: {prompt}")
    state.result = query_ollama(prompt, model="mistral")
    return state

# ✅ 6️⃣ Generator Node
def generator_node(state: WorkflowState) -> WorkflowState:
    prompt = f"Please expand creatively:\n{state.prompt}"
    print(f"[Generator Node] Prompt: {prompt}")
    state.result = query_ollama(prompt, model="mistral")
    return state

# ✅ 7️⃣ Build Graph
def build_graph():
    graph = StateGraph(state_schema=WorkflowState)

    graph.add_node("intake", intake_node)
    graph.add_node("classifier", classifier_node)
    graph.add_node("summarizer", summarizer_node)
    graph.add_node("generator", generator_node)

    graph.set_entry_point("intake")
    graph.add_edge("intake", "classifier")

    # ✅ Correct for langgraph 0.4+
    graph.add_conditional_edges(
        "classifier",
        route_condition,
        {
            "summarizer": "summarizer",
            "generator": "generator"
        }
    )

    graph.add_edge("summarizer", END)
    graph.add_edge("generator", END)

    return graph.compile()
