from langchain.tools import tool
from pydantic import BaseModel, Field
from typing import Literal

@tool("Web_search") #overrides the auto-derived name
def search(query:str)->str:
    """
    Perform a w eb search given the folowing query
    
    Args:
        query: query to perform search
    """
    return f"Results for: {query}"

print(search.name)

@tool("calculator", description="Peform  arithmetic calculation, Use this for any math problem")
def calc(expression:str)->str:
    """
    Evaluate mathematical expressions
    
    """
    return str(eval(expression))

# For anything beyond simple scalar args, define the schema explicitly with Pydantic — this gets you validation, defaults, and per-field descriptions the model can use to fill arguments correctly:


class WeatherInput(BaseModel):
    """Input for weather queries."""
    location:str=Field(description="City name or coordinate")
    units:Literal["celcius", "fahrenheit"]=Field(
        default="celcius",
        description="Temperature unit prefered"
    )
    include_forecast:bool=Field(default=False, description="Include 5-day forecast")


@tool(args_schema=WeatherInput)
def get_weather(location:str, units:str="celcius", include_forecast:bool=False):
    """Get current weather and optional forecast"""
    temp=22 if units=="celcius" else 72
    result=f"Current weather in {location}: {temp} degrees {units[0].upper()}"
    if include_forecast:
        result+="\Next 5 days: Sunny"
    return result
    


    
    