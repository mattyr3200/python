def week5():
    name = str(input("hello, whats your name?\n"))
    if not name:
        print("hello world")
    elif name[:4].capitalize() == "Sir ":
        print("hello, Sir", name[4:].capitalize() + ". it is good to meet you.")
    else:
        print("hello, ", name.capitalize() + ". it is good to meet you.")
week5()