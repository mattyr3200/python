def sub_name():
    try:
        sub = input("what subroutine would you like top go to:\n")
        sub_to_go = sub + "()"
        exec(sub_to_go)
    except NameError or TypeError:
        print("sorry that wasn't valid.")


def mathew():
    print("hello")


if __name__ == "__main__":
    sub_name()
