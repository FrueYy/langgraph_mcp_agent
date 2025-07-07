# Langgraph_mcp_agent
MCP-enabled intelligent agents based on the Langgraph framework.

# 项目名称

智能代理项目，集成MCPClient、MCPServer、基于LangGraph的ChatSession，支持Streamlit多轮对话和流程可视化。

## 功能

- 多种MCP传输协议支持（stdio, sse, websocket, streamable_http）
- 集成多工具、多资源和多提示的智能代理
- 基于LangGraph的对话流程管理
- Streamlit UI展示多轮对话和工具调用流程
- 支持工具自动调用与结果处理

## 目录结构
```bash
.
├── app/              
│   └── app.py             # 应用主程序(streamLIT)
├── core/
│   ├── chat/       # 
|   ├── mcp_server/
|   └── mcp_client.py
├── libs/
│   ├── llm_client.py             # 
│   └── utils.py              # 
├── tests/
│   ├── test_chat_session.py             # 
│   ├── test_mcp_client.py             # 
│   ├── test_mcp_server.py             # 
│   └── ...                             # 
├── pyproject.toml            # 
├── uv.lock                   # 
├── .gitignore
└── README.md 

## 环境要求

- Python 3.8+
- 依赖库见 requirements.txt

## 快速开始

```bash
git clone https://github.com/FrueYy/langgraph_mcp_agent.git
cd langgraph_mcp_agent
pip install uv
uv venv
source .venv/bin/activate
uv install
streamlit run app/app.py

