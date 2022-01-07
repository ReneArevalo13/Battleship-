# Battleship game: one player vs computer

def user_input():
    # function to initialize the game by asking where the player wants to shoot on the board
    inp = input("Where do you want to shoot? [X,Y]\n") # comes in as a string
    #print(inp)
    x_string, y_string = inp.split(",") # split the input string at the "," and store
    x = int(x_string)
    y = int(y_string)
    return (x,y) #output as a tuple


def render_board(height, width, shots):
    # function to render the game board with for a given height and width
    border = ("+" + "-" * width + "+")
    print(border)
    shots_set = set(shots)
    
    for y in range(height): #iterate along the vertical, y-axis
        row = []
        for x in range(width): #iterate along the horizontal, x-axis
            if (x, y) in shots_set:
                hit = "X" #symbol for ship being hit
            else:
                hit = " " #empty space for a non hit
            row.append(hit)

        print("|" + "".join(row) + "|") 
    print(border)


if __name__ == "__main__":
    shots = []

    while True:
        shot = user_input()
        shots.append(shot)
        render_board(10, 10, shots)

