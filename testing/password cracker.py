import string
import random
password = "Strek123!"
already_done = []


def logic_logarithm():
    cracker = ""
    while 1:
        if cracker != password:
            size = 9
            chars = string.digits + string.punctuation + string.ascii_letters
            cracker = ''.join(random.choice(chars) for _ in range(size))
            if cracker not in already_done:
                already_done.append(cracker)
                print(already_done)
        else:
            break
    print("your password is:\n", cracker)


if __name__ == "__main__":
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.punctuation)
    logic_logarithm()

