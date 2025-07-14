# langgraph_mcp_agent
基于Langgraph架构的支持MCP协议的智能代理

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
│   └── app.py                     # 应用主程序(streamLIT)
├── core/                          # 核心组件
│   ├── chat/                      # 聊天会话部分，基于Langgraph的聊天机器人
|   ├── mcp_server/                # mcp服务器，包含可调用的工具、资源等
|   └── mcp_client_manager.py      # mcp客户端管理，封装客户端读取服务器配置文件的部分              
├── libs/                          # 包含一些配置信息
│   ├── llm_client.py              
│   └── utils.py               
├── tests/                         
│   ├── test_chat_session.py              
│   ├── test_mcp_client.py              
│   ├── test_mcp_server.py              
│   └── ...                              
├── pyproject.toml             
├── uv.lock                    
├── .gitignore
└── README.md 
```
## 环境要求

- Python 3.8+
- 依赖库用uv直接下载

## 快速开始

```bash
git clone https://github.com/FrueYy/langgraph_mcp_agent.git
cd langgraph_mcp_agent
pip install uv
uv venv
source .venv/bin/activate
uv install
streamlit run app/app.py

