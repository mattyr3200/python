def price():
    prices = []
    total_price = 0
    for x in range(5):
        number = input("what is the price:\n")
        if number[-1].lower() == "p":
            prices.append(number[:-1])
            total_price += int(number[:-1])
        else:
            prices.append(number)
            total_price += int(number)

    print("this is the total price, in pounds: \n£", (total_price / 100))
    print("the average of the prices you have given is:\n£", (total_price / len(prices) / 100))
    print("the maximum of the prices you have given is:\n£", (int(max(prices)) / 100))
    print("the minimum of the prices you have given is:\n£", (int(min(prices)) / 100))
price()
