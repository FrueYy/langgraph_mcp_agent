from typing_extensions import TypedDict, Annotated
from langchain_openai.chat_models.base import BaseChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dotenv import load_dotenv
from ..mcp_client_manager import MCPClientManager
import asyncio
#加载环境变量，如API_KEY等
load_dotenv('/mnt/e/project/langgraph_mcp_agent/.env')

#定义图的状态
class State(TypedDict):
    messages: Annotated[list, add_messages]

#构建图结构
class ChatSession:
    def __init__(self):
        self.llm = BaseChatOpenAI(
            model='deepseek-chat',
            openai_api_key=os.getenv('DEEPSEEK_API_KEY'),
            openai_api_base='https://api.deepseek.com/v1',
            max_tokens=1024,
            temperature=0
        )
        self.server_config_path = os.getenv('SERVER_CONFIG_PATH')
        self.client = MCPClientManager(self.server_config_path)
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
            return {"messages": [await self.llm_with_tools.ainvoke(state["messages"]) ]}

        graph_builder.add_node("chatbot", chatbot)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_conditional_edges("chatbot", tools_condition)
        graph_builder.add_edge("tools", "chatbot")
        graph_builder.set_entry_point("chatbot")

        self.graph = graph_builder.compile(checkpointer=self.memory)

    def get_server_info(self):
        return self.client.get_raw_config() 

 
 
    async def stream_with_trace(self, user_input: str):
        config = {"configurable": {"thread_id": "1"}}
        final_response = ""

        async for event in self.graph.astream(
            {"messages": [{"role": "user", "content": user_input}]},
            config,
        ):
            for node_name, node_output in event.items():
                messages = node_output.get("messages", [])

                for msg in messages:
                    if msg.type == "ai":
                        content = msg.content or "[空回复]"
                        tool_calls = msg.tool_calls or []

                        if tool_calls:
                            yield "llm_thinking", "正在思考下一步动作..."

                            for call in tool_calls:
                                tool_name = call.get("name")
                                args = call.get("args", {})
                                yield "tool_call", f"{tool_name}({args})"
                        else:
                            yield "llm_response", content
                            final_response = content

                    elif msg.type == "tool":
                        yield "tool_result", msg.content

        yield "final_response", final_response


