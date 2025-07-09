# core/chat/chat_session.py
import asyncio
from typing import List, Tuple
from typing_extensions import TypedDict, Annotated
from langchain_openai.chat_models.base import BaseChatOpenAI
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
import os
from dotenv import load_dotenv
from ..mcp_client_manager import MCPClientManager

load_dotenv('/mnt/e/project/langgraph_mcp_agent/.env')

class State(TypedDict):
    messages: Annotated[list, add_messages]

class ChatSession:
    def __init__(self):
        self.llm = BaseChatOpenAI(
            model='deepseek-chat',
            openai_api_key=os.getenv('DEEPSEEK_API_KEY'),
            openai_api_base='https://api.deepseek.com/v1',
            max_tokens=1024,
            temperature=0
        )
        self.client = MCPClientManager(config_path='/mnt/e/project/langgraph_mcp_agent/core/mcp_server/server_config.json')
        self.graph = None
        self.tools = []
        self.llm_with_tools = None
        self.memory = MemorySaver()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._initialize_graph())

    async def _initialize_graph(self):
        self.tools = await self.client.get_tools()
        self.llm_with_tools = self.llm.bind_tools(self.tools)

        graph_builder = StateGraph(State)

        async def chatbot(state: State):
            return {"messages": [await self.llm_with_tools.ainvoke(state["messages"])]}

        graph_builder.add_node("chatbot", chatbot)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_conditional_edges("chatbot", tools_condition)
        graph_builder.add_edge("tools", "chatbot")
        graph_builder.set_entry_point("chatbot")

        self.graph = graph_builder.compile(checkpointer=self.memory)

    def get_server_info(self):
        return self.client.get_raw_config() 

    async def _stream_once(self, user_input: str) -> Tuple[str, List[str]]:
        config = {"configurable": {"thread_id": "1"}}
        trace = []
        final_response = ""
        async for event in self.graph.astream(
            {"messages": [{"role": "user", "content": user_input}]},
            config,
        ):
            for key, value in event.items():
                trace.append(f"[{key}] {value['messages'][-1].content}")
                final_response = value["messages"][-1].content
        return final_response, trace

    async def run(self, user_input: str) -> Tuple[str, List[str]]:
        return await self._stream_once(user_input)
