# A message is a structured object with three parts: **role** (system/user/assistant/tool), **content** (text, images, files, etc.), and **metadata** (token usage, IDs).


from dotenv import load_dotenv
import os
from langchain.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from langchain.chat_models import init_chat_model


load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")


model=init_chat_model("google_genai:gemini-2.5-flash");


messages=[
    SystemMessage("You are a helpful assistant that translate English to French"),
    HumanMessage("Translate: I love programming"),
    AIMessage("J'adore la programming"),
    HumanMessage("Translate : I love building applications"),
]

response=