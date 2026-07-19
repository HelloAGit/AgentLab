import asyncio
from collections import defaultdict

class Matcher:
    def __init__(self):
        self.orderbook = defaultdict(list)  # fixture_id -> list of intents

    def record_signal(self, sig):
        # store for analytics
        pass

    def match_intent(self, intent):
        fid = intent["fixture_id"]
        # naive matching: find opposite side
        opposite = "back" if intent["side"] == "lay" else "lay"
        for i, o in enumerate(self.orderbook[fid]):
            if o["side"] == opposite and abs(o["odds"] - intent["odds"]) < 0.05:
                matched = (intent, o)
                del self.orderbook[fid][i]
                return matched
        self.orderbook[fid].append(intent)
        return None

    async def settle_onchain(self, match):
        # call onchain_client to create settlement tx
        from onchain_client import settle_trade
        await settle_trade(match)
