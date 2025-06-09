from langchain.llms import Ollama
from langchain.agents import Tool, initialize_agent, AgentType
import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def call_mcp_tool(tool_name, tool_args=None):
    server_params = StdioServerParameters(
        command="python",
        args=["12mcp-server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, tool_args or {})
            return result.content[0].text

def reversed_echo_tool(input_text: str) -> str:
    return asyncio.run(call_mcp_tool("reversed_echo", {"message": input_text}))

def local_time_tool(_: str = "") -> str:
    return asyncio.run(call_mcp_tool("local_time"))

# LangChain tool tanımları
tools = [
    Tool(
        name="ReversedEchoTool",
        func=reversed_echo_tool,
        description="Echoes the given message in reverse"
    ),
    Tool(
        name="LocalTimeTool",
        func=local_time_tool,
        description="Returns the local time"
    )
]

# Ollama ile LLM oluştur
llm = Ollama(model="qwen2.5:14b")

# Ajanı başlat
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Örnek sorgular
if __name__ == "__main__":
    while True:
        prompt = input("Enter your prompt: ")
        if prompt.lower() in ["exit", "quit","q"]:
            break
        print(agent.run(prompt))
