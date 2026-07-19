from agent_base import AgentBase
import asyncio

class MomentumAgent(AgentBase):
    async def on_signal(self, sig):
        # If odds move in direction, follow momentum
        side = "back" if sig["pct_change"] < 0 else "lay"
        stake = 1.0
        await self.submit_intent(sig["fixture_id"], side, stake, sig["curr"])

if __name__ == "__main__":
    import asyncio
    a = MomentumAgent("momentum")
    async def run():
        # subscribe to signals endpoint or websocket; here we poll a simple queue
        while True:
            # placeholder: fetch next signal from a queue
            await asyncio.sleep(1)
    asyncio.run(run())
