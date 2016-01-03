import re
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

class TicTacToe:

    # initializes TicTacToe game based on size
    def __init__(self, size=3, player=XES):
        self.size = size
        self.board = []
        for row in range(0,self.size):
            new_row = []
            for col in range(0,self.size):
                new_row.append(EMPTY)
            self.board.append(new_row)
        self.winner = EMPTY
        self.num_moves = 0
        self.max_moves = self.size * self.size
        self.player = player
        self.prev_move = ()

    # prints current state of board
    def print_board(self):
        self.print_board_row(0)
        for row in range(1,self.size):
            print "-----"+"----" * (self.size-2)
            self.print_board_row(row)

    # helper function for print_board; prints one row
    def print_board_row(self,row):
        print self.board[row][0],
        for col in range(1,self.size):
            print "|",
            print self.board[row][col],
        print


    # returns index of board indicated by A,B,or C
    @staticmethod
    def convert_to_move(character):
        return ord(character) - ord('A')

    #requests and validates player's next move; once valid move received, records move
    def get_move(self):
        valid_move = False
        valid_first_moves = ['A', 'B', 'C'] #REPLACE WITH NUMBER
        valid_second_moves = ['1', '2', '3']
        while not valid_move:
            move = raw_input(self.player + "'s move (enter coordinates like battleship. e.g., B3): ")
            #check_move
            result = re.match('^([A-Z]|[a-z])([0-9]+)$',move)
            if result is not None:
                first_move = TicTacToe.convert_to_move(result.group(1))
                second_move = int(result.group(2)) - 1
                if (first_move >= 0 and first_move < self.size) and (second_move >= 0 and second_move < self.size):
                    if self.board[first_move][second_move] == EMPTY:
                        valid_move = True
                        self.board[first_move][second_move] = self.player
                        self.num_moves += 1
                        self.prev_move = (first_move, second_move)
                    else:
                        print "Invalid Move: please select an unoccupied space"
                else:
                    print "Invalid Move: must be A-"+ chr(ord('A')+self.size - 1) + " followed by 1-" + str(self.size)
            else:
                print "Invalid Move: please indicate 2 coordinates (e.g., C2)"


    def check_winning_row(self, row):
        for col in range(0,self.size):
            if self.board[row][col] != self.player:
                return False
        return True

    def check_winning_col(self, col):
        for row in range(0,self.size):
            if self.board[row][col] != self.player:
                return False
        return True

    def check_winning_diag(self, row, col):
        left_right_diag = False
        right_left_diag = False
        if (row == col):
            left_right_diag = True
            for index in range(0, self.size):
                if self.board[index][index] != self.player:
                    left_right_diag = False
        if self.size - 1 - col == row:
            right_left_diag = True
            for index in range(0, self.size):
                if self.board[index][self.size-1-index] != self.player:
                    right_left_diag = False
        return left_right_diag or right_left_diag

    # checks for winner and draw at same time
    def check_for_winner(self):
        (row,col) = self.prev_move
        found_winner = True
        #check row, col, diagonal (if relevant)
        if self.check_winning_row(row) or self.check_winning_col(col) or self.check_winning_diag(row,col):
            self.winner = self.player
        return

    def congratulate_winner(self):
        print "Congratulations,", self.winner, " you won!"

    # checks if every space has been taken
    def draw(self):
        if self.num_moves >= self.max_moves:
            return True
        return False


print "Welcome to TicTacToe"
size = input("What size board would you like to play with? (Enter 3-7) ")
my_game = TicTacToe(size)
while my_game.winner == EMPTY and not my_game.draw():
    if my_game.player == XES:
        my_game.player = OHS
    else:
        my_game.player = XES
    my_game.print_board()
    print
    my_game.get_move()
    my_game.check_for_winner()
my_game.print_board()
if my_game.winner != EMPTY:
    my_game.congratulate_winner()
else: #tie
    print "Tie!  Play again soon!"