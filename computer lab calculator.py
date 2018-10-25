def student_class():
    number_of_students = input("Enter the number of students in the class: \n")
    if number_of_students.isalpha() or number_of_students < "0":
        print("sorry that input was invalid. \n")
    else:
        number_of_pc = input("Enter the number of PC in the lab: \n")
        if number_of_pc > "0" or number_of_pc.isalpha():
            print("sorry that input is wrong. \n")
        else:
            print("sorry that input is wrong. \n")
            print(int(number_of_students) / int(number_of_pc))


student_class()
