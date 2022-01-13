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
                element = (head[0] + i, head[1])
            elif direction == "W":
                element = (head[0] - i, head[1])
            
            body.append(element)
        
        return Battleship(body)

    def __init__(self, body):
        self.body = body
        self.hits = [False] * len(body) #create array that holds hits, when hit, False -> True

    def body_index(self, location):
        try:
            return self.body.index(location)
        except ValueError:
            return None
    def is_destroyed(self):
        return all(self.hits)

class GameState(object):
    #class to control the gamestate 
    #battleships generated at beginning of game and passed in (not changing)
    #input board dimesions height, width
    #include empty shots list to hold shots 

    def __init__(self, battleships, height, width):
        self.battleships = battleships
        self.width = width
        self.height = height
        self.shots = []
    
    def take_shot(self, shot_location):
        #function to update whether battleship was hit
        is_hit = False
        for b in self.battleships:
            idx = b.body_index(shot_location)
            if idx is not None:
                is_hit = True
                b.hits[idx] = True
                break
        self.shots.append(Shot(shot_location, is_hit))
    
    def endgame(self):
        #for each battleship is the ship destroyed
        #if yes return True, else False
        return all([b.is_destroyed() for b in self.battleships])







class Shot(object):
    #class to hold hit/miss
    def __init__(self, location, is_hit):
        self.location = location
        self.is_hit = is_hit


def render_battleship(width, height, battleships):
    border = ("+" + "-" * width + "+")
    print(border)
    board = []

    #create empty board
    for x in range(width):
        row = []
        for y in range(height):
            row.append(None)
        board.append(row)

    #add battleships to the board with character
    for b in battleships:
        for x, y in b.body:
            board[x][y] = "*"

    # go through the rows and append the newly added ships to the board
    for y in range(height):
        row = []
        for x in range(width):
            row.append(board[x][y] or " ")
        print("|" + "".join(row) + "|")

    print(border)
    
     
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


def render(game, show_battleships = False):
    # function to render the game board with for a given height and width
    border = ("+" + "-" * game.width + "+")
    print(border)
    board = []

    #create empty board
    for x in range(game.width):
        row = []
        for y in range(game.height):
            row.append(None)
        board.append(row)
    
    #add battleships to the board with character
    if show_battleships:
        for b in game.battleships:
            for x, y in b.body:
                board[x][y] = "~"
    
    #add shots taken to the game board
    for s in game.shots:
        x, y = s.location
        if s.is_hit:
            ch = "H" #represents a hit
            #print("HIT")
        else:
            ch = "M" #represents a miss
            #print("MISS")
        board[x][y] = ch


    # go through the rows and append the newly added ships to the board
    for y in range(game.height):
        row = []
        for x in range(game.width):
            row.append(board[x][y] or " ")
        print("|" + "".join(row) + "|")

    print(border)
    



def user_input():
    # function to initialize the game by asking where the player wants to shoot on the board
    inp = input("Where do you want to shoot? [X,Y]\n") # comes in as a string
    #print(inp)
    x_string, y_string = inp.split(",") # split the input string at the "," and store
    x = int(x_string)
    y = int(y_string)
    return x, y #output as a tuple


if __name__ == "__main__":
    battleships = [Battleship.build((1,1), 2, "N")]
                    # ,Battleship.build((5,8), 5, "N"),
                    # Battleship.build((2,3), 4, "E")]

    game = GameState(battleships, 10, 10)
    # shots = [(1,1), (0,0), (5,7)]

    # for sh in shots:
    #     game.take_shot(sh)

    #main game loop
    while True:
        x, y = user_input()
        game.take_shot((x,y))
        render(game)

        #ENDGAME
        if game.endgame():
            print("YOU WIN!!")
            break




        
    
    








# for sh in game.shots:
#     print(sh.location)
#     print(sh.is_hit)
#     print("_____")

# for b in game.battleships:
#     print(b.body)
#     print(b.hits)
#     print("_____")
            
 
   # shots = []

   # while True:
  #     shot = user_input()
   #     shots.append(shot)
   #     render_board(10, 10, shots)
