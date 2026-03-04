from fastmcp import FastMCP
from supabase import create_client
import os
from typing import List, Dict

# ==========================================
# MCP Server
# ==========================================
mcp = FastMCP("AccidentDeathServer")

# ==========================================
# Load Environment Variables
# ==========================================
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# ==========================================
# TOOL 1: ถนนที่มีคนตาย
# ==========================================
@mcp.tool
def roads_with_death() -> List[Dict]:
    """
    Return all roads where death > 0
    Grouped and summed by street.
    """
    response = supabase.rpc("get_roads_with_death_mcp").execute()
    return response.data


# ==========================================
# TOOL 2: จังหวัดที่มีคนตาย
# ==========================================
@mcp.tool
def provinces_with_death() -> List[Dict]:
    """
    Return all provinces where death > 0
    Grouped and summed by province.
    """
    response = supabase.rpc("get_provinces_with_death_mcp").execute()
    return response.data


# ==========================================
# Optional: Health Check
# ==========================================
@mcp.tool
def health_check() -> str:
    return "MCP Server is running and connected to Supabase."


# ==========================================
# Run MCP
# ==========================================
if __name__ == "__main__":
    mcp.run()