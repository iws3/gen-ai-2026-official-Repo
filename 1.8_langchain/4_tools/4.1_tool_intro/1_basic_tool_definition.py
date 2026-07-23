# ___________________________________________________________________________
# Two things are doing real work here, not just decoration:

# 1. **Type hints are required.** `query: str`, `limit: int = 10` — these aren't just documentation, they generate the JSON schema the model actually sees and is constrained by when producing arguments.
# 2. **The docstring becomes the tool's description.** This is the single biggest lever you have over whether a model calls your tool at the right moment — a vague docstring produces a model that either never calls the tool or calls it inappropriately. Treat docstrings as prompt engineering, not documentation.

# Naming convention matters practically, not just stylistically: prefer `snake_case` (`web_search`, not `Web Search`) — some providers reject tool names with spaces or special characters outright.

# __________________________________________________________________]

from langchain.tools import tool


@tool
def search_database(query:str, limit:int=10)->str:
    """Search the customer database for records matching the query
    
    
    Args:
        query:search terms to look for
        limit:Maximum number of results to return
    
    """
    return f"Found {limit} results for '{query}"
    
    