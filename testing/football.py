def football_counter():
    wins = 0
    draws = 0
    losses = 0
    points = 0
    team_name = input("what is the team name? \n")
    for x in range(0, 5):
        while 1:
            try:
                g_scored = int(input("goal scored in match {0}:\n".format(x + 1)))
                while g_scored > 10:
                    g_scored = int(input("goal scored in match(your number was too high {0}:\n".format(x + 1)))
                break
            except ValueError:
                print("that's not a good number")
        while 1:
            try:
                g_against = int(input("goal scored against {0}:\n".format(x + 1)))
                while g_against > 10:
                    g_against = int(input("goal scored in match(your number was too high {0}:\n".format(x + 1)))
                break
            except ValueError:
                print("not good enough")
        if g_scored > g_against:
            wins += 1
            points += 3
        elif g_scored == g_against:
            draws += 1
            points += 1
        elif g_scored < g_against:
            losses += 1
    print()
    print(team_name)
    print("Wins:    ", wins)
    print("Draws:   ", draws)
    print("losses:  ", losses)
    print("points   ", points)

if __name__ == "__main__":
    football_counter()