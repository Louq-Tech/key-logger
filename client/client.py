import asyncio
from websockets import connect
from dotenv import load_dotenv
import os
import keyboard

load_dotenv()

websocket_url = os.getenv("WEBSOCKET_URL")

async def send_key(key_pressed):
    async with connect(websocket_url) as websocket:
        await websocket.send(key_pressed)

def on_key_event(event):
    key = event.name
    asyncio.run(send_key(key))

if __name__ == "__main__":
    keyboard.on_press(on_key_event)
    keyboard.wait()
