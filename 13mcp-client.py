from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Executable
    args=["12mcp-server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)


# Optional: create a sampling callback
async def handle_sampling_message(
    message: types.CreateMessageRequestParams,
) -> types.CreateMessageResult:
    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text="Hello, world! from model",
        ),
        model="gpt-3.5-turbo",
        stopReason="endTurn",
    )


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write, sampling_callback=handle_sampling_message
        ) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            list_result = await session.list_tools()
            for tool in list_result.tools:
                print(f"Tool: {tool.name} - {tool.description}")

            # Call a tool
            result = await session.call_tool("reversed_echo", {"message": "Hello, MCP!"})
            print("Tool call result:", result.content[0].text)

            # Call a tool
            result = await session.call_tool("local_time")
            print("Tool call result:", result.content[0].text)

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
