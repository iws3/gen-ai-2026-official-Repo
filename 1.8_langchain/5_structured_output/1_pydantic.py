# hello structured output:
# Models cn be required to provide their response in aformat matching a givenschema, this is useful for ensuring the output can be easily parsed and used in subsequent processing. Langchain support multiple schema types and methods for enforcing structured output

# working with pydantic here
# Pydantic models provide the richest features set with field validation , description, and nested structure

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
load_dotenv()

# os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
model=init_chat_model("google_genai:gemini-2.5-flash")

# create a simple movie structure
class Movie(BaseModel):
    title:str=Field(description="The title of the movie")
    year:int=Field(description="The year the movie was released")
    director:str=Field(description="The director of the movie")
    rating:float=Field(description="The movies rating out of 10")
    
# do 3 more types and give students exercise
model_with_structure=model.with_structured_output(Movie)

# get the response from llm

# response1=model.invoke("Provide me the details of the movie: The fisherman diary")
response2=model_with_structure.invoke("Provide me the details of the movie: The fisherman diary")
print(response2.title)
# print(model_with_structure)