"""this is a conversion table for C to F"""
__author__ = "Mathew Reynolds"
__email__ = "mattyr@talktalk.net"
__date__ = "08-11-2018"


def convert():
    print('{:^7}'.format("°C"), '{:^7}'.format("|"), '{:^7}'.format("°F") )
    print('{:^24}'.format("----- + -----"))
    for c in range(-10, +14):
        the_convert = (c * 9 / 5) + 32
        print('{:^10}'.format(c), "|", '{:^10}'.format(the_convert))

if __name__ == "__main__":
    convert()
