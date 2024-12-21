def append_file(message, log_save_location):
    with open(log_save_location, 'a') as file:
        file.write(message)

# This function is for backspace feature
def read_and_write_file(log_save_location):
    with open(log_save_location, 'r+') as file:
        content = file.read()
        if content:
            file.seek(0)
            file.write(content[:-1])
            file.truncate()
