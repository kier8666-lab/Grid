from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import datetime

app = FastAPI(title="Mock Agent")

class RunRequest(BaseModel):
    agent: str = "unknown"
    trace_id: str = "DL-local"

@app.post("/run")
async def run(request: RunRequest):
    await asyncio.sleep(0.2)
    return {
        "agent": request.agent,
        "trace_id": request.trace_id,
        "status": "OK",
        "ts": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
    }
