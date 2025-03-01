from langgraph.graph import StateGraph, START, END
from state import State
from nodes import classifier_node, response_node_llm, get_next_node

def build_router_graph() -> StateGraph:
    graph = StateGraph(State)
    graph.add_node("classifier", classifier_node)
    graph.add_node("response_llm", response_node_llm)
    graph.add_edge(START, "classifier")
    graph.add_conditional_edges("classifier", get_next_node, {"response_llm": "response_llm"})
    graph.add_edge("response_llm", END)
    chain = graph.compile()
    return chain
