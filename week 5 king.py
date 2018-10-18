def week5():
    name = str(input("hello, whats your name?\n"))
    if name == "":
        print("hello world")
    elif name.lower() == "arthur":
        print("My Liege! It is good to meet you.")
    else:
        print("hello, Sir", name.capitalize() + ". it is good to meet you.")
week5()