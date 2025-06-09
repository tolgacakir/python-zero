from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="EchoServer", stateless_http=True)


@mcp.tool(description="A simple reversed echo tool")
def reversed_echo(message: str) -> str:
    return f"Reversed Echo: {message[::-1]}"

@mcp.tool(description="An example tool that returns local time")
def local_time() -> str:
    from datetime import datetime
    return f"Local time is: {datetime.now().isoformat()}"

if __name__ == "__main__":
    mcp.run()