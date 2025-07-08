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
