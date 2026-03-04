from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("Demo MCP Server")

@mcp.tool()
def get_current_time():
    """Get current server time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@mcp.tool()
def calculate_vat(price: float, vat_rate: float = 7):
    """Calculate VAT from price"""
    vat = price * vat_rate / 100
    total = price + vat
    return {
        "price": price,
        "vat": vat,
        "total": total
    }

@mcp.tool()
def echo(message: str):
    """Echo message"""
    return f"You said: {message}"

@mcp.tool()
def hello(name: str):
    return f"Hello {name}"

# ✅ ใช้แบบนี้ใน v3
app = mcp.app

if __name__ == "__main__":
    mcp.run()