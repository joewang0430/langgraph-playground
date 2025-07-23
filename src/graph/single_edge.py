from langgraph.graph import StateGraph

def node_1(state):
    print("exe node 1")
    return {"result": state["imput"] + "passed node 1 exe"}

def node_2(state):
    print("exe node 2")
    return {"result": state["result"] + "then passed node 2 exe"}

# create workfow
workflow = StateGraph(dict)

# add node
workflow.add_node("node_1", node_1)
workflow.add_node("node_2", node_2)

# add edge
workflow.add_edge("node_1", "node_2")

# set entry and exit
workflow.set_entry_point("node_1")
workflow.set_finish_point("node_2")
