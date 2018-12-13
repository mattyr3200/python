import random


def names():
    with open("names", "r") as text_file:
        name = input("what is your name?\n")
        if name in text_file.read():
            print("your in")
        else:
            print("we will add your name now\n")
            name_add(name)


def name_add(name_to_add):
    with open("names", "a") as text_file:
        text_file.write(name_to_add)
        text_file.write("\n")
        text_file.close()


"""
def game():
    count = 0
    var1 = []
    for x in range(100):
        var = random.randint(1, 1000)

        while var in var1:
            var = random.randint(1, 1000)
        else:
            var1.append(var)
            var1.sort()
        count += var
    print(count)
"""
if __name__ == "__main__":
    names()
