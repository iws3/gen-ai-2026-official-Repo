# Store — memory that survives the conversation ending

# scenario:** A student, Godbless, uses your SEEDBot on Monday and tells it "I prefer Python over JavaScript." On Wednesday, in a completely new conversation (new thread, bot has no messages from Monday), SEEDBot should still know that preference. That's what `store` is for — it is not part of any one conversation's `state`, it lives independently.
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os

from typing import Any
from langgraph.store.memory import InMemoryStore
from langchain.tools import tool, ToolRuntime
from langchain.agents import create_agent

load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

model=init_chat_model("google_genai:gemini-2.5-flash")

@tool
def save_user_info(user_id:str, user_info:dict[str, Any], runtime:ToolRuntime)->str:
    """Save user info"""
    runtime.store.put(("users",), user_id, user_info) 
    return "Successfully saved user info"

@tool
def get_user_info(user_id:str, runtime:ToolRuntime)->str:
    """Look up user info"""
    result=runtime.store.get(("users",), user_id)
    return str(result.value) if result else "Unknown user"

store=InMemoryStore()

agent=create_agent(model, tools=[save_user_info, get_user_info], store=store)