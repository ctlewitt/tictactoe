from two_player import TicTacToe
from pass_exception import PassException


def test_board_copy():
    """Test that once a copy of a game is made, the original and copy store game state independently"""
    game1 = TicTacToe(TicTacToe.TWO_PLAYER_MODE)
    game2 = game1.copy_game()
    game1.make_move(1, 1)
    assert game1.board != game2.board


def test_board_copy_after_move():
    """Test that move is successfully copied with game"""
    game1 = TicTacToe(TicTacToe.TWO_PLAYER_MODE)
    game1.make_move(1, 1)
    game2 = game1.copy_game()
    assert game1.board == game2.board


def test_board_copy_after_move_should_fail():
    """Test that boards that should be unequal are unequal; fails silently, raises exception when passes"""
    game1 = TicTacToe(TicTacToe.TWO_PLAYER_MODE)
    game2 = game1.copy_game()
    game1.make_move(1, 1)
    try:
        assert game1.board != game2.board
    except AssertionError:
        return
    raise PassException, "Passed: altered game board was unequal to original"
