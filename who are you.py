def greeting():
    name = str(input("hello, whats your name?\n"))
    if name == "":
        print("hello world")
    else:
        print("hello,", name.capitalize() + ". it is good to meet you.")
greeting()