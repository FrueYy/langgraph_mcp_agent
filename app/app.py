import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import asyncio
from core.chat.chat_session import ChatSession

st.set_page_config(page_title="LangGraph MCP Agent", layout="wide")

# 状态初始化
if "session" not in st.session_state:
    st.session_state.session = ChatSession()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "workflow_steps" not in st.session_state:
    st.session_state.workflow_steps = []  # 用来存储工具调用工作流简化信息

st.title("🧠 LangGraph MCP Agent")

# MCP 服务信息展示
with st.expander("🛠️ 当前 MCP 服务配置", expanded=False):
    st.json(st.session_state.session.get_server_info())

# 侧边栏操作
with st.sidebar:
    if st.button("🧹 清空聊天", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.workflow_steps = []
        st.session_state.session = ChatSession()  # 重建会话
        st.experimental_rerun()

    if st.button("🔄 刷新工具", use_container_width=True):
        st.session_state.session = ChatSession()  # 重建会话即刷新工具
        st.session_state.workflow_steps = []
        st.experimental_rerun()

# 展示历史对话
for i, (user_msg, bot_msg) in enumerate(st.session_state.chat_history):
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)
    # 展示对应的工作流（简化版）
    if i < len(st.session_state.workflow_steps):
        steps = st.session_state.workflow_steps[i]
        with st.expander("🔍 函数调用轨迹", expanded=False):
            for step in steps:
                st.markdown(f"- {step}")

# 处理用户输入
user_input = st.chat_input("请输入你的问题...")

if user_input:
    st.chat_message("user").markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("正在思考中..."):

            # 调用你的异步 run 接口，这里没有细化流式，直接调用run
            response, trace = asyncio.run(st.session_state.session.run(user_input))

            # 显示回复
            st.markdown(response)

            # 记录工作流（trace是list[str]，直接存储）
            st.session_state.workflow_steps.append(trace)

            # 更新历史对话
            st.session_state.chat_history.append((user_input, response))

