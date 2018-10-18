def price():
    l = ()
    for x in range(5):
        number = input("what is the price:\n")
        l = (number[:1])

    print(sum(l)/len(l))
    print(max(l))
    print(min(l))
price()