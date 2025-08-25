from app.core.states import State
from langgraph.graph import StateGraph,START,END
from app.core.nodes import Agents
from app.Tools.custom_tools import tool_node
from langgraph.prebuilt import tools_condition
from langgraph.checkpoint.memory import MemorySaver
from app.common.logger import get_logger

class GraphBuilder:
    def __init__(self):
        self.graph=StateGraph(State)
        self.obj=Agents()
        self.memory=MemorySaver()
        self.logger = get_logger(__name__)
        self.logger.info("graph initialization takes placed")

    def graph_initializing(self):
        self.graph.add_node("assistant",self.obj.assistants)
        self.graph.add_node("tools",tool_node)
        self.graph.add_edge(START,"assistant")
        self.graph.add_conditional_edges("assistant",
                                         tools_condition,
                                         {
                                             "tools",
                                             END
                                         }
        )

        self.graph.add_edge("tools",END)
        self.logger.info("graph initializated successfully")
        return self.graph.compile(checkpointer=self.memory)

    def graph_retrieval(self):
        self.logger.info("graph successfully retrieved")
        return self.graph_initializing()

            
