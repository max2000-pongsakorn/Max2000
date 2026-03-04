from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("Demo MCP Server")

@mcp.tool()
def hello(name: str):
    return f"Hello {name}"

app = mcp.asgi()