# These are the three ways to actually run a model, and picking the right one is mostly about UX and throughput tradeoffs


# Throughput is the amount of work, material, or data that a system processes, produces, or handles within a specific timeframe. It measures overall efficiency and capacity, representing the rate at which items move from input to output


# Throughput is the amount of work, material, or data that a system processes, produces, or handles within a specific timeframe. It measures overall efficiency and capacity, representing the rate at which items move from input to output





from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
# import tools to use
from langchain.tools import tool
load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")


model=init_chat_model("google_genai:gemini-2.5-flash");

response=model.invoke("Why do parrots have colorful feathers")
print(response.text)


# Blocks until the full response is generated, then returns a single `AIMessage`. Use it for: batch jobs, background processing, anything where partial output has no value to show a user.














