import os
import asyncio
from typing import Annotated, TypedDict
from dotenv import load_dotenv
from langchain_openai.chat_models.base import BaseChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from ..mcp_client_manager import MCPClientManager

# 加载环境变量
load_dotenv("/mnt/e/project/langgraph_mcp_agent/.env")

# 定义 LangGraph 的 State
class State(TypedDict):
    messages: Annotated[list, add_messages]

class ChatSession:
    def __init__(self, model_name: str = "deepseek-chat"):
        self.llm = BaseChatOpenAI(
            model=model_name,
            openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
            openai_api_base="https://api.deepseek.com/v1",
            max_tokens=1024,
            temperature=0,
        )
        self.server_config_path = os.getenv("SERVER_CONFIG_PATH")
        self.client = MCPClientManager(self.server_config_path)
        self.memory = MemorySaver()
        self.tools = []
        self.graph = None
        self.llm_with_tools = None
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._initialize_graph())

    async def _initialize_graph(self):

        self.tools = await self.client.get_tools()
        #prompt = await self.client.get_prompt("PromptServer","ask_about_topic", {"topic": "LangGraph MCP Agent"})
        self.llm_with_tools = self.llm.bind_tools(self.tools)

        builder = StateGraph(State)

        async def chatbot(state: State):
            return {"messages": [await self.llm_with_tools.ainvoke(state["messages"]) ]}

        builder.add_node("chatbot", chatbot)
        builder.add_node("tools", ToolNode(tools=self.tools))
        builder.add_conditional_edges("chatbot", tools_condition)
        builder.add_edge("tools", "chatbot")
        builder.set_entry_point("chatbot")

        self.graph = builder.compile(checkpointer=self.memory)
        print(self.graph.get_graph().draw_mermaid())

    def get_server_info(self):
        return self.client.get_raw_config()
    

    async def stream_with_trace(self, user_input: str, resource_uris: list[str] = None):
        config = {"configurable": {"thread_id": "1"}}
        final_response = ""
           
        # 加载 MCP 资源内容
        context_texts = []
#        if resource_uris:
        print(f"加载资源文件")
        blobs = await self.client.get_resources("DataServer")
        print(f"加载到 {len(blobs)} 个资源文件")        
        context_texts = [b.as_string() for b in blobs]

        # 构造 prompt messages
        messages = []
        if context_texts:
            context_block = "\n\n".join(context_texts)
            messages.append({
                "role": "system",
                "content": f"以下是相关背景资料，请结合回答用户问题：\n{context_block}"
            })
        messages.append({"role": "user", "content": user_input})

        # 执行对话流
        async for event in self.graph.astream({"messages": messages}, config):
            for node_name, node_output in event.items():
                for msg in node_output.get("messages", []):
                    if msg.type == "ai":
                        content = msg.content or "[空回复]"
                        tool_calls = msg.tool_calls or []

                        if tool_calls:
                            yield "llm_thinking", "正在思考下一步动作..."
                            for call in tool_calls:
                                yield "tool_call", f"{call['name']}({call.get('args', {})})"
                        else:
                            yield "llm_response", content
                            final_response = content
                    elif msg.type == "tool":
                        yield "tool_result", msg.content

        yield "final_response", final_response
