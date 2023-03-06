import os, random


def main():
    # print("Este es mi executable")
    gameloop()


# Refactor method
def exitcode(score):
    print("Would you like to try again?")
    continue_playing = input("y/n: ")

    if continue_playing != "y":
        os.system("clear")
        return False

    score["user"] = 0
    score["cpu"] = 0
    os.system("clear")
    return True


def gamelogic(user, cpu, score):
    if user == cpu:
        print("Tie! nobody wins 😂")
        return

    if user == 0:
        if cpu == 2:
            winnermessage()
            score["user"] += 1
        else:
            losermessage()
            score["cpu"] += 1
    elif user == 1:
        if cpu == 0:
            winnermessage()
            score["user"] += 1
        else:
            losermessage()
            score["cpu"] += 1
    elif user == 2:
        if cpu == 1:
            winnermessage()
            score["user"] += 1
        else:
            losermessage()
            score["cpu"] += 1


def winnermessage():
    print("\033[95mYou win! Congrats! ✨\033[0m")


def losermessage():
    print("\033[91mCPU is the winner, good luck next time ~ 🥲\033[0m")


def gameloop():
    options = ("rock", "paper", "scissors")
    icons = {"rock": "👊", "paper": "🧻", "scissors": "🔪"}
    score = {"user": 0, "cpu": 0}

    active_game = True
    while active_game:
        cpu_index = random.randint(0, 2)

        choose = input("Your choice: ").casefold().strip()
        if choose == "exit":
            os.system("clear")
            break
        # Check if the user selects an existing element from the list and return the index if it is found or -1
        user_index = options.index(choose) if choose in options else -1

        if user_index < 0:
            print(
                "\033[93mPlease choose:\033[0m \n\t👊 rock  \n\t🧻 paper  \n\t🔪 scissors "
            )
            # active_game = exitcode()
            continue

        user_result = options[user_index]
        cpu_result = options[cpu_index]

        os.system("clear")
        # Game logic
        gamelogic(user_index, cpu_index, score)

        print(
            f"\nYou choose => {icons[user_result]} {user_result}\nCPU choose => {icons[cpu_result]} {cpu_result}\n"
        )
        print(
            f"\033[96mCurrent Score:\n\tUser: | {score['user']} | CPU: | {score['cpu']} |\033[0m"
        )

        if score["cpu"] >= 2 or score["user"] >= 2:
            active_game = exitcode(score)
            if not active_game:
                break

        print("\n\033[93m ------- NEXT ROUND ------- \033[0m\n")


main()
