from PlayerClass import Player
import sys
import random
import re


def add_new_player():
    passed = input("please enter the authorised password:\n")
    count = 0

    while passed != "Password123":
        count += 1
        if count >= 5:
            print("you have had too many attempts")
            main_menu_2()
        passed = input("please enter the authorised password:\n")
    else:
        with open('Players.txt', 'a+') as player_file:
            new_player = Player((input("username:\n")), "")
            while True:
                new_player.password = input("Password:\n")
                if len(new_player.password) not in range(6, 12):
                        print("Make sure your password is at least 6 and less than 12 letters")
                elif re.search('[0-9]', new_player.password) is None:
                        print("Make sure your password has a number in it")
                elif re.search('[A-Z]', new_player.password) is None:
                        print("Make sure your password has a capital letter in it")
                else:
                    break
            if (new_player.name + " " + new_player.password) in open('Players.txt').read():
                    print("sorry that username and password are already being used")
                    sys.exit()
            player_file.write(new_player.name)
            player_file.write(" ")
            player_file.write(new_player.password)
            player_file.write("\n")
            main_menu()


def check_player_1():
    player_1_name = input("player 1, please enter your username:\n")
    player_1_password = input("player 1, please enter your password: \n")
    if (player_1_name + " " + player_1_password) in open('Players.txt').read():
        print("you have been cleared")
        print("welcome back", player_1_name)
        check_player_2(player_1_name, player_1_password)
    else:
        print("those credentials don't exist sadly")
        sys.exit()


def check_player_2(player_1_name, player_1_pass):
    player_2_name = input("player 2, please enter your username:\n")
    player_2_password = input("player 2, please enter your password: \n")
    if (player_2_name, player_2_password) == (player_1_name, player_1_pass):
        print("sorry that is the same as player 1 credentials")
    else:
        if (player_2_name + " " + player_2_password) in open('Players.txt').read():
            print("you have been cleared")
            print("welcome back", player_2_name)
            round_1(player_1_name, player_2_name)
        else:
            print("those credentials don't exist sadly")
            sys.exit()


def round_1(player_1, player_2):
    round_total = 0
    scores_1 = []
    scores_2 = []
    player_1_total = 0
    player_2_total = 0
    for rounds in range(1, 6):
        print("\nwelcome to round", rounds,  "\n")
        for y in range(2):
            dice = random.randint(1, 6)
            print(player_1, "round", rounds, ", die", y + 1)
            print(dice, "\n")
            round_total += dice
            scores_1.append(dice)
            player_1_total += dice
            if len(scores_1) == 2:
                if scores_1[0] == scores_1[1]:
                    print("welcome too the bonus round")
                    extra_die = random.randint(1, 6)
                    print("your extra die scored you an extra", extra_die, player_1)
                    player_1_total += extra_die
                    round_total += extra_die
                else:
                    print("no bonus round")
                if round_total % 2 == 0:
                    print("Well Done, your number was even and has gained 10 points")
                    player_1_total += 10
                    round_total = 0
                else:
                    if (player_1_total - 5) < 0:
                        player_1_total = 0
                    else:
                        print("Unlucky, your number was odd so you loose 5 points")
                        player_1_total -= 5
                    round_total = 0
                scores_1 = []
            print(player_1, "round", rounds, " total is", player_1_total)
            input("press enter for next die role")

        for x in range(2):
            dice = random.randint(1, 6)
            print(player_2, "round", rounds, ", die", x + 1)
            print(dice, "\n")
            scores_2.append(dice)
            player_2_total += dice
            if len(scores_2) == 2:
                if scores_2[0] == scores_2[1]:
                    print("welcome too the bonus round")
                    extra_die = random.randint(1, 6)
                    print("your extra die scored you an extra", extra_die, player_2)
                    player_2_total += extra_die
                    round_total += extra_die
                else:
                    print("no bonus round")
                if round_total % 2 == 0:
                    print("Well Done, your number was even and has gained 10 points")
                    player_2_total += 10
                    round_total = 0
                else:
                    if (player_2_total - 5) < 0:
                        player_2_total = 0
                    else:
                        print("Unlucky, your number was odd so you loose 5 points")
                        player_2_total -= 5
                    round_total = 0
                scores_2 = []
            print(player_1, "round", rounds, " total is", player_1_total)
            input("press enter for next die role")
        print(player_1, "round", rounds, " total is", player_1_total)
        print(player_2, "round", rounds, " total is", player_2_total)
    winner(player_1_total, player_2_total, player_1, player_2)


def winner(player_1_total, player_2_total, player_1, player_2):
    while player_1_total == player_2_total:
        print("since you both have the same score you are allowed more die rolls")
        dice2 = random.randint(1, 6)
        print(player_1, "your dice is", dice2)
        dice = random.randint(1, 6)
        print(player_2, "your die is", dice)
        player_2_total += dice
        player_1_total += dice2
    else:
        if player_1_total > player_2_total:
            print("well done player 1, you Win")
            with open("leaderboard.txt", "a+")as the_leaders:
                the_leaders.write(player_1)
                the_leaders.write(" ")
                the_leaders.write(str(player_1_total))
                the_leaders.write("\n")
        else:
            print("well done player 2, you Win")
            with open("leaderboard.txt", "a+")as the_leaders:
                the_leaders.write(player_2)
                the_leaders.write(" ")
                the_leaders.write(str(player_2_total))
                the_leaders.write("\n")
        leader_board()


def get_score(element):
    return element[-3::]


def leader_board():
    names = []
    top_5 = []
    with open("leaderboard.txt", "r") as leaders:
        for lines in leaders:
            names.append(lines[0:-1])
    names.sort(key=get_score, reverse=True)
    for y in range(len(names)):
        top_5.append(names[y])
    top_5_leaders(top_5)


def top_5_leaders(top_5):
    print("These are the top 5 leaders:")
    for lead in range(len(top_5)):
        print((lead + 1), ".", top_5[lead-1])


def main_menu():
    print("Main Menu")
    print("1.Play Game")
    print("2.Add New Player")
    print("3.Leader Board")
    choice()


def main_menu_2():
    print("Main Menu")
    print("1.Play Game")
    print("2.Leader Board")
    choice_2()


def choice_2():
    user_choice = input("please enter you choice:\n")
    if user_choice == "1":
        check_player_1()
    elif user_choice == "2":
        leader_board()
    else:
        print("sorry didn't get that input can you please repeat")
        choice_2()


def choice():
    user_choice = input("please enter you choice:\n")
    if user_choice == "1":
        check_player_1()
    elif user_choice == "2":
        add_new_player()
    elif user_choice == "3":
        leader_board()
    else:
        print("sorry didn't get that input can you please repeat")
        choice()


if __name__ == "__main__":
    main_menu()

