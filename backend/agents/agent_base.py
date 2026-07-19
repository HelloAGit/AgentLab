import asyncio
import aiohttp
import os
import random
from abc import ABC, abstractmethod

class AgentBase(ABC):
    def __init__(self, name):
        self.name = name
        self.arena_url = os.getenv("ARENA_URL", "http://localhost:8001")
        self.session = aiohttp.ClientSession()

    @abstractmethod
    async def on_signal(self, sig):
        pass

    async def submit_intent(self, fixture_id, side, stake, odds):
        payload = {
            "agent": self.name,
            "fixture_id": fixture_id,
            "side": side,
            "stake": stake,
            "odds": odds
        }
        await self.session.post(f"{self.arena_url}/intent", json=payload)
