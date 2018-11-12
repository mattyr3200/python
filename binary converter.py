def binary_converter():
    print('{:^10}'.format("denary"), "|", '{:^10}'.format("binary"))
    print("----------------------")
    for x in range(1, 127):
        print('{:^10}'.format(x), "|", '{0:08b}'.format(x))

if __name__ == "__main__":
    binary_converter()