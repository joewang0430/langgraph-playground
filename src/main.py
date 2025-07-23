from langgraph.graph import StateGraph
from graph import single_edge, cond_branch

def hello_node(data):
    print("Hello, LangGraph!")
    return data


# if __name__ == "__main__":
#     app = single_edge.workflow.compile()
#     final_state = app.invoke({"imput": "test "})
#     print("Final result: ", final_state)


# for cond_branch test
if __name__ == "__main__":
    app = cond_branch.workflow.compile()
    # result = app.invoke({"input": "short"})
    result = app.invoke({"input": "longlonglonglong"})
    print(result)


# if __name__ == "__main__":
#     graph = StateGraph(dict)
#     graph.add_node("hello", hello_node)
#     graph.set_entry_point("hello")

#     app = graph.compile()  # Compile into a runnable object
#     app.invoke({})