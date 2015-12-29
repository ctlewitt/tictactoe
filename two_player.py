#print board
#print whose turn and ask for move
#read in move
#verify legal move (correct input, square not taken)
#make move
#check if player won
  #only need to check for wins connected to this move
  #but the board is so small it doesn't matter
#


EMPTY = " "
XES = "X"
OHS = "O"
board = []
winner = ""

def fill_board():
    for row in range(0,3):
        new_row = []
        for col in range(0,3):
            new_row.append(EMPTY)
        board.append(new_row)

def print_board():
    print_board_row(0)
    for row in range(1,3):
        print "---------"
        print_board_row(row)

def print_board_row(row):
    print board[row][0],
    for col in range(1,3):
        print "|",
        print board[row][col],
    print

#SWITCH STATEMENT OR ENUM WOULD BE BETTER.  COULD ALSO USE ENUM TO HANDLE VALID INPUT CHECKING TOO
def convert_to_move(character):
    if character == 'A':
        return 0
    if character == 'B':
        return 1
    if character == 'C':
        return 2

#def set_position(player, first_move, second_move):
#    board[first_move][second_move] = player

def get_move(player):
    valid_move = False
    valid_first_moves = ['A', 'B', 'C'] #REPLACE WITH NUMBER
    valid_second_moves = ['1', '2', '3']
    while not valid_move:
        move = input(player,"'s move (enter coordinates like battleship. e.g., B3): ")
        #check_move
        if len(move) == 2:
            if (valid_first_moves.__contains__(move[0])) and (valid_second_moves.__contains__(move[1])):
                first_move = convert_to_move(move[0])
                second_move = move[1] - 1
                if board[first_move][second_move] == EMPTY:
                    valid_move = True
                    board[first_move][second_move] = player
       else:
            print "Invalid Move"

def check_for_winner(player):
    #check rows
    for row in range(0,3):
        
    #check cols
    #check diagonals

fill_board()
print "Welcome to TicTacToe"
player = XES
while winner == "":
    if player == XES:
        player = OHS
    else:
        player = XES
    print_board()
    get_move()
    check_for_winner(player)
congradulate_winner()
