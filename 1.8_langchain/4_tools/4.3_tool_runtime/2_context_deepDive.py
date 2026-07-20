# Knowing who is calling

# Context — knowing WHO is calling, immutably
# scenario:** A banking assistant. Two customers, Alice and Bob, are both chatting with the SAME agent instance at different times. The agent must never mix up whose balance it's reporting. `context` is set once, per `.invoke()` call, and is what pins down "this specific run is for Bob."

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os
from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime
from langchain.agents import create_agent

load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

model=init_chat_model("google_genai:gemini-2.5-flash")

USER_DATABASE={
    "user1123":{"name":"Alice Johnson", "account_type":"Premium", "balance":5000}
}

@dataclass
class UserContext:
    user_id:str


@tool
def get_account_info(runtime:ToolRuntime[UserContext])->str:
    """Get the current user's account information"""
    user_id=runtime.context.user_id
    user=USER_DATABASE.get(user_id)
    if user:
        return f"Account holder: {user['name']}\nBalance: ${user['balance']}"
    return "User not found"

agent=create_agent(model, tools=[get_account_info], context_schema=UserContext)

result=agent.invoke(
    {"messages":[{"role":"user", "content":"What is my balance"}]},
    context=UserContext(user_id="user123")
)


print(result)