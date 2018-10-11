def sweet_divider():
    number_of_pupils = int(input("how many pupils are there: \n"))
    while number_of_pupils <= 1:
        number_of_pupils = int(input("how many pupils are there, please enter a value above zero: \n"))
    else:
        number_of_sweets = int(input("how many sweets are in your bag: \n"))
        while number_of_sweets <= 1:
            number_of_sweets = int(input("how many sweets are in your bag, please enter a value above 0: \n"))
        else:
            print("number of sweets per pupil: \n", (number_of_sweets // number_of_pupils))
            print("number of sweets left over: \n", (number_of_sweets % number_of_pupils))
sweet_divider()