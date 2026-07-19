import asyncio
import aiohttp
import os
from typing import Dict

TXLINE_FEED_URL = os.getenv("TXLINE_FEED_URL", "https://txline.example/api/odds")

async def fetch_odds(session: aiohttp.ClientSession) -> Dict:
    async with session.get(TXLINE_FEED_URL, timeout=10) as resp:
        resp.raise_for_status()
        return await resp.json()
