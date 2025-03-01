# Human_AI_Interaction-Report-Generation-Agent
This agent aims to create a detailed report based on an unstructured information flow, such as a conversation between a human and an AI. This project implements an interactive chatbot using LangGraph with a locally running LLM (Ollama model "llama3.1:8b"). The chatbot classifies user inputs, generates responses, and can produce a final report summarizing the conversation. You may use a LLM model of your choice.

## Overview

### State Management:
The conversation state is maintained using a simple dictionary that stores the conversation messages and a classification label.

### Graph Workflow:
The system uses LangGraph to build a chain of nodes that:
Classify the last user message.
Generate a response using the local Ollama LLM.
Optionally, generate a final report summarizing the conversation.
Local LLM Integration:
The project leverages the local Ollama CLI to run the model without relying on an external REST endpoint.

### Prerequisites

Python 3.8 or later
Ollama installed and running locally with the model llama3.1:8b
Ensure the ollama CLI is in your system’s PATH

Required Python packages (install via pip):
pip install langgraph langchain-core langchain
Project Structure

The repository includes the following key files:

state.py: Defines the conversation state schema.
nodes.py: Contains the node functions and the Ollama LLM integration.
router.py: Builds the LangGraph workflow by connecting the nodes.
main.py: Implements an interactive REPL for conversation and report generation.
Setup & Installation

Clone the Repository:
git clone <repository-url>
cd <repository-folder>
Install Dependencies:
pip install langgraph langchain-core langchain
Ensure Ollama is Running:
Verify that your local Ollama server is running and that the model llama3.1:8b is available.
Running the Project

To start the interactive chatbot, run:

python main.py
Interactive Chat:
The chatbot will prompt you for input.
Generate a Report:
Type report at any time to generate and display a comprehensive report summarizing the conversation so far.
Exit:
Type quit or exit to end the session.
How It Works

State Initialization:
The state is initialized as a dictionary that holds the conversation messages and the current classification.
Classification Node:
The classifier_node examines the last user message and assigns a classification (e.g., greeting, help, farewell).
Response Generation:
The response_node_llm builds a prompt based on the conversation history and classification, then calls the local Ollama model using the CLI to generate a response.
Graph Flow:
The nodes are connected using LangGraph. The flow is:
START → classifier_node → (conditional routing) → response_node_llm → END
Report Generation:
When the user types report, the report_node aggregates the conversation and uses the LLM to generate a comprehensive summary.
Visualizing the Graph

You can also visualize your graph flowchart by calling the built‑in visualization methods in LangGraph. For example, to view the Mermaid diagram of the graph, you can add the following snippet in your main.py (or another dedicated script) before entering the interactive loop:

chain = build_router_graph()
print(chain.get_graph().draw_mermaid())
Copy the output and paste it into a Mermaid Live Editor for a graphical view.

Additional Information

Local LLM Integration:
The project uses the ollama CLI to generate text locally. The OllamaLLM class wraps the command-line call and returns the model's output.
State and Node Functions:
The state is maintained as a dictionary and passed between nodes, ensuring a consistent data structure across the pipeline.
Future Enhancements:
You might consider adding more nuanced routing based on additional metrics, such as confidence scores or custom logic.
