from PlayerClass import Player
import sys
import random


def add_new_player():
    with open('Players.txt', 'a+') as player_file:
        new_player = Player((input("username:\n")), (input("Password:\n")))
        if (new_player.name + " " + new_player.password) in open('Players.txt').read():
                print("sorry that username has been taken")
                sys.exit()
        player_file.write(new_player.name)
        player_file.write(" ")
        player_file.write(new_player.password)
        player_file.write("\n")


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

#player_1, player_2
def round_1():
    round_total = 0
    scores_1 = []
    scores_2 = []
    player_1_total = 0
    player_2_total = 0
    for rounds in range(1,6):
        print("\nwelcome to round", rounds, "\n")
        for y in range(2):
            dice = random.randint(1, 6)
            print("player 1, round", rounds, ", die", y + 1)
            print(dice, "\n")
            round_total += dice
            scores_1.append(dice)
            player_1_total += dice
            if len(scores_1) == 2:
                if scores_1[0] == scores_1[1]:
                    print("welcome too the bonus round")
                    extra_die = random.randint(1, 6)
                    print("your extra die scored you an extra", extra_die)
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

        for x in range(2):
            dice = random.randint(1, 6)
            print("player 2, round", rounds, ", die", x + 1)
            print(dice, "\n")
            scores_2.append(dice)
            player_2_total += dice
            if len(scores_2) == 2:
                if scores_2[0] == scores_2[1]:
                    print("welcome too the bonus round")
                    extra_die = random.randint(1, 6)
                    print("your extra die scored you an extra", extra_die)
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
        print("player 1 your round", rounds, " total is", player_1_total)
        print("player 2 your round", rounds, " total is", player_2_total)
    winner(player_1_total, player_2_total)


def winner(player_1_total, player_2_total):
    if player_1_total > player_2_total:
        print("well done player 1, you Win")
        with open("leaderboard.txt", "a+")as the_leaders:
            the_leaders.write("mathew ", player_1_total)
            the_leaders.write("\n")
    else:
        print("well done player 2, you Win")
        with open("leaderboard.txt", "a+")as the_leaders:
            the_leaders.write("mathew ")
            the_leaders.write(str(player_2_total))
            the_leaders.write("\n")
    leaderboard()


def leaderboard():
    names = []
    scores = []
    with open("leaderboard.txt", "r") as leaders:
        for lines in leaders:
            names.append(lines)
    for i in names:
        scores.append(names[int(i)][-3])




if __name__ == "__main__":
    round_1()
