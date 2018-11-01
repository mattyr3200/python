def passwords():
    no_go_words = ["huddersfield", "justinbieber", "cheese", "canalside"]
    username = input("can we please have your username: \n")
    student_id = input("can we please have your student ID; \n")
    no_go_words.append(username)
    no_go_words.append(student_id)
    password = input("please enter your password:\n")
    while (len(password) in range(6, 12)) and password in no_go_words:
        password = input("please enter your password:\n")
    else:
        print("passwords has been changed. \n")
passwords()
