from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("Demo MCP Server")

@mcp.tool()
def hello(name: str):
    return f"Hello {name}"

app = mcp.asgi()

if __name__ == "__main__":
    mcp.run()