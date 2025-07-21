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

    mcp.run(transport="stdio")