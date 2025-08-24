from typing_extensions import Annotated,TypedDict,Literal,List
from pydantic import BaseModel,Field
from langgraph.graph import add_messages
from app.core.LLM import ModelLoader


llm=ModelLoader().model_loading()

class Details(TypedDict):
    seat_no: int
    passenger_name: str
    source: str
    destination: str
    date_input: str

# class Detail(BaseModel):
#     seat_no: int
#     passenger_name: str
#     source: str
#     destination: str
#     date_input: Annotated[str,Field(description="from the user input parse dateformat and time",examples=['2025-06-10 12:00:00'])]


class State(TypedDict):
    messages: Annotated[List,add_messages]
    detail: List[Details]