def sub_name():
    sub = input("what subroutine would you like top go to: \n ")
    #to_go = sub + "()"

    if sub == "my_name":
        my_name()
    elif sub == "mathew":
        mathew()
    return sub


def mathew():
    print("hello")


def my_name():
    print("help")

print(sub_name())
