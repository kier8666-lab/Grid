from fastapi import FastAPI
from pydantic import BaseModel
import asyncio, datetime

app = FastAPI(title="Mock Agent")

class AgentRunRequest(BaseModel):
    agent: str = "unknown"
    trace_id: str = "DL-local"

@app.post("/run")
async def run(payload: AgentRunRequest):
    await asyncio.sleep(0.2)
    return {
        "agent": payload.agent,
        "trace_id": payload.trace_id,
        "status": "OK",
        "ts": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
    }
