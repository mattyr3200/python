try:
    i = int(input('Enter a number: '))
    j = int(input('Enter a number: '))

    print(i/j)
except ValueError:
    print('Enter a number')
except ZeroDivisionError:
    print('CANNOT DIVIDE BY ZERO')
