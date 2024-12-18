def append_file(message):
    with open("./logs.txt", 'a') as file:
        file.write(message)

# This function is for backspace feature
def read_and_write_file():
    with open("./logs.txt", 'r') as file:
        content = file.read()
        if content:
            content = content[:-1]

            with open("./logs.txt", 'w') as file:
                file.write(content)
