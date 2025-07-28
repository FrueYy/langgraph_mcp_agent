from mcp.server.fastmcp import FastMCP
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from core.mcp_client_manager import MCPClientManager
from dotenv import load_dotenv
from collections import defaultdict

# 加载环境变量
load_dotenv("/mnt/e/project/langgraph_mcp_agent/.env")

# 初始化 MCP 服务
client = MCPClientManager(os.getenv("SERVER_CONFIG_PATH"))

mcp = FastMCP(name="SearchMCPResource")

@mcp.tool()
async def list_mcp_resources() -> dict:
    """ 
    列出所有已注册在mcp服务器的可用的资源 URI,在查询资源时优先调用此工具查询mcp服务器上的资源列表。
    当询问的是安装方法、使用手册、版本特征、API 文档等内容时，优先使用此工具查询。
    如无结果，再使用搜索引擎网上搜索。

    Args:
        None

    Returns:
        dict[str, list[str]]:
            - key: 服务器名称
            - value: 该服务器上所有资源的 URI 列表
    """
    all_uris = []
    uri_server_map = {}
    server_config = client.get_raw_config() 

    for server in server_config:
        print(f"正在加载 {server} 的资源...")
        try:
            async with client.client.session(server) as session:
                resource_list = await session.list_resources()
                for r in resource_list.resources:
                    uri_server_map[r.uri] = server #uri -> server 映射
                uris = [r.uri for r in resource_list.resources]
                all_uris.extend(uris)
        except Exception as e:
            print(f"[跳过] {server} 出错：{e}")
            continue

    server_to_uris = defaultdict(list)
    for uri in all_uris:
        server = uri_server_map.get(uri)
        if server:
            server_to_uris[server].append(uri)
        else:
            continue

    return server_to_uris

@mcp.tool()
async def read_mcp_resources(server: str, uris: list[str]) -> list[str]:
    """
    根据用户所要查询的资源，读取指定服务器上的资源内容。无需读取所有资源，只需读取用户指定的资源。
    Args:
        server: 服务器名称
        uris: 要读取的资源 URI 列表
    """
    context_texts = []
    try:
        blobs = await client.get_resources(server, uris=uris)
        for b in blobs:
            content = b.as_string()
            max_len = 3000
            parts = [content[i:i+max_len] for i in range(0, len(content), max_len)]
            context_texts.extend(parts)

    except Exception as e:
        print(f"加载 {server} 的资源失败：{e}")

    return context_texts


if __name__ == "__main__":
    # 启动 MCP 服务
    mcp.run(transport="stdio")