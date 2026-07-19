from aiohttp import web
import asyncio
import json
from matcher import Matcher

matcher = Matcher()

routes = web.RouteTableDef()

@routes.post("/signals")
async def receive_signal(request):
    sig = await request.json()
    # broadcast to agents or store
    matcher.record_signal(sig)
    return web.json_response({"ok": True})

@routes.post("/intent")
async def receive_intent(request):
    intent = await request.json()
    match = matcher.match_intent(intent)
    if match:
        # settle on-chain
        await matcher.settle_onchain(match)
    return web.json_response({"ok": True, "matched": bool(match)})

app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, port=8001)
