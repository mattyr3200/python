def temperature():
    average = 0
    list_of_temps = []
    temp_to_list = input("please enter a temperature;\n")
    average += int(temp_to_list)
    list_of_temps.append(temp_to_list)
    while temp_to_list.isdigit():
        temp_to_list = input("please enter a temperature;\n")
        if temp_to_list.isdigit():
            average += int(temp_to_list)
            print(average)
            list_of_temps.append(temp_to_list)
    print("a non number was entered")
    print("\n")
    print("The maximum temperature you gave was:\n", max(list_of_temps))
    print("The minimum temperature you gave was:\n", min(list_of_temps))
    print("The average temperature you gave was:\n", average / int(len(list_of_temps)))

temperature()