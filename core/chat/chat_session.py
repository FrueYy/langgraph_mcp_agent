import os
import asyncio
from typing import Annotated, TypedDict, Optional, List, Dict
from dotenv import load_dotenv
from langchain_openai.chat_models.base import BaseChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from ..mcp_client_manager import MCPClientManager
from collections import defaultdict

import traceback
# 加载环境变量
load_dotenv("/mnt/e/project/langgraph_mcp_agent/.env")

# 定义 LangGraph 的 State
class State(TypedDict):
    messages: Annotated[list, add_messages]
# 对话会话部分
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
    # 初始化图
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

    # 获取服务器信息
    def get_server_info(self):
        return self.client.get_raw_config()
    
    # 获取模型名称
    async def list_all_resources(self) -> List[str]:
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
    
    # 获取所有提示
    async def list_all_prompts(self) -> List[tuple[str, dict]]:
        all_prompts = []
        config = self.client.get_raw_config()
        for server in config:
            try:
                print(f"尝试连接 MCP 服务器 {server} 获取提示...")
                async with self.client.client.session(server) as session:
                    prompt_list = await session.list_prompts()
                    print(f"服务器 {server} 返回提示数: {len(prompt_list.prompts)}")
                    for p in prompt_list.prompts:
                        print(f"提示: {p.name}, 参数: {p.arguments}")
                        all_prompts.append((p.name, p.arguments or {}))
            except Exception as e:
                print(f"[跳过] {server} 出错：{e}")
        return all_prompts

    # 获取指定提示内容
    async def get_prompt_content(self, server_name: str, prompt_name: str, args: dict | None = None) -> str:
        try:
            result = await self.client.get_prompt(server_name, prompt_name, arguments=args or {})
            if result: # HumanMessage | AIMessage 列表
                msg = result[0]
                return getattr(msg.content, "text", str(msg.content))
        except Exception as e:
            import traceback; traceback.print_exc()
            print(f"[错误] 获取提示失败: {type(e).__name__}: {e}")
        return ""

    # 更新对话
    async def stream_with_trace(self, user_input: str, resource_uris: Optional[List[str]] = None, prompt_injection: Optional[str] = None, prompt_args: Optional[dict] = None):
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

            server_to_uris = defaultdict(list)
            for uri in resource_uris:
                server = uri_server_map.get(uri)
                if not server:
                    print(f"[警告] 未找到 uri 映射的 server：{uri}")
                else:
                    print(f"[映射] {uri} 属于 server {server}")
                    server_to_uris[server].append(uri)

            # 按 server 分组加载资源
            for server, uris in server_to_uris.items():
                try:
                    blobs = await self.client.get_resources(server, uris=uris)
                    for b in blobs:
                        content = b.as_string()
                        max_len = 3000
                        parts = [content[i:i+max_len] for i in range(0, len(content), max_len)]
                        context_texts.extend(parts)
                        print(f"[调试] 当前context_texts块数: {len(context_texts)}")
                        total_chars = sum(len(t) for t in context_texts)
                        print(f"[调试] 当前context_texts总字符数: {total_chars}")
                except Exception as e:
                    print(f"加载 {server} 的资源失败：{e}")

        # prompt messages
        messages = []

        # 注入快捷提示的内容到 system message
        if prompt_injection:
            args = prompt_args or {}
            response_text = await self.get_prompt_content(server_name="prompt-mcp", prompt_name=prompt_injection, args=args)
            user_input = response_text

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
