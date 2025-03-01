import subprocess
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from state import State

class OllamaLLM:
    def __init__(self, model: str):
        self.model = model

    def generate(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True,
                text=True,
                check=True
            )
            output = result.stdout.strip()
            return output if output else "No generated text available."
        except subprocess.CalledProcessError as e:
            return f"Ollama CLI error (status {e.returncode}): {e.stderr}"
        except Exception as e:
            return "Ollama error: " + str(e)

ollama_llm = OllamaLLM(model="llama3.1:8b")

def classifier_node(state: State) -> State:
    if not state["messages"]:
        return {"messages": state["messages"], "classification": "unknown"}
    last_message: BaseMessage = state["messages"][-1]
    message_text = last_message.content.lower()
    if "hello" in message_text or "hi" in message_text:
        return {"messages": state["messages"], "classification": "greeting"}
    elif "help" in message_text or "support" in message_text:
        return {"messages": state["messages"], "classification": "help"}
    elif "bye" in message_text or "goodbye" in message_text:
        return {"messages": state["messages"], "classification": "farewell"}
    return {"messages": state["messages"], "classification": "unknown"}

def response_node_llm(state: State) -> State:
    classification = state.get("classification", "unknown")
    conversation_text = " ".join(msg.content for msg in state["messages"])
    if classification == "greeting":
        prompt = "Generate a friendly greeting response based on: " + conversation_text
    elif classification == "help":
        prompt = "Generate a helpful response asking what assistance is needed, based on: " + conversation_text
    elif classification == "farewell":
        prompt = "Generate a farewell response for the user, based on: " + conversation_text
    else:
        prompt = "Generate a clarifying response asking the user to rephrase, based on: " + conversation_text
    response_text = ollama_llm.generate(prompt)
    state["messages"].append(AIMessage(content=response_text))
    return state

def report_node(state: State) -> State:
    conversation_text = "\n".join(msg.content for msg in state["messages"])
    prompt = ("Generate a comprehensive report summarizing the following conversation "
              "between a human and an AI:\n\n" + conversation_text)
    report = ollama_llm.generate(prompt)
    state["messages"].append(AIMessage(content="Final Report:\n" + report))
    return state

def get_next_node(state: State) -> str:
    return "response_llm"
