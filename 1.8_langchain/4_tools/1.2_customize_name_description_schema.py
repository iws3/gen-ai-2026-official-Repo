from langchain.tools import tool

@tool("Web_search") #overrides the auto-derived name
def search(query:str)->str:
    """
    Perform a w eb search given the folowing query
    
    Args:
        query: query to perform search
    """
    return f"Results for: {query}"

print(search.name)
    