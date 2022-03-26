from gameComponents import _init_
from gameComponents import gameVars, winLose

while gameVars.player_choice is False:
    _init_.executing_functions()

    if gameVars.player_lives == 0:
        winLose.winorlose("lost")
    elif gameVars.computer_lives == 0:
        winLose.winorlose("won")
    else:
        gameVars.player_choice = False
