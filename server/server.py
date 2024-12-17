import asyncio
from websockets import serve
import websockets
import formatting

async def echo(websocket):
    try:
        async for message in websocket:
            formatting.format(message)
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed normally (1000 OK).")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed unexpectedly.")

async def main():
    async with serve(echo, "localhost", 8765, ping_interval=None, ping_timeout=None) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())