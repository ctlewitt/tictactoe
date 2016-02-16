from two_player import TicTacToe
import two_player

# run game:
print "Welcome to TicTacToe"
# get mode, size, first player as appropriate and set up game
game_type = TicTacToe.get_game_type()
if game_type == TicTacToe.TWO_PLAYER_MODE:
    size = TicTacToe.get_size()
    two_player.my_game = TicTacToe(game_type, size)
else:
    difficulty = TicTacToe.get_difficulty_choice()
    player_xo_choice = TicTacToe.get_player_xo_choice()
    two_player.my_game = TicTacToe(game_type, TicTacToe.MIN_BOARD, player_xo_choice, difficulty)

# play until someone wins or quits or there is a draw
while two_player.my_game.winner == TicTacToe.EMPTY and not two_player.my_game.draw() and not two_player.my_game.quit:
    two_player.my_game.print_board()
    two_player.my_game.get_move()
    two_player.my_game.check_for_winner()
    two_player.my_game.trade_turns()

# game over: print result
if two_player.my_game.quit:
    print "Too bad. Play again soon!"
else:
    two_player.my_game.print_board()
    if two_player.my_game.winner != TicTacToe.EMPTY:  # there is a winner
        two_player.my_game.congratulate_winner()
    else:  # no winner: tie
        print "Tie!  Play again soon!"
