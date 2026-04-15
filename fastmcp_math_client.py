import asyncio
from fastmcp import Client

async def main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        # List available tools
        tools = await client.list_tools()
        print("Available tools:", tools)
        # Call the add tool
        result = await client.call_tool(name="add", arguments={"a": 2, "b": 3})
        print("add(2, 3) =", result)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
