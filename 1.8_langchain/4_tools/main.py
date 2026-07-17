from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
# import tools to use
from langchain.tools import tool
load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")


model=init_chat_model("google_genai:gemini-2.5-flash");

print(model)

@tool
def get_weather(location:str)->str:
    """Get the weather at a location"""
    return f"It's sunny in {location}"

# tallking About tools in genai'


model_with_tools=model.bind_tools(get_weather)
print(model_with_tools)


response=model_with_tools.invoke("What is the Weather like in Boston")

for tool_call in response.tool_calls:
    # view tool calls made b the model
    print(f"Tool:{tool_call['name']}")
    print(f"args: {tool_call['args']}")
    # print(f"Tool call dictionary is: {response}")
    


# def get_weather(city:str)->str:
#     """ Get a weather for a city. """
#     return f"The weather in {city} is sunny."


# agent=create_agent(
#     model="gemini-2.5-flash",
#     tools=[get_weather],
#     system_prompt="You are a helpful assistant."
# )
# print(agent)


# TOOL EXECUTION LOOP

# STEP 1: Model generate tool calls
messages=[{
    "role":"user",
    "content":"What is the weather in Boston"
}]

ai_msg=model_with_tools.invoke(messages)
messages.append(ai_msg)


# step 2: execute tools and collect reults
for tool_Call in ai_msg.tool_calls:
    # Execute the tool with tool with the generated arguments
    tool_result=get_weather.invoke(tool_Call)
    messages.append(tool_result)
# step 3: pass the results back to the model for final response

final_response=model_with_tools.invoke(messages)

print(f"final response: {final_response.text}")
print(messages)


# started working with tools