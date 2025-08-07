import os
import asyncio

from mcp import stdio_client, StdioServerParameters
from strands import Agent
from strands.tools.mcp import MCPClient
from strands.models import BedrockModel


# MCP server params
SERVER_CMD = "uv"
SERVER_ARGS = ["run", "research_server.py"]

# Model in Bedrock
MODEL_ID = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
REGION = "us-east-1"

def create_mcp_client():
    """
    Creates an MCPClient that connects to your MCP tool server ie research_server
    """
    return MCPClient(lambda: stdio_client(
        StdioServerParameters(
            command="uv",
            args=["run", "research_server.py"],
        )
    ))


async def mcp_chatbot():
    print(" ### Starting MCP ChatBot...")

    # Initialize MCP client
    mcp_client = create_mcp_client()

    # Use context manager to manage MCP lifecycle
    with mcp_client:
        # List tools from the MCP server
        tools = mcp_client.list_tools_sync()

        print("*** Tools loaded from MCP research server:")
        for tool in tools:
            if hasattr(tool, "tool_spec"):
                spec = tool.tool_spec
                print(f" - {spec['name']}: {spec.get('description', 'No description')}")


        # Initialize Claude model via Bedrock
        model = BedrockModel(
            model_id=MODEL_ID,
            region_name=REGION,
            max_tokens=2024,
            temperature=0.3,
            streaming=False
        )

        # Create agent with researcher server MCP tools
        agent = Agent(
            model=model,
            tools=tools,
            system_prompt=(
                "You are an intelligent research documeent finder assistant. "
                "Use tools reasonbly and help with concise details about research papers"
                 "Never assumer , always show the infromation from the document only"
            )
        )

        # Interactive chatbot loop
        print("\n🤖 MCP Research ChatBot is ready! Type 'quit' to exit.\n")
        while True:
            query = input("User: ").strip()
            if query.lower() in {"quit", "exit"}:
                break

            try:
                response = agent(query)
                print(f"\n")
                #print(f"\nResearch Assistant: {response}\n")
            except Exception as e:
                print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(mcp_chatbot())
