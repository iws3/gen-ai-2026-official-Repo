# State — reading conversation history inside a tool

# scenario:** A tutoring bot needs a tool that tells the student how many questions they've asked so far this session, to nudge them ("you've asked 5 questions about loops — want a mini-quiz?").

# AGENT STATE [messages: [Human, Ai..], user_id:"user_123", ...other additional custom tools] --->your @tool

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os
from langchain.tools import tool, ToolRuntime
from langchain.agents import create_agent, AgentState
from langchain.messages import HumanMessage

load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

model=init_chat_model("google_genai:gemini-2.5-flash")

class CustomState(AgentState):
    user_id:str
    
@tool
def get_user_info(runtime:ToolRuntime)->str:
    """Look up user info."""
    user_id=runtime.state["user_id"]
    return "User is John Smith" if user_id=="user_123" else "Unknown user"

agent=create_agent(
    model=model,
    tools=[get_user_info],
    state_schema=CustomState
)


result=agent.invoke({
    "messages":"Look for user information",
    "user_id":"user_123"
})

# print(result["messages"][-1].content)
print(result)