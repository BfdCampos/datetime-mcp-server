from mcp.server.fastmcp import FastMCP
import os
import datetime

mcp = FastMCP("Datetime")

@mcp.tool("now")
def now() -> str:
    """
    Returns the current date and time.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
