import streamlit as st
import sys
import os
import asyncio
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.chat.chat_session import ChatSession

st.set_page_config(page_title="LangGraph MCP Agent", layout="wide")

# 模型选择
st.sidebar.markdown("### 模型选择")
available_models = ["deepseek-chat", "deepseek-reasoner"]

# 初始化默认模型
if "selected_model" not in st.session_state:
    st.session_state.selected_model = "deepseek-chat"

# 选择模型
selected_model = st.sidebar.selectbox("请选择模型", available_models, index=available_models.index(st.session_state.selected_model))

# 切换模型
if selected_model != st.session_state.selected_model:
    st.session_state.selected_model = selected_model
    st.session_state.session = ChatSession(model_name=selected_model)
    st.experimental_rerun()

# 状态初始化
if "thought_history" not in st.session_state:
    st.session_state.thought_history = []

if "session" not in st.session_state:
    st.session_state.session = ChatSession(model_name=st.session_state.selected_model)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "workflow_steps" not in st.session_state:
    st.session_state.workflow_steps = []  # 用来存储工具调用工作流简化信息

# MCP Prompt缓存
if "all_prompts" not in st.session_state:
    prompts = asyncio.run(st.session_state.session.list_all_prompts())
    # prompts 是 List[(name, args_schema)]
    st.session_state.all_prompts = prompts

st.title("🧠LangGraph MCP Agent")

# 加载资源列表
if "resource_uris" not in st.session_state:
    st.session_state.resource_uris = []

if "all_resource_uris" not in st.session_state:
    uris = asyncio.run(st.session_state.session.list_all_resources())
    print(f"加载到 {len(uris)} 个资源")
    st.session_state.all_resource_uris = uris

with st.sidebar:
    st.markdown("### 📂选择注入资源")
    selected_uris = st.multiselect(
        "选择需要注入上下文的资源：",
        st.session_state.all_resource_uris,
        default=st.session_state.resource_uris,
    )
    st.session_state.resource_uris = selected_uris

# 提示模版名称与参数名列表的映射
prompt_args_map = {}
for name, args in st.session_state.all_prompts:
    prompt_args_map[name] = [arg.name for arg in args] if args else []

# 侧边栏：资源选择、快捷提示操作
with st.sidebar:
    st.markdown("### 💡 快捷提示操作")

    # 选择提示模板
    selected_prompt = st.selectbox("选择一个提示模板", ["（不使用提示）"] + list(prompt_args_map.keys()), key="selected_prompt")

    # 根据选择设置参数名列表
    if selected_prompt == "（不使用提示）":
        st.session_state.selected_prompt_args = []
    else:
        st.session_state.selected_prompt_args = prompt_args_map.get(selected_prompt, [])

    st.markdown("---")

    # 侧边栏操作：清空聊天、刷新工具
    if st.button("清空聊天", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.workflow_steps = []
        st.session_state.thought_history = []
        st.session_state.session = ChatSession(model_name=st.session_state.selected_model)  # 重建会话
        st.experimental_rerun()

    if st.button("刷新工具", use_container_width=True):
        st.session_state.session = ChatSession(model_name=st.session_state.selected_model)  # 重建会话即刷新工具
        st.session_state.workflow_steps = []
        st.experimental_rerun()

    # MCP服务信息展示
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

        st.markdown("---")
        st.markdown("###  添加新工具")

        new_tool_json = st.text_area(
            "请输入新工具 JSON（键名+对象）",
            height=160,
            placeholder='"demo-tool": {"command": "python", "args": ["demo.py"], "transport": "stdio"}'
        )

        if st.button(" 添加工具并保存"):
            try:
                # 解析用户输入
                parsed = json.loads("{" + new_tool_json.strip().rstrip(",") + "}")

                # 读取原始配置
                current_config = st.session_state.session.get_server_info()
                current_config.update(parsed)

                # 写回配置文件
                with open(st.session_state.session.server_config_path, "w", encoding="utf-8") as f:
                    json.dump(current_config, f, indent=4, ensure_ascii=False)

                st.success(" 工具添加成功并已写入配置文件！")
                st.experimental_rerun()

            except Exception as e:
                st.error(f" 添加失败，请检查 JSON 格式：{e}")

# 历史对话 
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

# 用户输入处理 
if st.session_state.selected_prompt and st.session_state.selected_prompt_args:
    arg_count = len(st.session_state.selected_prompt_args)
    if arg_count == 1:
        placeholder_text = f"请输入参数（{st.session_state.selected_prompt_args[0]}），系统将根据参数内容补充提示并作答"
    else:
        arg_names_str = " || ".join(st.session_state.selected_prompt_args)
        placeholder_text = f"请按顺序输入参数（{arg_names_str}），各参数之间用 '||' 分隔，系统将根据参数内容补充提示并作答"
else:
    placeholder_text = "请输入你的问题..."

user_input = st.chat_input(placeholder_text)

if user_input:
    st.chat_message("user").markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("正在思考中..."):
            response_box = {"response": ""}
            thought_buffer = []

            with st.expander("💡 思考过程", expanded=True):
                thought_container = st.empty()

                async def handle():
                    prompt_name = st.session_state.get("selected_prompt")
                    arg_names = st.session_state.get("selected_prompt_args", [])

                    # 解析参数
                    if prompt_name and arg_names:
                        parts = [part.strip() for part in user_input.split("||")]
                        args_dict = dict(zip(arg_names, parts))
                    else:
                        args_dict = {}

                    async for etype, content in st.session_state.session.stream_with_trace(
                        user_input,
                        resource_uris=st.session_state.resource_uris,
                        prompt_injection=prompt_name,
                        prompt_args=args_dict
                    ):
                        if etype in {"llm_thinking", "tool_call", "tool_result"}:
                            icon_map = {
                                "llm_thinking": "💭",
                                "tool_call": "[工具调用]",
                                "tool_result": "[工具返回]",
                            }
                            icon = icon_map.get(etype, "-")
                            line = f"{icon} {content}"
                            thought_buffer.append(line)
                            thought_container.markdown(
                                "\n".join(f"- {line}" for line in thought_buffer),
                                unsafe_allow_html=True
                            )
                        elif etype == "final_response":
                            response_box["response"] = content

                asyncio.run(handle())

            st.markdown(response_box["response"])

            # 保存聊天历史
            st.session_state.chat_history.append((user_input, response_box["response"]))
            st.session_state.thought_history.append(thought_buffer)
            st.session_state.workflow_steps.append([])
