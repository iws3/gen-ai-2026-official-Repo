# Typedict provides a simple alternative using ython's built in typing : ideal when you dont need runtime validation

#  Typedict create  a simple dictionary so we dont need runtime validation - pydantic will have a run time validation

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
load_dotenv()

# os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
model=init_chat_model("google_genai:gemini-2.5-flash")

from typing_extensions import TypedDict, Annotated
class MovieDict(TypedDict):
    """A movie with details"""
    title:Annotated[str, "The title of the movie"]
    year:Annotated[int, "The year the movie was released"]
    direction:Annotated[str, "The director of the moviee"]
    ratings:Annotated[float, "The movie's rating out of 2"]
    
    
model_typedict=model.with_structured_output(MovieDict)

res=model_typedict.invoke(model_typedict)
print(res)   
    