from two_player import TicTacToe
import two_player
import unittest
import test2
from pass_exception import PassException

class TicTacToeTest(unittest.TestCase):
    def test_board_copy(self):
        """Test that once a copy of a game is made, the original and copy store game state independently"""
        game1 = TicTacToe(two_player.TWO_PLAYER_MODE)
        game2 = game1.copy_game()
        game1.make_move(1, 1)
        self.assertNotEqual (game1.board, game2.board)


    def test_board_copy_after_move(self):
        """Test that move is successfully copied with game"""
        game1 = TicTacToe(two_player.TWO_PLAYER_MODE)
        game1.make_move(1, 1)
        game2 = game1.copy_game()
        self.assertEqual(game1.board, game2.board)

    def test_exception_thrown(self):
        """Test that test_board_copy_after_move_should_fail raises and AssertionError"""
        self.assertRaises(PassException, test2.test_board_copy_after_move_should_fail)

#    def test

if __name__ == '__main__':
    unittest.main()