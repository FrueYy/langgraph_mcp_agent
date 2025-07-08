
from typing import Annotated

from langchain_openai.chat_models.base import BaseChatOpenAI
from langchain_tavily import TavilySearch  
from langchain_core.messages import BaseMessage
from typing_extensions import TypedDict
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_community.agent_toolkits.financial_datasets.toolkit import (
    FinancialDatasetsToolkit,
)
from langchain_community.utilities.financial_datasets import FinancialDatasetsAPIWrapper
from langgraph_mcp_agent.core.mcp_client_manager import MCPClientManager

# 加载.env文件中的环境变量
load_dotenv('/mnt/e/project/chatbot_v1/.env')

# 定义状态类型，使用 add_messages 注解来自动合并消息列表
class State(TypedDict):
    messages: Annotated[list, add_messages]  # 消息列表将使用 add_messages reducer 自动合并           


# 初始化 DeepSeek 聊天模型
llm=BaseChatOpenAI(model='deepseek-chat',
    openai_api_key=os.getenv('DEEPSEEK_API_KEY'),   
    openai_api_base='https://api.deepseek.com/v1',
    max_tokens=1024,
    temperature=0)


# 创建状态图构建器
graph_builder = StateGraph(State)

# 初始化工具
client = MCPClientManager(config_path='/mnt/e/project/langgraph/mcp_server/server_config.json')  # MCP客户端管理器
tools = client.get_tools()  # 获取MCP客户端管理器中的工具
# 将工具绑定到LLM
llm_with_tools = llm.bind_tools(tools)

# 定义聊天机器人节点函数
def chatbot(state: State):
    """LLM节点函数，处理用户输入并生成响应"""
    return {"messages": [llm_with_tools.invoke(state["messages"])]}
# 添加聊天机器人节点
graph_builder.add_node("chatbot", chatbot)

# 添加工具节点
tool_node = ToolNode(tools=tools)  # 添加自定义的乘法工具和金融数据工具 [search_tool, multiply] + 
graph_builder.add_node("tools", tool_node)

# 添加条件边
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
# 工具调用完成后，返回到聊天机器人节点
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")


memory = MemorySaver()  # 在内存中保存状态

# 使用内存保存器编译图
graph = graph_builder.compile(checkpointer=memory)  # 将内存保存器传递给图

# 打印图结构
print(graph.get_graph().draw_mermaid())

def stream_graph_updates(user_input: str):
    config = {"configurable": {"thread_id": "1"}} 
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}, config):
        for key, value in event.items(): 
#            if value["messages"][-1].content=="":
#                continue
#            if key == "tools":
#                continue
            print(f"[{key}]", value["messages"][-1].content)  # 打印每个事件的消息内容

while True:
    try:
        user_input = input("User: ")    
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break

