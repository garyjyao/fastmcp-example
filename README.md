# FastMCP Example Repository

This repository demonstrates a simple MCP (Model Control Protocol) implementation using the `fastmcp` library. It includes example clients and servers for mathematical operations and greeting services.

## Files

- `fastmcp_math_server.py` – MCP server providing an `add` tool.  
- `fastmcp_math_client.py` – Client that connects to the math server, lists tools, and calls `add`.  
- `greet_mcp_server.py` – MCP server that greets users.  
- `greet_mcp_client.py` – Client that calls the greeting service.  
- `main.py` – Example entry point that demonstrates FastAPI, which can be used to wrap up FastMCP server.  
- `test_main.http` – HTTP test definition for the FastAPI server.

## Running the Server

```bash
python fastmcp_math_server.py
```

The server will start on `http://127.0.0.1:8000/mcp`.

## Testing the Server

Use the provided clients to interact with the server:

```bash
python fastmcp_math_client.py
```

The client will list available tools and perform an `add` operation.

## License

This example is provided for educational purposes.
