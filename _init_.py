from gameComponents import gameVars
from random import randint


def executing_functions():
    print("*_____*WELCOME TO RPS GAME*_____*")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("*_*TEST YOUR LUCK*_*")
    print("Choose your weapon! Or type quit to exit\n")  # \n means "new line"
    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

    if gameVars.player_choice == "quit":
        print("You chose to quit")
        exit()

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("user chose: " + gameVars.player_choice)
    print("computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice:
        print("tie")
    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            gameVars.player_lives -= 1
            print("you lose! player lives:", gameVars.player_lives)
        else:
            print("you win!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "rock":
            gameVars.player_lives -= 1
            print("you lose! player lives:", gameVars.player_lives)
        else:
            print("you win!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            gameVars.player_lives -= 1
            print("you lose! player lives:", gameVars.player_lives)
        else:
            print("you win!")
            gameVars.computer_lives -= 1
