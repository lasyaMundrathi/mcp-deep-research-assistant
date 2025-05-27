import asyncio
from mcp.server.fastmcp import FastMCP
from agents import run_research

# Create FastMCP instance
mcp = FastMCP("crew_research")

@mcp.tool()
async def crew_research(query: str) -> str:
    """Run CrewAI-based research system for given user query. Can do both standard and deep web search.

    Args:
        query (str): The research query or question.

    Returns:
        str: The research response from the CrewAI pipeline.
    """
    try:
        # Since run_research is not async, we'll run it in a thread pool
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, run_research, query)
        return result
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")