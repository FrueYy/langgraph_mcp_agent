# 🧠langgraph_mcp_agent

基于Langgraph架构的支持MCP协议的智能代理

## 项目名称

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
│   └── app.py                     # 应用主程序(streamlit)
├── core/                          # 核心组件
│   ├── chat/                      # 聊天会话部分，基于Langgraph的聊天机器人
│   ├── mcp_server/                # mcp服务器，包含可调用的工具、资源等
│   └── mcp_client_manager.py      # mcp客户端管理，封装客户端读取服务器配置文件的部分                                          
├── pyproject.toml             
├── uv.lock                    
├── .gitignore
├── .env.example                   # 环境变量示例文件
└── README.md 
```

## 环境要求

- Python 3.8及以上版本  
- uv 管理工具（用于依赖安装和虚拟环境管理）  
- 建议使用虚拟环境避免依赖冲突  

## 快速开始

### 1. 克隆代码仓库

在命令行（Terminal）输入以下命令，将项目代码克隆到本地：

```bash
git clone https://github.com/FrueYy/langgraph_mcp_agent.git
cd langgraph_mcp_agent
```

### 2. 配置环境变量

项目依赖一些密钥和配置，需复制示例文件并填写个人信息：

```bash
cp .env.example .env
```
### 3. 安装 Python 依赖及创建虚拟环境

建议使用虚拟环境隔离项目依赖，安装 [uv](https://pypi.org/project/uv/) 管理工具后执行：

```bash
pip install uv               # 安装 uv 工具
uv venv                      # 创建虚拟环境
source .venv/bin/activate    # 激活虚拟环境
uv install                   # 安装项目依赖
```
### 4. 启动 Streamlit 应用

依赖安装完成后，启动项目主程序：

```bash
streamlit run app/app.py
```

## 其他说明

- 请在项目根目录复制 `.env.example` 文件为 `.env`，并填写自己的API密钥等配置信息。  
- 依赖由 uv 根据 pyproject.toml 管理，请确保网络畅通。  
- 项目支持多种MCP传输协议，详细配置请查看 `core/mcp_server` 和 `core/mcp_client_manager.py`。  
- 遇到环境问题请确认Python版本及虚拟环境是否激活。  
- 欢迎根据需求扩展工具、资源和提示模板。  

---

感谢使用 langgraph_mcp_agent，期待你的反馈与贡献！