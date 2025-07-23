from langgraph.graph import StateGraph

def hello_node(data):
    print("Hello, LangGraph!")
    return data

if __name__ == "__main__":
    graph = StateGraph(dict)
    graph.add_node("hello", hello_node)
    graph.set_entry_point("hello")

    app = graph.compile()  # Compile into a runnable object
    app.invoke({})