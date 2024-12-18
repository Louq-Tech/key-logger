import asyncio
from websockets import serve
import websockets
from formatting import format

async def receive_key(websocket):
    try:
        async for message in websocket:
            format(message)
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed normally (1000 OK).")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed unexpectedly.")

async def main():
    async with serve(receive_key, "localhost", 8765, ping_interval=None, ping_timeout=None) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())