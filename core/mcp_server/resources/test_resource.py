import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="DataServer")

# Basic dynamic resource returning a string 
@mcp.resource("resource://greeting")
def get_greeting() -> str:
    """Provides a simple greeting message."""
    return "Hello from FastMCP Resources!"

# Resource returning JSON data (dict is auto-serialized)
@mcp.resource("data://config")
def get_config() -> dict:
    """Provides application configuration as JSON."""
    return {
        "theme": "dark",
        "version": "1.2.0",
        "features": ["tools", "resources"],
    }

if __name__ == "__main__":
    # 启动 MCP 服务器，使用 stdio 通信
    print("✅ Data Server 启动，提供动态资源和数据")
    mcp.run(transport="stdio")