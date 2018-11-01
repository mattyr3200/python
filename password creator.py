import string
import random
from time import sleep


def password(size=random.randint(6, 12), chars=string.digits + string.punctuation + string.ascii_letters):
    sleep(1)
    return ''.join(random.choice(chars) for _ in range(size))

print("creating password...")
print (password(34, 'abc'))
