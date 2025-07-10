import streamlit as st
import sys
import os
import asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.chat.chat_session import ChatSession

st.set_page_config(page_title="LangGraph MCP Agent", layout="wide")

# 状态初始化
if "thought_history" not in st.session_state:
    st.session_state.thought_history = []

if "session" not in st.session_state:
    st.session_state.session = ChatSession()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "workflow_steps" not in st.session_state:
    st.session_state.workflow_steps = []  # 用来存储工具调用工作流简化信息

st.title("🧠 LangGraph MCP Agent")

# 侧边栏操作
with st.sidebar:
    if st.button("🧹 清空聊天", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.workflow_steps = []
        st.session_state.thought_history = []
        st.session_state.session = ChatSession()  # 重建会话
        st.experimental_rerun()

    if st.button("🔄 刷新工具", use_container_width=True):
        st.session_state.session = ChatSession()  # 重建会话即刷新工具
        st.session_state.workflow_steps = []
        st.experimental_rerun()

    # MCP 服务信息展示
    with st.expander("🛠️ 当前 MCP 服务配置", expanded=False):
        st.json(st.session_state.session.get_server_info())

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



