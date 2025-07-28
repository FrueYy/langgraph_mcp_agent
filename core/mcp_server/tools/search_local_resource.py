# filename: multi_format_auto_read_server.py

import os, difflib
from pathlib import Path
import fitz  # PyMuPDF
from mcp.server.fastmcp import FastMCP, Context

# 初始化 MCP 服务
mcp = FastMCP(name="AutoReadMultiFormatServer")

# 资源目录
RESOURCE_DIR = "/mnt/e/project/langgraph_mcp_agent/core/mcp_server/resources/njtf_resources/"
# 索引列表，存储资源元数据
res_index = []
for path in Path(RESOURCE_DIR).iterdir():
    if not path.is_file(): continue
    suffix = path.suffix.lower()
    if suffix in {".md", ".pdf", ".txt"}:
        res_index.append({"filename": path.name, "path": path, "suffix": suffix})

@mcp.tool()
def list_local_resources() -> list[str]:
    """
    请求本地资源读取时，先列出所有可用资源文件（支持 .md、.pdf、.txt)。
    """
    return [r["filename"] for r in res_index]

@mcp.tool()
def read_local_resource(filename: str) -> str:
    """
    读取指定资源文件内容：
      - .md/.txt:以 UTF-8 文本方式读取
      - .pdf:使用 PyMuPDF 提取所有页面文本
    Args:
        filename: 要读取的文件名

    Returns:
        文件内容或错误信息
    """
    rec = next((r for r in res_index if r["filename"] == filename), None)
    if not rec:
        return f"错误：未找到文件 `{filename}`。"

    try:
        if rec["suffix"] in {".md", ".txt"}:
            return rec["path"].read_text(encoding="utf-8")
        elif rec["suffix"] == ".pdf":
            doc = fitz.open(rec["path"])
            return "\n".join(page.get_text() for page in doc)
        else:
            return f"不支持的文件类型：{rec['suffix']}"
    except Exception as e:
        return f"读取 `{filename}` 时出错：{e}"
    
@mcp.tool()
def write_markdown_file(filename: str, content: str) -> str:
    """在给定的文件夹内写入并保存一个markdown 文件，且不能写入重复文件。

    Args:
        filename: 要创建的文件名
        content: 要写入文件的内容.

    Returns:
        对于操作结果的描述
    """
    # 确定文件名以 .md 结尾
    if not filename.endswith(".md"):
        filename += ".md"

    # 构建完整的文件路径
    file_path = Path(RESOURCE_DIR) / filename

    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 检查是否已存在同名文件
    if file_path.exists():
        return (
            f"Error: 文件 {file_path} 已存在，"
            "请更换文件名或删除现有文件。\n"
        )

    # 写入文件内容
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Success: Markdown 文件保存至 {file_path}"
    except Exception as e:
        return f"写入文件错误: {str(e)}"
    

if __name__ == "__main__":
    mcp.run(transport="stdio")
