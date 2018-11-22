import time
import random
import sys

"""
    -this is week 6 work
    -there is a subroutine selector
"""
__author__ = " Mathew Reynolds"
__email__ = "mattyr@talktalk.net"
__date__ = "08-11-2018"


def task_selector():
    print("welcome to the task selector")
    while 1:
        try:
            selector = input("please input what task you would like:\n")
            sub_to_go = selector + "()"
            exec(sub_to_go)
        except NameError or TypeError:
            print("sorry that wasn't valid.")


def task_1():
    list_o_things = ["yes", "no", "maybe", "ni!", "hello", "goodbye"]
    name = random.choice(list_o_things)
    return name


def task_2():
    email = input("please input your email: \n")
    split_email = email.split("@")
    if "@" not in email:
        print("this email is invalid")
    elif email[0] == "@":
        print("the email is invalid")
    elif split_email[1] != "pop.ac.uk":
        print("the email is invalid")
    else:
        print("email is valid")
    return email


def task_3():
    email = input("please input your email: \n")
    split_email = email.split("@")
    if "@" not in email:
        print("this email is invalid")
    elif email[0] == "@":
        print("the email is invalid")
    elif split_email[1] != "pop.ac.uk":
        print("the email is invalid")
    else:
        print(split_email[0])


def task_4():
    key_word = "ni!"
    user_def = input("please input your word:\n").lower()
    while 1:
        if user_def != key_word:
            user_def = input("please input your word:\n").lower()
        else:
            sys.exit()


def task_5():
    the_question = input("please input your question: \n")
    the_word = input("please input the word you want to find: \n")
    if the_word in the_question:
        return True
    else:
        return False


def task_6():
    chat_operators = ["Chad Micheal's", "Max Million", "Joe Charleston", "Mathew Reynolds"]
    filler_words = ["Maybe.", "Please tell me more.", "I am pleased to hear about that."]
    email = input("please input your academic email: \n")
    split_email = email.split("@")
    if "@" not in email:
        print("this email is invalid")
        sys.exit()
    elif email[0] == "@":
        print("the email is invalid")
        sys.exit()
    elif split_email[1] != "pop.ac.uk":
        print("the email is invalid")
        sys.exit()
    else:
        print("this email... is valid")
    print("Hello to the university chat room, please wait whilst we connect you to your host.\n")
    time.sleep(2)
    print("you are now connected with", random.choice(chat_operators))
    time.sleep(1)
    while 1:
        question = input("Hello " + split_email[0] + " how can I help you today?\n")
        if question.lower() == "goodbye":
            print("thank you for using this system today. goodbye " + split_email[0])
            sys.exit()
        elif "WIFI" in question.upper():
            print("WIFI is excellent across the campus.")
        elif "library" in question.lower():
            print("The library is closed today")
        elif "deadline" in question.lower():
            print("Your deadline has been extended by two working days")
        else:
            print(random.choice(filler_words))
        prob = round(random.uniform(0, 1), 2)
        if prob <= 0.15:
            print("we have lost connection")
            sys.exit()


if __name__ == "__main__":
    task_selector()
