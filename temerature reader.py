def temperature():
    list_of_temps =[]
    temp_to_list = input("please enter a temperature(remember .00);\n")
    list_of_temps.append(temp_to_list)
    while temp_to_list.isdigit():
        temp_to_list = input("please enter a temperature(remember .00);\n")
        if temp_to_list.isdigit():
            int(temp_to_list)
            list_of_temps.append(temp_to_list)
        print(list_of_temps)
    int(list_of_temps[0])
    print(max(list_of_temps))
    print(min(list_of_temps))
    print(sum(list_of_temps) / int(len(list_of_temps)))

temperature()