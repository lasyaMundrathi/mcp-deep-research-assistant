# Deep Researcher: Multi-Agent Research Assistant (Streamlit & MCP)

A modular, AI-powered research assistant that performs in-depth web research and summarizes findings with citations. Built with [CrewAI](https://github.com/joaomdmoura/crewAI), enhanced by [Linkup](https://linkup.dev/) for real-time search, and accessible via Streamlit or as an MCP tool for IDEs (e.g., Cursor).
## 🏗️ System Architecture
<img src="https://github.com/user-attachments/assets/3ec33263-7d27-4f6f-a42c-ed9d29b65a12" alt="Architecture Flow of Multi-Agent Research System" width="300"/>

---

## Key Components

### Agents (CrewAI)

* **Web Search Agent**: Fetches real-time internet results.
* **Research Analyst Agent**: Synthesizes, deduplicates, and fact-checks findings.
* **Technical Writer Agent**: Composes a well-cited article.

### Tools

* **Linkup Search Tool**: Interfaces with Linkup API for reliable, real-time search.

### User Interfaces

* **Streamlit UI**: Query and view responses in-browser.
* **MCP Server**: Call the researcher from any IDE supporting MCP (e.g., Cursor).

---

## How It Works

1. User enters a query (Streamlit or MCP).
2. CrewAI workflow:

   * Web Search Agent collects sources
   * Analyst Agent reviews/verifies
   * Writer Agent composes the result
3. Final response shown in UI or returned to IDE.

---

## Setup

### Prerequisites

* Python 3.11+
* [Linkup API Key](https://linkup.dev)

### Run Streamlit App

```bash
streamlit run app/streamlit_app.py
```

### Run as MCP Server (for IDEs like Cursor)

```bash
python server.py
```

Add to your `mcp.json`:

```json
{
  "mcpServers": {
    "crew_research": {
      "command": "uv",
      "args": ["--directory", "./Multi-Agent-deep-researcher-mcp-windows-linux", "run", "server.py"],
      "env": {"LINKUP_API_KEY": "your_linkup_api_key_here"}
    }
  }
}
```

---

## Folder Structure

```
deep-researcher/
├── agents/
│   ├── web_search_agent.py
│   ├── research_analyst.py
│   └── technical_writer.py
├── tools/
│   └── linkup_tool.py
├── app/
│   └── streamlit_app.py
├── server.py
├── crewai_orchestration.py
├── requirements.txt
└── README.md
```

---

## Credits

* [CrewAI](https://github.com/joaomdmoura/crewAI)
* [Linkup API](https://linkup.dev)
* MCP Client from [Cursor](https://www.cursor.so/)

---

