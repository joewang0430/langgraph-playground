from langgraph.graph import StateGraph
from graph import single_edge

def hello_node(data):
    print("Hello, LangGraph!")
    return data

if __name__ == "__main__":
    single_edge_app = single_edge.workflow.compile()
    single_edge_app.invoke({"imput": "test "})


# if __name__ == "__main__":
#     graph = StateGraph(dict)
#     graph.add_node("hello", hello_node)
#     graph.set_entry_point("hello")

#     app = graph.compile()  # Compile into a runnable object
#     app.invoke({})