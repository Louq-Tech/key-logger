import asyncio
from websockets import connect
import keyboard

async def send_key(key_pressed):
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send(key_pressed)

def on_key_event(event):
    key = event.name
    asyncio.run(send_key(key))

if __name__ == "__main__":
    keyboard.on_press(on_key_event)
    keyboard.wait()
