import os
import fitz  
from mcp.server.fastmcp import FastMCP
import urllib.parse
#本地天洑资源服务器
mcp = FastMCP(name="LocalResourceServer")
RESOURCE_DIR = "/mnt/e/project/langgraph_mcp_agent/core/mcp_server/resources/njtf_resources/"

@mcp.resource(uri = "file://AICFD_2025R1_case_manual.md")
def read_case_manual() -> str:
    """读取天洑 AICFD_2025R1 案例手册"""
    path = os.path.join(RESOURCE_DIR, "AICFD_2025R1_case_manual.md")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
@mcp.resource(uri = "file://AICFD_2025R1_install_guide.md")
def read_install_guide() -> str:
    """读取天洑 AICFD_2025R1 安装指南"""
    path = os.path.join(RESOURCE_DIR, "AICFD_2025R1_install_guide.md")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
@mcp.resource(uri = "file://AICFD_2025R1_user_manual.md")
def read_user_manual() -> str:
    """读取天洑 AICFD_2025R1 用户手册"""
    path = os.path.join(RESOURCE_DIR, "AICFD_2025R1_user_manual.md")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
@mcp.resource(uri = "file://AICFD_2025R1_new_features.md")
def read_new_features() -> str:
    """读取天洑 AICFD_2025R1 新版本特性介绍"""
    path = os.path.join(RESOURCE_DIR, "AICFD_2025R1_new_features.md")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()    


if __name__ == "__main__":
    mcp.run(transport="stdio")
