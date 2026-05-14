from fastapi import FastAPI, Request
import datetime

app = FastAPI(title="Mock Agent")

@app.post("/run")
async def run(request: Request):
    payload = await request.json()
    agent = payload.get("agent", "unknown")
    trace_id = payload.get("trace_id", "DL-local")
    return {
        "agent": agent,
        "trace_id": trace_id,
        "status": "OK",
        "ts": datetime.datetime.utcnow().isoformat()+"Z"
    }
