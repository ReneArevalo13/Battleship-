# Battleship game: one player vs computer

class Battleship(object):

    @staticmethod
    def build(head, length, direction):
        #method to build an instance of a battleship
        #head:coordinate on game grid of where the head of the ship should be   
        #length: how long (how many spaces should the ship span)
        #direction: in what direction should the ship go in N,E,S,W 
        # ex: b1 = Battleship.build((1,1), 5, "N"), head at (1,1), length of 5 pointing North 
        #        
        body = [] #empty list to build the body of the battleship

        #logic to add length to the body in the given direction
        for i in range(length):
            if direction == "N":
                element = (head[0], head[1] - i)
            elif direction == "S":
                element = (head[0], head[1] + i)
            elif direction == "E":
                element = (head[0] - i, head[1])
            elif direction == "W":
                element = (head[0] + i, head[1])
            
            body.append(element)
        
        return Battleship(body)

        

    def __init__(self, body):
        self.body = body

def render_battleship(width, height, battleships):
    border = ("+" + "-" * width + "+")
    print(border)
    board = []

    #create empty board
    for x in range(width):
        board.append(" " for y in range(height))

    for b in battleships:
        for x, y in b.body:
            board[x][y] = "O"



    print(board)
    print(border)
    
     

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




#if __name__ == "__main__":

 
   # shots = []

   # while True:
  #     shot = user_input()
   #     shots.append(shot)
   #     render_board(10, 10, shots)