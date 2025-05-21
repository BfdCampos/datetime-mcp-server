from mcp.server.fastmcp import FastMCP
import os
import datetime

mcp = FastMCP("Datetime")

@mcp.tool("now")
def now() -> dict:
    """
    Returns the current date and time in local and UTC formats.
    """
    return {
        "local_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "utc_time": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
    }

