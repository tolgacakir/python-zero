from mcp import FastMCP
import datetime

mcp = FastMCP("Time MCP Server")

@mcp.tool()
def get_current_time() -> str:
    """Get the current time in ISO format"""
    return datetime.datetime.now().isoformat()