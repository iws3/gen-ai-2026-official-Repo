from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# add_messages is called reducers


class State(TypedDict):
    messages:Annotated[list, add_messages]
    

graph_builder=StateGraph(State)

print(graph_builder)