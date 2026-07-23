# nested  typedic models

from typing_extensions import TypedDict, Annotated

class Actor(TypedDict):
    name:Annotated[str, ""]