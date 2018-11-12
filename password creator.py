import string
import random
from time import sleep


def password():
    chars = string.digits + string.punctuation + string.ascii_letters
    size = random.randint(6, 12)
    sleep(1)
    return ''.join(random.choice(chars) for _ in range(size))

print(password())
