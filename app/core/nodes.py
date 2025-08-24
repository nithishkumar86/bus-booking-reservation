from app.core.states import State
from app.core.LLM import ModelLoader
from langchain_core.prompts import ChatPromptTemplate
from app.core.prompt_library import PROMPT_TEMPLATES1,PROMPT_TEMPLATES2
from langgraph.graph import MessagesState
from app.Tools.custom_tools import bind_tools
from app.common.logger import get_logger

logger = get_logger(__name__)

class Agents:
    def __init__(self):
        self.llm=ModelLoader().model_loading()
        self.logger = get_logger(__name__)
        self.logger.info("model initialized in the agent")
  
    def assistants(self,state:State):
        prompt=ChatPromptTemplate.from_messages(
            [
                ("system",PROMPT_TEMPLATES2["prompt2"]),
                ("user","Here is the question {messages}")
            ]
        )
        chain=prompt|bind_tools
        response=chain.invoke({'messages':state["messages"]})
        self.logger.info(f"assitant node finised his work and the response is : {response}")
        return {"messages":[response]}