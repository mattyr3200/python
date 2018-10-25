import string
import random


def password(size=random.randint(6, 12), chars=string.digits + string.punctuation + string.ascii_letters):
    print("creating password...")
    print(''.join(random.choice(chars) for _ in range(size)))

password()
