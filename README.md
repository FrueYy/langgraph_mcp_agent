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

## 环境要求

- Python 3.8+
- 依赖库见 requirements.txt

## 快速开始

```bash
git clone https://github.com/<用户名>/my_ai_agent_project.git
cd my_ai_agent_project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/main.py

