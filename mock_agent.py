from fastapi import FastAPI, Request
import asyncio, datetime

app = FastAPI(title="Mock Agent")

@app.post("/run")
async def run(request: Request):
    payload = await request.json()
    agent = payload.get("agent", "unknown")
    trace_id = payload.get("trace_id", "DL-local")
    await asyncio.sleep(0.2)
    return {
        "agent": agent,
        "trace_id": trace_id,
        "status": "OK",
        "ts": datetime.datetime.utcnow().isoformat()+"Z"
    }
