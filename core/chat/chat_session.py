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
from collections import defaultdict
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
    
    async def list_all_resources(self) -> list[str]:
        all_uris = []
        config = self.client.get_raw_config() 

        for server in config:
            print(f"正在加载 {server} 的资源...")
            try:
                async with self.client.client.session(server) as session:
                    resource_list = await session.list_resources()
                    uris = [r.uri for r in resource_list.resources]
                    print(f"[{server}] 发现 {len(uris)} 个资源")
                    all_uris.extend(uris)
            except Exception as e:
                print(f"[跳过] {server} 出错：{e}")
                continue

        return all_uris

    async def list_all_prompts(self) -> list[str]:
        all_prompts = []
        config = self.client.get_raw_config()
        for server in config:
            print(f"正在加载 {server} 的提示...")
            try:
                async with self.client.client.session(server) as session:
                    prompt_list = await session.list_prompts()
                    prompts = [p.name for p in prompt_list.prompts]
                    print(f"[{server}] 发现 {len(prompts)} 个提示")
                    all_prompts.extend(prompts)
            except Exception as e:
                print(f"[跳过] {server} 出错：{e}")
                continue

        return all_prompts
        
    async def stream_with_trace(self, user_input: str, resource_uris: list[str] = None):
        print(f"收到资源注入请求，uris: {resource_uris}")
        config = {"configurable": {"thread_id": "1"}}
        final_response = ""
        
        # 加载 MCP 资源内容
        context_texts = []
        if resource_uris:
            # 创建 uri -> server 映射
            uri_server_map = {}
            server_config = self.client.get_raw_config()
            for server in server_config:
                try:
                    async with self.client.client.session(server) as session:
                        resource_list = await session.list_resources()
                        for r in resource_list.resources:
                            uri_server_map[r.uri] = server
                except:
                    continue

            # get_resources

            server_to_uris = defaultdict(list)
            for uri in resource_uris:
                server = uri_server_map.get(uri)
                if not server:
                    print(f"[警告] 未找到 uri 映射的 server：{uri}")
                else:
                    print(f"[映射] {uri} 属于 server {server}")
                    server_to_uris[server].append(uri)

            for server, uris in server_to_uris.items():
                try:
                    blobs = await self.client.get_resources(server, uris=uris)
                    for b in blobs:
                        content = b.as_string()
                        max_len = 3000
                        parts = [content[i:i+max_len] for i in range(0, len(content), max_len)]
                        context_texts.extend(parts)
                        # 打印当前context_texts长度（块数）
                        print(f"[调试] 当前context_texts块数: {len(context_texts)}")

                        # 打印所有文本块的总字符数
                        total_chars = sum(len(t) for t in context_texts)
                        print(f"[调试] 当前context_texts总字符数: {total_chars}")
                except Exception as e:
                    print(f"加载 {server} 的资源失败：{e}")


        # prompt messages
        messages = []
        if context_texts:
            context_block = "\n\n".join(context_texts)
            messages.append({
                "role": "system",
                "content": f"以下是相关背景资料，请结合回答用户问题：\n{context_block}"
            })
        messages.append({"role": "user", "content": user_input})

        # 更新对话
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
