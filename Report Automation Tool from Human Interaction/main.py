from langchain_core.messages import AIMessage, HumanMessage
from router import build_router_graph
from nodes import report_node
from state import State

def interactive_chat():
    chain = build_router_graph()
    # Print the ASCII diagram of the graph
    print("Graph Flowchart:")
    print(chain.get_graph().draw_ascii())
    
    conversation_state: State = {"messages": [], "classification": ""}
    print("Interactive Chat. Type 'report' to generate a conversation report, or 'quit' to exit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        elif user_input.lower() == "report":
            conversation_state = report_node(conversation_state)
            print("AI:", conversation_state["messages"][-1].content)
            print("-" * 40)
            continue
        conversation_state["messages"].append(HumanMessage(content=user_input))
        conversation_state = chain.invoke(conversation_state)
        ai_response = conversation_state["messages"][-1].content
        print("AI:", ai_response)
        print("-" * 40)

if __name__ == "__main__":
    interactive_chat()
