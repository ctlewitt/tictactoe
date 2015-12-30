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
        for row in range(0,3):
            new_row = []
            for col in range(0,3):
                new_row.append(EMPTY)
            self.board.append(new_row)
        self.winner = ""
        self.num_moves = 0
        self.max_moves = self.size * self.size
        self.player = player

    # prints current state of board
    def print_board(self):
        self.print_board_row(0)
        for row in range(1,3):
            print "---------"
            self.print_board_row(row)

    # helper function for print_board; prints one row
    def print_board_row(self,row):
        print self.board[row][0],
        for col in range(1,3):
            print "|",
            print self.board[row][col],
        print

#SWITCH STATEMENT OR ENUM WOULD BE BETTER.  COULD ALSO USE ENUM TO HANDLE VALID INPUT CHECKING TOO
    # returns index of board indicated by A,B,or C
    @staticmethod
    def convert_to_move(character):
        if character == 'A':
            return 0
        if character == 'B':
            return 1
        if character == 'C':
            return 2

    #requests and validates player's next move; once valid move received, records move
    def get_move(self):
        valid_move = False
        valid_first_moves = ['A', 'B', 'C'] #REPLACE WITH NUMBER
        valid_second_moves = ['1', '2', '3']
        while not valid_move:
            move = raw_input(self.player + "'s move (enter coordinates like battleship. e.g., B3): ")
            #check_move
            if len(move) == 2:
                if (valid_first_moves.__contains__(move[0])) and (valid_second_moves.__contains__(move[1])):
                    first_move = TicTacToe.convert_to_move(move[0])
                    second_move = int(move[1]) - 1
                    if self.board[first_move][second_move] == EMPTY:
                        valid_move = True
                        self.board[first_move][second_move] = self.player
                    else:
                        print "Invalid Move: please select an unoccupied space"
                else:
                    print "Invalid Move: must be A-C followed by 1-3"
            else:
                print "Invalid Move: please indicate 2 coordinates"

    # checks for winner and draw at same time
    def check_for_winner(self):
        temp_player = ""
        temp_player_wins = False
        #check rows
        for row in range(0,3):
            temp_player = self.board[row][0]
            temp_player_wins = True
            for col in range(0,3):
                if temp_player != self.board[row][col]:
                    temp_player_wins = False
            if temp_player_wins:
                winner = temp_player
                return

        #check cols
        for col in range(0,3):
            temp_player = self.board[0][col]
            temp_player_wins = True
            for row in range(0,3):
                if temp_player != self.board[row][col]:
                    temp_player_wins = False
            if temp_player_wins:
                self.winner = temp_player
                print "There is a winner: " + self.winner
                return

        #check diagonals
        temp_player1 = self.board[0][0]
        temp_player2 = self.board[0][2]
        temp_player1_wins = True
        temp_player2_wins = True
        for index in range(0,3):
            if temp_player1 != self.board[index][index]:
                temp_player1_wins = False
            if temp_player2 != self.board[index][3-index-1]:
                temp_player2_wins = False
        if temp_player1_wins:
            self.winner = temp_player1
            return
        if temp_player2_wins:
            self.winner = temp_player2
            return

    def congratulate_winner(self):
        print "Congratulations,", self.winner, " you won!"

    def draw(self):
        for row in range(0,3):
            for col in range(0,3):
                if self.board[row][col] == EMPTY:
                    return False
        return True


print "Welcome to TicTacToe"
my_game = TicTacToe()
while my_game.winner == "" and not my_game.draw():
    if my_game.player == XES:
        my_game.player = OHS
    else:
        my_game.player = XES
    my_game.print_board()
    print
    my_game.get_move()
    my_game.check_for_winner()
my_game.print_board()
if my_game.winner != "":
    my_game.congratulate_winner()
else: #tie
    print "Tie!  Play again soon!"