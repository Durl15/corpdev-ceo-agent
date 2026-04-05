"""
CorpDev CEO Agent — FastAPI Backend
DJ AI Business Consultant LLC
Railway deployment
"""

import os
import json
import re
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="CorpDev CEO Agent", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-20250514"

SYSTEM_PROMPT = """You are CorpDev CEO Agent, a corporate intelligence assistant specialized in finding executive contact information.

When given a company or executive name, use web search to gather:
- Full name and current title
- Company name and HQ location
- Direct email (or likely email pattern based on domain)
- Phone number (direct or main line)
- LinkedIn profile URL
- Company website
- Industry and employee count
- One strategic intelligence note (recent news, funding, expansion, key initiative)

Return your findings as a JSON array using this exact schema:

[
  {
    "name": "Full Name",
    "title": "Current Title",
    "company": "Company Name",
    "industry": "Industry",
    "hq": "City, State",
    "email": "email@domain.com or pattern like firstname@company.com",
    "email_confidence": "confirmed|likely|pattern",
    "phone": "+1 (555) 000-0000 or main: (555) 000-0000",
    "linkedin": "https://linkedin.com/in/...",
    "website": "https://company.com",
    "employees": "500-1,000",
    "intel": "One sentence of strategic intelligence about this person or company",
    "confidence": 85
  }
]

Return ONLY the JSON array, no markdown, no explanation. If multiple executives found, return all of them.
Fill missing fields with "Not found". Confidence is 0-100 based on how verified the data is."""


class SearchRequest(BaseModel):
    query: str
    mode: str = "company"
    industry: str = "All"


class SearchResponse(BaseModel):
    contacts: list
    raw: str
    query: str


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.get("/health")
async def health():
    return {"status": "ok", "agent": "CorpDev CEO Agent", "model": MODEL}


@app.post("/api/search", response_model=SearchResponse)
async def search(req: SearchRequest):
    if not ANTHROPIC_API_KEY:
        raise HTTPException(status_code=500, detail="ANTHROPIC_API_KEY not configured")

    industry_hint = f" (industry focus: {req.industry})" if req.industry != "All" else ""

    if req.mode == "company":
        user_prompt = (
            f"Find the CEO and top executives with contact information for: {req.query}{industry_hint}. "
            f"Search for their current leadership team, email addresses, phone numbers, and LinkedIn profiles. "
            f"Return as JSON array."
        )
    else:
        user_prompt = (
            f"Find contact information for executive: {req.query}{industry_hint}. "
            f"Search for their current company, title, email, phone, and LinkedIn. "
            f"Return as JSON array."
        )

    payload = {
        "model": MODEL,
        "max_tokens": 4000,
        "system": SYSTEM_PROMPT,
        "tools": [{"type": "web_search_20250305", "name": "web_search"}],
        "messages": [{"role": "user", "content": user_prompt}],
    }

    headers = {
        "Content-Type": "application/json",
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "anthropic-beta": "web-search-2025-03-05",
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(ANTHROPIC_URL, json=payload, headers=headers)

    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)

    data = resp.json()

    text_parts = [
        block["text"]
        for block in data.get("content", [])
        if block.get("type") == "text"
    ]
    raw_text = "\n".join(text_parts)

    contacts = []
    try:
        json_match = re.search(r"\[[\s\S]*\]", raw_text)
        if json_match:
            contacts = json.loads(json_match.group())
    except Exception:
        pass

    return SearchResponse(contacts=contacts, raw=raw_text, query=req.query)


app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
