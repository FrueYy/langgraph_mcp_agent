import json
from pathlib import Path
from langchain_mcp_adapters.client import MultiServerMCPClient
from typing import Any

class MCPClientManager:
    def __init__(self, config_path: str | Path | None = None):
        self.config_path = config_path
        self.client = self._init_client()

    def _init_client(self) -> MultiServerMCPClient:

        if isinstance(self.config_path, str):
            self.config_path = Path(self.config_path)

        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file {self.config_path} does not exist.")

        with open(self.config_path, 'r') as file:
            config = json.load(file)

        return MultiServerMCPClient(config)
    async def get_tools(self, server_name: str = None):
        return await self.client.get_tools(server_name=server_name)

    async def get_prompt(self, server_name: str, prompt_name: str, arguments: dict[str, Any] = None):
        return await self.client.get_prompt(server_name, prompt_name, arguments=arguments)

    async def get_resources(self, server_name: str, uris: list[str] = None):
        return await self.client.get_resources(server_name, uris=uris)  
    
    def get_raw_config(self) -> dict:
        with open(self.config_path, "r") as f:
            return json.load(f)