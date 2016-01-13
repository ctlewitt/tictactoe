import re

EMPTY = " "
XES = "X"
OHS = "O"
MIN_BOARD = 3
MAX_BOARD = 26


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
        self.quit = False

    # prints current state of board
    def print_board(self):
        self.print_board_row(0)
        for row in range(1,self.size):
            print "-----"+"----" * (self.size-2)
            self.print_board_row(row)
        print

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
        return ord(character.capitalize()) - ord('A')

    #requests and validates player's next move; once valid move received, records move
    def get_move(self):
        valid_move = False
        while not valid_move:
            move = raw_input(self.player + "'s move (enter coordinates like battleship. e.g., B3; Q to quit): ")
            # check_move
            if move == "Q" or move == "q":
                valid_move = True
                my_game.quit = True
            else:
                result = re.match('^([A-Z]|[a-z])([0-9]+)$',move)
                if result is not None:
                    first_move = TicTacToe.convert_to_move(result.group(1))
                    second_move = int(result.group(2)) - 1
                    if 0 <= first_move < self.size and 0 <= second_move < self.size:
                        if self.board[first_move][second_move] == EMPTY:
                            valid_move = True
                            self.board[first_move][second_move] = self.player
                            self.num_moves += 1
                            self.prev_move = (first_move, second_move)
                        else:
                            print "Invalid Move: please select an unoccupied space"
                    else:
                        print "Invalid Move: must be A-" + chr(ord('A')+self.size - 1) + " followed by 1-" + str(self.size)
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
        if row == col:
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
        if not my_game.quit:
            (row,col) = self.prev_move
            # check row, col, diagonal (if relevant)
            if self.check_winning_row(row) or self.check_winning_col(col) or self.check_winning_diag(row,col):
                self.winner = self.player

    def congratulate_winner(self):
        print "Congratulations,", self.winner, " you won!"

    # checks if every space has been taken
    def draw(self):
        if self.num_moves >= self.max_moves:
            return True
        return False

    @staticmethod
    def get_size():
        valid_size = False
        while not valid_size:
            size_input = raw_input("What size board would you like to play with? (Enter " +
                               str(MIN_BOARD) + "-" + str(MAX_BOARD) + ") ")
            result = re.match("^([0-9]+)$", size_input)
            if result is not None:
                size = int(result.group(1))
                if MIN_BOARD <= size <= MAX_BOARD:
                    valid_size = True
                    return size
                else:
                    print "Size must be in range"
            else:
                print "Size must be a number"

    def trade_turns(self):
        if my_game.player == XES:
            my_game.player = OHS
        else:
            my_game.player = XES




#get size of board
#while game still being played
    #print board
    #print whose turn and ask for move
    #read in move
    #verify legal move (correct input, square not taken)
    #make move
    #check if player won or if there is a draw
        #only need to check for wins connected to this move
#print outcome of game
print "Welcome to TicTacToe"
size = TicTacToe.get_size()
my_game = TicTacToe(size)
while my_game.winner == EMPTY and not my_game.draw() and not my_game.quit:
    my_game.print_board()
    my_game.get_move()
    my_game.check_for_winner()
    my_game.trade_turns()
if my_game.quit:
    print "Too bad. Play again soon!"
else:
    my_game.print_board()
    if my_game.winner != EMPTY:
        my_game.congratulate_winner()
    else: #tie
        print "Tie!  Play again soon!"
