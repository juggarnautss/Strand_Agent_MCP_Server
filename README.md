# MCP Research Server

## Overview

This project demonstrates the power of **AWS strands agents** and how quickly you can build intelligent, context-aware applications. AWS provides a robust foundation for creating agents that can understand, reason, and act on complex data - and with **Model Context Protocol (MCP)** integration, you can extend these capabilities seamlessly.

## Why AWS Agents?

- **Model Driven Orchestration**: Strands leverages model reasoning to plan, orchestrate tasks, and reflect on goals
- **Model and Provider Agnostic**: Work with any LLM provider - Amazon Bedrock, OpenAI, Anthropic, local models. Switch providers without changing your code.
- **Simple MultiAgent Primitives**: Simple primitives for handoffs, swarms, and graph workflows with built-in support for A2A
- **Best in-class AWS integration**: Native tools for AWS service interactions. Deploy easily into EKS, Lambda, EC2, and more. Native MCP tool integration.

## MCP Integration Made Easy

**Model Context Protocol (MCP)** transforms how agents access and utilize external data sources. This project showcases how effortlessly you can:

### Quick Setup
- Connect your AWS agent to local data sources
- Extend agent capabilities with custom tools
- Maintain secure, standardized communication protocols

## Project Structure

```
mcp_server/
├── research_server.py    # Core MCP server implementation
├── mcp_chatbot.py       # Chatbot interface
├── main.py              # Entry point
├── research_papers/     # Document storage
└── requirements.txt     # Dependencies
```

## Getting Started

1. **Install Dependencies**
   ```bash
   uv init
   uv pip install -r requirements.txt
   ```

2. **Run the agent which in turn will spaws the server**
   ```bash
   python mcp_chatbot.py
   ```
   
## Use Cases

- Research paper analysis and summarization
- Document Q&A systems
- Knowledge base integration
- Custom data source connectivity

## AWS strand agent
 - https://strandsagents.com/latest/


## Develop mcp server from scratch
- https://aiinfrahub.com/about-us/building-an-mcp-server-using-fastmcp-and-arxiv/
- https://github.com/juggarnautss/mcp_server_fastmcp_arxiv
