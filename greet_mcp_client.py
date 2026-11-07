import asyncio
from fastmcp import Client

def get_client(url):
    return Client(url)

client = get_client("http://localhost:8000/mcp")
# client = Client("https://mcp-server-example.fastmcp.app/mcp")

async def list_tool(client: Client):
    async with client:
        tools = await client.list_tools()
        return tools
# List available tools
tools = asyncio.run(list_tool(client))
print("Available tools:", tools)

async def call_tool(name: str, client: Client):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        return result
# Call the greet tool
result = asyncio.run(call_tool("Ford",client))
print(result)