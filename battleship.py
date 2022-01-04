# Battleship game: one player vs computer


def user_input():
    # function to initialize the game by asking where the player wants to shoot on the board
    inp = input("Where do you want to shoot? [X,Y] \n") # comes in as a string
    x_string, y_string = inp.split(",") # split the input string at the "," and store
    x = int(x_string)
    y = int(y_string)
    return x,y