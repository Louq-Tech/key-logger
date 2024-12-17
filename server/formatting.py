excluded_keys = ["caps lock", "shift", "right shift", "ctrl", "right ctrl", "alt", "right alt", "up", "right", "down", "left", "home", "end", "page down", "page up", "delete", "print screen", "insert"]
space_keys = ["space", "tab"]
break_line = ["enter"]

def format(message):
    if message not in excluded_keys:
        if message in space_keys:
            with open("./logs.txt", 'a') as file:
                file.write(" ")
            print(end=" ", flush=True)

        elif message in break_line:
            with open("./logs.txt", 'a') as file:
                file.write("\n")
            print()

        elif message == "backspace":
            with open("./logs.txt", 'r') as file:
                content = file.read()
                if content:
                    content = content[:-1]

                with open("./logs.txt", 'w') as file:
                    file.write(content)

        else:
            with open("./logs.txt", 'a') as file:
                file.write(message)
            print(message, end='', flush=True)