import unittest

from Piece import Knight
from chess_engine import game_state
from ai_engine import chess_ai
from enums import Player


def get_board(empty):
    """
        Returns a new instance of the `game_state` class representing a game board.

        Params:
            empty: A boolean indicating whether the board should be initialized as empty.
        Returns:
            A new `game_state` object representing a game board.
            If `empty` is True, the board will be initialized with `Player.EMPTY` values.
            Otherwise, the board will be initialized with the default values defined in the `game_state` class.
        """
    testing_board = game_state()
    if empty:
        testing_board.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]

    return testing_board


class KnightTest(unittest.TestCase):
    """a class for testing knight class methods"""

    def test_valid_piece_takes(self):
        """Test the get_valid_piece_takes() method of the Knight class when there are no valid piece takes."""
        testing_board = get_board(True)
        testing_knight = Knight('n', 5, 3, Player.PLAYER_1)
        valid_moves = testing_knight.get_valid_piece_takes(testing_board)
        expected_result = []
        self.assertEqual(set(valid_moves), set(expected_result))

    def test_valid_piece_takes_surrounded(self):
        """Test the get_valid_piece_takes() method of the Knight class when the knight is surrounded."""
        testing_board = get_board(True)
        testing_knight = Knight('n', 3, 3, Player.PLAYER_1)
        valid_moves = testing_knight.get_valid_piece_takes(testing_board)
        expected_result = []    # No valid moves when surrounded by own pieces
        self.assertEqual(set(valid_moves), set(expected_result))

    def test_valid_piece_takes_corner(self):
        """Test the get_valid_piece_takes() method of the Knight class when the knight is in a corner."""
        testing_board = get_board(False)
        testing_knight = Knight('n', 8, 8, Player.PLAYER_1)
        valid_moves = testing_knight.get_valid_piece_takes(testing_board)
        expected_result = [(6, 7), (7, 6)]    # Only two valid moves in the corner
        self.assertEqual(set(valid_moves), set(expected_result))

    def test_valid_peaceful_moves(self):
        """Test the get_valid_peaceful_moves() method of the Knight class."""
        testing_board = get_board(True)
        testing_knight = Knight('n', 3, 4, Player.PLAYER_1)
        valid_moves = testing_knight.get_valid_peaceful_moves(testing_board)
        expected_result = [(5, 5), (1, 5), (4, 6), (4, 2), (2, 6), (2, 2), (5, 3), (1, 3)]
        self.assertEqual(set(valid_moves), set(expected_result))

    def test_valid_peaceful_moves_center(self):
        """Test the get_valid_peaceful_moves() method of the Knight class when the knight is in the center."""
        testing_board = get_board(True)
        testing_knight = Knight('n', 4, 4, Player.PLAYER_1)
        valid_moves = testing_knight.get_valid_peaceful_moves(testing_board)
        expected_result = [(6, 5), (2, 3), (6, 3), (5, 6), (3, 6), (3, 2), (2, 5), (5, 2)]
        self.assertEqual(set(valid_moves), set(expected_result))

    def test_valid_peaceful_moves_edge(self):
        """Test the get_valid_peaceful_moves() method of the Knight class when the knight is at the edge."""
        testing_board = get_board(True)
        testing_knight = Knight('n', 0, 6, Player.PLAYER_1)
        valid_moves = testing_knight.get_valid_peaceful_moves(testing_board)
        expected_result = [(2, 5), (2, 7), (1, 4)]    # Limited valid moves near the edge
        self.assertEqual(set(valid_moves), set(expected_result))

    def test_piece_moves(self):
        """Test the get_valid_piece_moves() method of the Knight class."""
        testing_board = get_board(True)
        testing_knight = Knight('n', 4, 2, Player.PLAYER_1)
        valid_piece_moves = testing_knight.get_valid_piece_moves(testing_board)
        expected_result = [(2, 1), (3, 4), (6, 1), (5, 4), (3, 0), (2, 3), (5, 0), (6, 3)]
        self.assertEqual(set(valid_piece_moves), set(expected_result))

    def test_evaluate_board(self):
        """Test the evaluate_board() method of the chess_ai class."""
        testing_board = get_board(True)
        ai = chess_ai()
        result = ai.evaluate_board(testing_board, Player.PLAYER_1)
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_fools_mate(self):
        """Test checkmate_stalemate_checker() method of the Board class in a specific scenario called Fool's Mate."""
        testing_board = get_board(True)
        testing_board.move_piece([1, 1], [3, 1], False)
        testing_board.white_turn = False
        testing_board.move_piece([6, 3], [5, 3], False)
        testing_board.white_turn = True
        testing_board.move_piece((1, 2), (2, 2), False)
        testing_board.white_turn = False
        testing_board.move_piece((7, 4), (3, 0), False)
        testing_board.white_turn = True

        testing_board._is_check = True
        result = testing_board.checkmate_stalemate_checker()
        expected_result = 0
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
