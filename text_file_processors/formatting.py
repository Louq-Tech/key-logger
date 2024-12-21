from text_file_processors.file_io import append_file, read_and_write_file

excluded_keys = ["caps lock", "shift", "right shift", "ctrl", "right ctrl", "alt", "right alt", "up", "right", "down", "left", "home", "end", "page down", "page up", "delete", "print screen", "insert"]
space_keys = ["space", "tab"]
break_line = ["enter"]

def format(message, log_save_location):
    if message not in excluded_keys:
        if message in space_keys:
            append_file(" ", log_save_location)

        elif message in break_line:
            append_file("\n", log_save_location)

        elif message == "backspace":
            read_and_write_file(log_save_location)

        else:
            append_file(message, log_save_location)