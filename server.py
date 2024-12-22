import os
import asyncio
from websockets import serve
import websockets
from text_file_processors.formatting import process_key_message
from dotenv import load_dotenv

load_dotenv()

async def receive_key(websocket):
    try:
        async for message in websocket:
            process_key_message(message, os.getenv("CLOUD_LOG_STORAGE_AREA"))
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed normally (1000 OK).")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed unexpectedly.")

async def main():
    async with serve(receive_key, "localhost", 8765, ping_interval=None, ping_timeout=None) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())