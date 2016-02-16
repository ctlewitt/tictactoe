from two_player import TicTacToe

# run game:
print "Welcome to TicTacToe"
# get mode, size, first player as appropriate and set up game
game_type = TicTacToe.get_game_type()
if game_type == TicTacToe.TWO_PLAYER_MODE:
    size = TicTacToe.get_size()
    my_game = TicTacToe(game_type, size)
else:
    difficulty = TicTacToe.get_difficulty_choice()
    player_xo_choice = TicTacToe.get_player_xo_choice()
    my_game = TicTacToe(game_type, TicTacToe.MIN_BOARD, player_xo_choice, difficulty)

# play until someone wins or quits or there is a draw
while my_game.winner == TicTacToe.EMPTY and not my_game.draw() and not my_game.quit:
    my_game.print_board()
    my_game.get_move()
    my_game.check_for_winner()
    my_game.trade_turns()

# game over: print result
if my_game.quit:
    print "Too bad. Play again soon!"
else:
    my_game.print_board()
    if my_game.winner != TicTacToe.EMPTY:  # there is a winner
        my_game.congratulate_winner()
    else:  # no winner: tie
        print "Tie!  Play again soon!"
