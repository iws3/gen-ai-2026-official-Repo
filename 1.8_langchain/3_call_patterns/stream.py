from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
# import tools to use
from langchain.tools import tool
load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")


model=init_chat_model("google_genai:gemini-2.5-flash");


for chunk in model.stream("why do parrots have colorful feathers? "):
    print(chunk.text, end="|", flush=True)