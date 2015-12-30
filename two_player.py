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
draw = False

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
        move = raw_input(player + "'s move (enter coordinates like battleship. e.g., B3): ")
        #check_move
        if len(move) == 2:
            if (valid_first_moves.__contains__(move[0])) and (valid_second_moves.__contains__(move[1])):
                first_move = convert_to_move(move[0])
                second_move = int(move[1]) - 1
                if board[first_move][second_move] == EMPTY:
                    valid_move = True
                    board[first_move][second_move] = player
                else:
                    print "Invalid Move: please select an unoccupied space"
            else:
                print "Invalid Move: must be A-C followed by 1-3"
        else:
            print "Invalid Move: please indicate 2 coordinates"

#checks for winner and draw at same time
def check_for_winner(player):
    temp_player = ""
    temp_player_wins = False
    #check rows
    for row in range(0,3):
        temp_player = board[row][0]
        temp_player_wins = True
        for col in range(0,3):
            if temp_player != board[row][col]:
                temp_player_wins = False
        if temp_player_wins:
            winner = temp_player
            return

    #check cols
    for col in range(0,3):
        temp_player = board[0][col]
        temp_player_wins = True
        for row in range(0,3):
            if temp_player != board[row][col]:
                temp_player_wins = False
        if temp_player_wins:
            winner = temp_player
            print "There is a winner: " + winner
            return

    #check diagonals
    temp_player1 = board[0][0]
    temp_player2 = board[0][2]
    temp_player1_wins = True
    temp_player2_wins = True
    for index in range(0,3):
        if temp_player1 != board[index][index]:
            temp_player1_wins = False
        if temp_player2 != board[index][3-index-1]:
            temp_player2_wins = False
    if temp_player1_wins:
        winner = temp_player1
        return
    if temp_player2_wins:
        winner = temp_player2
        return

def congratulate_winner(player):
    print "Congratulations,", player, " you won!"

def draw():
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] == EMPTY:
                return False
    return True

fill_board()
print "Welcome to TicTacToe"
player = XES
while winner == "" and not draw():
    if player == XES:
        player = OHS
    else:
        player = XES
    print_board()
    print
    get_move(player)
    check_for_winner(player)
print_board()
if winner != "":
    congratulate_winner(player)
else: #tie
    print "Tie!  Play again soon!"