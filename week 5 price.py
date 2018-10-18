def price():
    prices = []
    total_price = 0
    for x in range(5):
        number = input("what is the price:\n")
        prices.append(number[:2])
        total_price += int(number[:2])
    print("the average of the prices you have given is:\n", total_price / len(prices))
    print("the maximum of the prices you have given is:\n", max(prices))
    print("the minimum of the prices you have given is:\n", min(prices))
price()