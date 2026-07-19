import asyncio
import aiohttp
import os
import json
from detector import SharpMovementDetector
from txline_client import fetch_odds
from aiohttp import web

detector = SharpMovementDetector(window=5, pct_threshold=0.07)
SIGNAL_LOG = "signals.log"

async def poll_loop():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                data = await fetch_odds(session)
                # data expected: list of fixtures with odds
                for f in data.get("fixtures", []):
                    fid = f["id"]
                    odds = f["odds"]["txline"]
                    sig = detector.update(fid, odds)
                    if sig:
                        log_signal(sig)
                        # publish to agents via websocket or REST
                        await publish_signal(sig)
            except Exception as e:
                print("poll error", e)
            await asyncio.sleep(60)  # poll every 60 seconds

def log_signal(sig):
    with open(SIGNAL_LOG, "a") as fh:
        fh.write(json.dumps(sig) + "\n")

async def publish_signal(sig):
    # simple HTTP POST to arena/agents; in production use pub/sub or websockets
    url = os.getenv("SIGNAL_ENDPOINT", "http://localhost:8001/signals")
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=sig)

if __name__ == "__main__":
    asyncio.run(poll_loop())
