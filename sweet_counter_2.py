def sweet_divider():
    number_of_pupils = int(input("how many pupils are there: \n"))
    number_of_sweets = int(input("how many sweets are in your bag: \n"))
    print("number of sweets per pupil: \n", (number_of_sweets // number_of_pupils))
    print("number of sweets left over: \n", (number_of_sweets % number_of_pupils))

if __name__ == '__main__':
    sweet_divider()