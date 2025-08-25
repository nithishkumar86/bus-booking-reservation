from typing_extensions import Annotated,TypedDict,Literal,List
from pydantic import BaseModel,Field
from langgraph.graph import add_messages
from app.core.LLM import ModelLoader



class State(TypedDict):
    messages: Annotated[List,add_messages]