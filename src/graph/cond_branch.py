from langgraph.graph import StateGraph

# decision function, decide next node based on length
def decide_next_node(state):
    if len(state["input"]) > 10:
        return "long_input_node"
    else:
        return "short_input_node"

# Test version (decision function):
# def decide_next_node(state):
#     print("state type:", type(state), "state:", state)
#     if isinstance(state, dict) and "input" in state:
#         if len(state["input"]) > 10:
#             return "long_input_node"
#         else:
#             return "short_input_node"
#     else:
#         raise ValueError("state must include dict of 'input'")
    
def long_input_handler(state):
    return {"result": "handled long input: " + state["input"]}

def short_input_handler(state):
    return {"result": "handled short input: " + state["input"]}

def identity_node(state):
    return state  # only return original: state

workflow = StateGraph(dict)

workflow.add_node("long_input_node", long_input_handler)
workflow.add_node("short_input_node", short_input_handler)
# workflow.add_node("decision_node", decide_next_node)
workflow.add_node("decision_node", identity_node)    # Only do data forwarding

# set conditional edge
workflow.add_conditional_edges(
    "decision_node",
    decide_next_node,
    {
        "long_input_node": "long_input_node",
        "short_input_node": "short_input_node"
    }
)
'''
    This is a dictionary listing all possible branches and 
    their corresponding target nodes. For example, if the 
    decision function returns "long_input_node", it jumps 
    to the "long_input_node" node.
'''

workflow.set_entry_point("decision_node")
workflow.set_finish_point("long_input_node") # or "short_input_node", all good

'''
           +------------------+
           |  decision_node   |
           +------------------+
                   |
         decide_next_node(state)
           |                 |
          |                   |
+------------------+   +------------------+
| long_input_node  |   | short_input_node |
+------------------+   +------------------+
'''