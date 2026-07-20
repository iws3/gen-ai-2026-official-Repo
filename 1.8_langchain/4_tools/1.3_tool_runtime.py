# A tool that only sees its declared arguments is limited. `ToolRuntime` is a special parameter, **automatically injected and hidden from the model** (it never appears in the tool's schema), that gives a tool access to everything about the running agent:



# def create_head():'
# play(football here for us as well)'
from langchain.tools import tool, ToolRuntime
from langchain.messages import HumanMessage

@tool
def get_last_user_message(runtime:ToolRuntime)->str:
    """Get the most recent message from the user."""
    messages=runtime.state["messages"]
    for message in reversed(messages):
        if isinstance(messages, HumanMessage):
            return message.content
        return "No user messages found"