# CorpDev CEO Agent
DJ AI Business Consultant LLC
Corporate contact intelligence powered by Claude + live web search.

## Stack
- Backend: FastAPI + httpx -> Anthropic API (claude-sonnet-4 + web_search tool)
- Frontend: Vanilla HTML/CSS/JS served by FastAPI
- Deploy: Railway (nixpacks, auto-detects Python)

## Railway Deployment
1. Push repo to GitHub
2. Railway -> New Project -> Deploy from GitHub repo
3. Variables -> ANTHROPIC_API_KEY=sk-ant-...
4. Railway builds and exposes public URL automatically

## Local Dev
  pip install -r requirements.txt
  $env:ANTHROPIC_API_KEY="sk-ant-..."
  uvicorn main:app --reload --port 8000
  Open: http://localhost:8000

## API
  GET  /         Frontend UI
  GET  /health   Health check
  POST /api/search  { "query": "Salesforce", "mode": "company", "industry": "Tech" }
