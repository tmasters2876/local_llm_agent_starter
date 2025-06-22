from langgraph.graph import StateGraph, END
from pydantic import BaseModel

from ollama_connector import query_ollama

# ✅ Extended WorkflowState — source of truth
class WorkflowState(BaseModel):
    prompt: str
    result: str | None = None
    route: str | None = None
    temperature: float = 0.7
    num_predict: int = 100
    model: str = "mistral"

# ✅ Intake Node
def intake_node(state: WorkflowState) -> WorkflowState:
    print(f"[Intake Node] Received: {state.prompt}")
    return state

# ✅ Classifier Node
def classifier_node(state: WorkflowState) -> WorkflowState:
    if "summarize" in state.prompt.lower():
        state.route = "summarizer"
    else:
        state.route = "generator"
    print(f"[Classifier Node] Routing to: {state.route}")
    return state

# ✅ Condition function
def route_condition(state: WorkflowState) -> str:
    return state.route

# ✅ Summarizer Node — now passes all params
def summarizer_node(state: WorkflowState) -> WorkflowState:
    prompt = f"Please provide a concise summary:\n{state.prompt}"
    print(f"[Summarizer Node] Prompt: {prompt}")
    state.result = query_ollama(
        prompt,
        model=state.model,
        temperature=state.temperature,
        num_predict=state.num_predict
    )
    return state

# ✅ Generator Node — now passes all params
def generator_node(state: WorkflowState) -> WorkflowState:
    prompt = f"Please expand creatively:\n{state.prompt}"
    print(f"[Generator Node] Prompt: {prompt}")
    state.result = query_ollama(
        prompt,
        model=state.model,
        temperature=state.temperature,
        num_predict=state.num_predict
    )
    return state

# ✅ Build the LangGraph
def build_graph():
    graph = StateGraph(state_schema=WorkflowState)

    graph.add_node("intake", intake_node)
    graph.add_node("classifier", classifier_node)
    graph.add_node("summarizer", summarizer_node)
    graph.add_node("generator", generator_node)

    graph.set_entry_point("intake")
    graph.add_edge("intake", "classifier")
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
