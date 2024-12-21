def append_file(message, log_save_location):
    with open(log_save_location, 'a') as file:
        file.write(message)

# This function is for backspace feature
def read_and_write_file(log_save_location):
    with open(log_save_location, 'r') as file:
        content = file.read()
        if content:
            content = content[:-1]

            with open("./logs.txt", 'w') as file:
                file.write(content)
