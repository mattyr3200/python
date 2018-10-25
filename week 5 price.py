def price():
    prices = []
    total_price = 0
    for x in range(5):
        number = input("what is the price:\n")
        prices.append(number[:-1])
        total_price += int(number[:-1])
    print("this is the total price, in pounds: \n £", (total_price / 100))
    print("the average of the prices you have given is:\n", total_price / len(prices))
    print("the maximum of the prices you have given is:\n", max(prices))
    print("the minimum of the prices you have given is:\n", min(prices))
price()
