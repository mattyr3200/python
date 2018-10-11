with open("names", "r") as textfile:
    name = input("what is your name?\n")
    while name in textfile.read():
        print("your in")
        break
    else:
        print("your not")