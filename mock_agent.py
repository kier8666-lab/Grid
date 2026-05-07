from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
import asyncio, datetime, os, secrets

app = FastAPI(title="Mock Agent")

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def get_api_key(api_key: str = Depends(api_key_header)):
    expected_api_key = os.environ.get("API_KEY")
    if not expected_api_key or not secrets.compare_digest(api_key, expected_api_key):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing API Key"
        )
    return api_key

@app.post("/run")
async def run(request: Request, api_key: str = Depends(get_api_key)):
    payload = await request.json()
    agent = payload.get("agent", "unknown")
    trace_id = payload.get("trace_id", "DL-local")
    await asyncio.sleep(0.2)
    return {
        "agent": agent,
        "trace_id": trace_id,
        "status": "OK",
        "ts": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
    }
