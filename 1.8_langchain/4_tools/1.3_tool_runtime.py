# A tool that only sees its declared arguments is limited. `ToolRuntime` is a special parameter, **automatically injected and hidden from the model** (it never appears in the tool's schema), that gives a tool access to everything about the running agent:



# def create_head():'
# play(football here for us as well)'
from langchain.tools import tool, ToolRuntime
from langchain.messages import HumanMessage

# @tool
# def get_last_user_message(runtime:ToolRuntime)->str:
#     """Get the most recent message from the user."""
#     messages=runtime.state["messages"]
#     for message in reversed(messages):
#         if isinstance(messages, HumanMessage):
#             return message.content
#         return "No user messages found"

from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime
from langchain.agents import create_agent
from dotenv import load_dotenv
import os
from langchain.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from langchain.chat_models import init_chat_model


load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")


model=init_chat_model("google_genai:gemini-2.5-flash");
USER_DATABASE = {
    "user123": {"name": "Alice Johnson", "account_type": "Premium", "balance": 5000},
}

@dataclass
class UserContext:
    user_id: str

@tool
def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
    """Get the current user's account information."""
    user_id = runtime.context.user_id
    user = USER_DATABASE.get(user_id)
    if user:
        return f"Account holder: {user['name']}\nBalance: ${user['balance']}"
    return "User not found"

agent = create_agent(model, tools=[get_account_info], context_schema=UserContext)
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's my balance?"}]},
    context=UserContext(user_id="user123"),   # this is what runtime.context resolves to
)
print(result)