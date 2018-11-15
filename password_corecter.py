
import re


def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) not in range(6, 12):
            print("Make sure your password is at least 8 and less than 12 letters")
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]', password) is None:
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password seems fine")
            break


if __name__ == "__main__":
    validate()
