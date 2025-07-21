import os
import fitz  # PyMuPDF 用于读取 PDF 文件
from mcp.server.fastmcp import FastMCP

# 你的资源文件夹路径（相对路径或绝对路径均可）

mcp = FastMCP(name="LocalResourceServer")
RESOURCE_DIR = "/mnt/e/project/langgraph_mcp_agent/core/mcp_server/resources/njtf_resources/"
for filename in os.listdir(RESOURCE_DIR):
    full_path = os.path.join(RESOURCE_DIR, filename)
    if not os.path.isfile(full_path):
        continue

    uri = f"file://{filename}"

    @mcp.resource(uri)
    def read_source() -> str:
        path = os.path.join(RESOURCE_DIR, filename)
        if filename.endswith(".md"):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        elif filename.endswith(".pdf"):
            doc = fitz.open(path)
            return "\n".join(page.get_text() for page in doc)
        else:
            return f"[不支持的文件类型: {filename}]"




if __name__ == "__main__":
    # 启动 MCP 服务器，使用 stdio 通信
    mcp.run(transport="stdio")
