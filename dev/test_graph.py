# test_graph.py

from langgraph_nodes import build_graph
from langgraph.graph import END

graph = build_graph()

result = graph.invoke({"prompt": "Can you summarize LangGraph's purpose?"})
print(f"\n[Final Result] {result}")
