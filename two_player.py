import re
import copy

EMPTY = " "
XES = "X"
OHS = "O"
MIN_BOARD = 3
MAX_BOARD = 26
COMPUTER_MODE = 1
TWO_PLAYER_MODE = 2
NOT_OVER = 52


class TicTacToe:
    # initializes TicTacToe game based on size
    def __init__(self, game_type, size=3, player_xo_choice=XES):
        self.game_type = game_type
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
        # whose turn it is
        self.player = XES
        # computer is OHS or XES (whatever person didn't pick)
        if player_xo_choice == XES:
            self.computer = OHS
        else:
            self.computer = XES
        self.prev_move = ()
        self.quit = False
        self.score = NOT_OVER
        self.board_possibilities = {}

    # copy constructor
    def copy_game(self):
        return copy.deepcopy(self)

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

    # MINIMAX
    def do_minimax(self):
        # base case: if gameover, return move and score
        if self.score != NOT_OVER:
            return self.prev_move, self.score
        # recursive step: make list of moves&scores and return min/max depending on
        scores = []
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.board[row][col] == EMPTY:
                    new_game = self.copy_game()
                    new_game.make_move(row, col)
                    new_game.get_score()
                    new_game.trade_turns()
                    #new_game.player is wrong player
                    key = (new_game.player, str(new_game.board))
                    if not my_game.board_possibilities.has_key(key):
                        new_game_move, new_game_score = new_game.do_minimax()
                        my_game.board_possibilities[key] = new_game_move, new_game_score
                    else:
                        new_game_move, new_game_score = my_game.board_possibilities[key]
                    scores.append(((row, col), new_game_score))
        # computer's "turn": computer maximizes own score => get max
        if self.player == self.computer:
            max_score = -2
            max_move = ()
            for ((row_move, col_move), points) in scores:
                if points > max_score:
                    max_score = points
                    max_move = row_move, col_move
            return max_move, max_score

        # person's "turn" computer minimizes person's score => get min
        else:
            min_score = 2
            min_move = ()
            for ((row_move, col_move), points) in scores:
                if points < min_score:
                    min_score = points
                    min_move = row_move, col_move
            return min_move, min_score



    #requests and validates player's next move; once valid move received, records move
    def get_move(self):
        if self.game_type == COMPUTER_MODE and self.player == self.computer:
            print "Computer's move: "
            temp_game = self.copy_game()
            ((first_move, second_move), score) = temp_game.do_minimax()
        else:
            valid_move = False
            while not valid_move:
                move = raw_input(self.player + "'s move (enter coordinates like battleship. e.g., B3; Q to quit): ")
                # check_move
                if move == "Q" or move == "q":
                    valid_move = True
                    self.quit = True
                else:
                    result = re.match('^([A-Z]|[a-z])([0-9]+)$',move)
                    if result is not None:
                        first_move = TicTacToe.convert_to_move(result.group(1))
                        second_move = int(result.group(2)) - 1
                        if 0 <= first_move < self.size and 0 <= second_move < self.size:
                            if self.board[first_move][second_move] == EMPTY:
                                valid_move = True
                                # moved this to end: self.make_move(first_move, second_move)
                            else:
                                print "Invalid Move: please select an unoccupied space"
                        else:
                            print "Invalid Move: must be A-" + chr(ord('A')+self.size - 1) + " followed by 1-" + str(self.size)
                    else:
                        print "Invalid Move: please indicate 2 coordinates (e.g., C2)"
        self.make_move(first_move, second_move)

    #make given move
    def make_move(self, first_move, second_move):
        self.board[first_move][second_move] = self.player
        self.num_moves +=1
        self.prev_move = (first_move, second_move)

    #check if given row has winning move
    def check_winning_row(self, row):
        for col in range(0,self.size):
            if self.board[row][col] != self.player:
                return False
        return True

    #check if given column has winning move
    def check_winning_col(self, col):
        for row in range(0,self.size):
            if self.board[row][col] != self.player:
                return False
        return True

    #check if given move is in diagonal and if it causes a win
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
        if not self.quit:
            (row,col) = self.prev_move
            # check row, col, diagonal (if relevant)
            if self.check_winning_row(row) or self.check_winning_col(col) or self.check_winning_diag(row,col):
                self.winner = self.player

    def get_score(self):
        self.check_for_winner()
        if self.winner != EMPTY:
            if self.winner == self.computer:
                self.score = 1
            elif self.winner != self.computer:
                self.score = -1
        elif self.draw():
            self.score = 0

    # congratulate the winner
    def congratulate_winner(self):
        if self.game_type == COMPUTER_MODE and self.winner == self.computer:
            print "I win!  Play again soon!"
        else:
            print "Congratulations,", self.winner, " you won!"

    # checks if every space has been taken
    def draw(self):
        if self.num_moves >= self.max_moves:
            return True
        return False

    #get the size of the board user wants to play on
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

    @staticmethod
    def get_player_xo_choice():
        while True:
            player_xo_choice = raw_input("Do you want to be X or O (X goes first)? ").upper()
            if player_xo_choice == "X" or player_xo_choice == "O":
                return player_xo_choice
            else:
                print "Invalid choice.  Must choose 'X' or 'O'."

    #find out if playing in 2 player mode or against computer
    @staticmethod
    def get_game_type():
        while True:
            game_type = int(raw_input("Enter 1 to play against computer or 2 to play in two player mode: "))
            if game_type == 1 or game_type == 2:
                return game_type
            else:
                print "You must select 1 or 2."

    # switch whose turn it is
    def trade_turns(self):
        if self.player == XES:
            self.player = OHS
        else:
            self.player = XES



# run game:
# get size of board and prompt for moves until game complete,
# printing the board, checking for win/draw/quit, and switching turns each time
# print results

print "Welcome to TicTacToe"
# get mode, size, first player as appropriate and set up game
game_type = TicTacToe.get_game_type()
if game_type == TWO_PLAYER_MODE:
    size = TicTacToe.get_size()
    my_game = TicTacToe(game_type, size)
else:
    player_xo_choice = TicTacToe.get_player_xo_choice()
    my_game = TicTacToe(game_type, MIN_BOARD, player_xo_choice)

# play until someone wins or quits or there is a draw
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
