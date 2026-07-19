import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
load_dotenv()

# os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
model=init_chat_model("google_genai:gemini-2.5-flash")

from pydantic import BaseModel, Field
from typing import List

class Actor(BaseModel):
    name:str
    role:str
    
class MovieDetails(BaseModel):
    title:str
    year:int
    cast:list[Actor]
    genres:list[str]
    budget:float | None=Field(description="Millions in FCFA")
    youtube_link:str=Field(description="Youtube Link that is actually clickable")
    
# model_with_structured_output=model.with_structured_output(MovieDetails)
# response1= model_with_structured_output.invoke("Please give me top 30 cameroonina movies")

# To actually get the list: CREATE THE WRAPPER (this is the secret sauce)
class MovieDatabase(BaseModel):
    """A collection of Cameroonian cinema data"""
    movies:List[MovieDetails]=Field(description="A list of movies, Ensure there are exactly 30")
structured_output=model.with_structured_output(MovieDatabase)
response1=structured_output.invoke("Provide a list of top 10 Camseroonian Movies")
print(response1)

print(f"Foubd {len(response1.movies)} Movies")
    
