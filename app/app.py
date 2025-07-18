import streamlit as st
import sys
import os
import asyncio
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.chat.chat_session import ChatSession

st.set_page_config(page_title="LangGraph MCP Agent", layout="wide")

# === 模型选择 ===
st.sidebar.markdown("### 模型选择")
available_models = ["deepseek-chat", "deepseek-reasoner"]

# 初始化默认模型
if "selected_model" not in st.session_state:
    st.session_state.selected_model = "deepseek-chat"

# 显示模型选择器
selected_model = st.sidebar.selectbox("请选择模型", available_models, index=available_models.index(st.session_state.selected_model))

# 切换模型后重建 ChatSession
if selected_model != st.session_state.selected_model:
    st.session_state.selected_model = selected_model
    st.session_state.session = ChatSession(model_name=selected_model)
    st.rerun()

# 状态初始化
if "thought_history" not in st.session_state:
    st.session_state.thought_history = []

if "session" not in st.session_state:
    st.session_state.session = ChatSession(model_name=st.session_state.selected_model)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "workflow_steps" not in st.session_state:
    st.session_state.workflow_steps = []  # 用来存储工具调用工作流简化信息

st.title("🧠LangGraph MCP Agent")



# 侧边栏操作
with st.sidebar:
    if st.button("清空聊天", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.workflow_steps = []
        st.session_state.thought_history = []
        st.session_state.session = ChatSession(model_name=st.session_state.selected_model)  # 重建会话
        st.rerun()

    if st.button("刷新工具", use_container_width=True):
        st.session_state.session = ChatSession(model_name=st.session_state.selected_model)  # 重建会话即刷新工具
        st.session_state.workflow_steps = []
        st.rerun()

    # MCP 服务信息展示
    with st.expander("当前 MCP 服务配置", expanded=True):
        server_info = st.session_state.session.get_server_info()

        card_style = """
            <style>
            .tool-card {
                background-color: #f9f9f9;
                border-radius: 12px;
                padding: 12px 16px;
                margin-bottom: 10px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            }
            .tool-name {
                font-weight: 600;
                font-size: 16px;
                color: #262730;
                margin-bottom: 6px;
            }
            .tool-transport {
                font-size: 14px;
                color: #6c757d;
            }
            .tool-transport span {
                font-weight: 500;
                background-color: #e8f0fe;
                color: #1967d2;
                padding: 2px 6px;
                border-radius: 6px;
            }
            </style>
        """
        st.markdown(card_style, unsafe_allow_html=True)

        for tool_name, config in server_info.items():
            transport = config.get("transport", "unknown")
            card_html = f"""
            <div class="tool-card">
                <div class="tool-name">{tool_name}</div>
                <div class="tool-transport"> Transport: <span>{transport}</span></div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)

                # 添加工具
        st.markdown("---")
        st.markdown("###  添加新工具")

        new_tool_json = st.text_area(
            "请输入新工具 JSON（键名+对象）",
            height=160,
            placeholder='"demo-tool": {"command": "python", "args": ["demo.py"], "transport": "stdio"}'
        )

        if st.button(" 添加工具并保存"):
            try:
                # 1. 解析用户输入
                parsed = json.loads("{" + new_tool_json.strip().rstrip(",") + "}")
                
                # 2. 读取原始配置
                current_config = st.session_state.session.get_server_info()
                current_config.update(parsed)

                # 3. 写回配置文件
                with open(st.session_state.session.server_config_path, "w", encoding="utf-8") as f:
                    json.dump(current_config, f, indent=4, ensure_ascii=False)

                st.success(" 工具添加成功并已写入配置文件！")
                st.rerun()

            except Exception as e:
                st.error(f" 添加失败，请检查 JSON 格式：{e}")



# 显示历史对话
for i, (user_msg, bot_msg) in enumerate(st.session_state.chat_history):
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        # 显示思考过程
        if i < len(st.session_state.thought_history):
            with st.expander("💡 思考过程", expanded=False):
                for line in st.session_state.thought_history[i]:
                    st.markdown(f"- {line}")
        st.markdown(bot_msg)

# 处理用户输入
user_input = st.chat_input("请输入你的问题...")

if user_input:
    st.chat_message("user").markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("正在思考中..."):
            response_box = {"response": ""}
            trace_lines = []
            thought_buffer = []

            with st.expander("💡 思考过程", expanded=True):
                thought_container = st.empty()  # 在expander内流式更新

                async def handle():
                    async for etype, content in st.session_state.session.stream_with_trace(user_input):
                        if etype in {"llm_thinking", "tool_call", "tool_result"}:
                            icon_map = {
                                "llm_thinking": "💭",
                                "tool_call": "[工具调用]",
                                "tool_result": "[工具返回]",
                            }
                            icon = icon_map.get(etype, "-")
                            line = f"{icon} {content}"
                            thought_buffer.append(line)

                            # 实时刷新内容
                            thought_container.markdown(
                                "\n".join(f"- {line}" for line in thought_buffer),
                                unsafe_allow_html=True
                            )
                        elif etype == "final_response":
                            response_box["response"] = content
                        elif etype == "trace_tree":
                            trace_lines.extend(content)

                asyncio.run(handle())

            # 输出最终回复
            st.markdown(response_box["response"])

            # 保存到历史状态
            st.session_state.chat_history.append((user_input, response_box["response"]))
            st.session_state.thought_history.append(thought_buffer)
            st.session_state.workflow_steps.append(trace_lines)



