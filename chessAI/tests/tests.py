from ..helpers import *
import unittest


# run in top directory with python -m chessAI.tests
# or python -m unittest test

class Test(unittest.TestCase):

    def test_is_valid_pawn_move(self):
        board = Board()
        white_pawn1 = Pawn(WHITE, 3, 3, figDict[WHITE][Pawn])
        black_pawn1 = Pawn(BLACK, 4, 3, figDict[BLACK][Pawn])
        board.add_figure(white_pawn1)
        board.add_figure(black_pawn1)
        print("--------- White Pawn Tests")
        print("----------- Test series 1 (pawn in front)")
        self.assertFalse(is_valid_pawn_move(board, (3, 3), (4, 3)), "Should be False")
        self.assertFalse(is_valid_pawn_move(board, (3, 3), (4, 4)), "Should be False")
        self.assertFalse(is_valid_pawn_move(board, (3, 3), (4, 2)), "Should be False")
        board.move_figure((4, 3), (4, 4))
        print("----------- Test series 2 (pawn diagonally)")
        self.assertTrue(is_valid_pawn_move(board, (3, 3), (4, 3)), "Should be True")
        self.assertTrue(is_valid_pawn_move(board, (3, 3), (4, 4)), "Should be True")
        self.assertFalse(is_valid_pawn_move(board, (3, 3), (4, 2)), "Should be False")
        board.move_figure((3, 3), (5, 7))
        print("----------- Test series 3 (pawn index out of bounds)")
        self.assertFalse(is_valid_pawn_move(board, (5, 7), (6, 6)), "Should be False")
        self.assertTrue(is_valid_pawn_move(board, (5, 7), (6, 7)), "Should be True")
        self.assertFalse(is_valid_pawn_move(board, (5, 7), (6, 8)), "Should be False")
        print("----------- Test series 4 (pawn moves more than one field)")
        self.assertFalse(is_valid_pawn_move(board, (5, 7), (7, 7)), "Should be False")
        board.move_figure((5, 7), (1, 3))
        self.assertTrue(is_valid_pawn_move(board, (1, 3), (3, 3)), "Should be True")
        self.assertFalse(is_valid_pawn_move(board, (1, 3), (3, 4)), "Should be False")
        board.move_figure((4, 4), (3, 3))
        self.assertFalse(is_valid_pawn_move(board, (1, 3), (3, 3)), "Should be False")
        self.assertFalse(is_valid_pawn_move(board, (1, 3), (6, 2)), "Should be False")
        board.move_figure((3, 3), (2, 3))
        self.assertFalse(is_valid_pawn_move(board, (1, 3), (3, 3)), "Should be False")
        self.assertFalse(is_valid_pawn_move(board, (1, 3), (1, 3)), "Should be False")
        self.assertFalse(is_valid_pawn_move(board, (1, 3), (0, 3)), "Should be False")
        board.clear_board()
        white_pawn1.set_position(3, 3)
        black_pawn1.set_position(4, 3)
        board.add_figure(white_pawn1)
        board.add_figure(black_pawn1)
        board.switch_turn()
        print("--------- Black Pawn Tests")
        print("----------- Test series 1 (pawn in front)")
        self.assertFalse(is_valid_pawn_move(board, (4, 3), (3, 3)), "Should be False")
        self.assertFalse(is_valid_pawn_move(board, (4, 3), (3, 4)), "Should be False")
        self.assertFalse(is_valid_pawn_move(board, (4, 3), (4, 2)), "Should be False")
        board.move_figure((3, 3), (3, 2))
        print("----------- Test series 2 (pawn diagonally)")
        self.assertTrue(is_valid_pawn_move(board, (4, 3), (3, 3)), "Should be True")
        self.assertTrue(is_valid_pawn_move(board, (4, 3), (3, 2)), "Should be True")
        self.assertFalse(is_valid_pawn_move(board, (4, 3), (3, 4)), "Should be False")
        board.move_figure((4, 3), (5, 7))
        print("----------- Test series 3 (pawn index out of bounds)")
        self.assertFalse(is_valid_pawn_move(board, (5, 7), (4, 6)), "Should be False")
        self.assertTrue(is_valid_pawn_move(board, (5, 7), (4, 7)), "Should be True")
        self.assertFalse(is_valid_pawn_move(board, (5, 7), (4, 8)), "Should be False")
        print("----------- Test series 4 (pawn moves more than one field)")
        self.assertFalse(is_valid_pawn_move(board, (5, 7), (3, 7)), "Should be False")
        board.move_figure((5, 7), (6, 3))
        self.assertTrue(is_valid_pawn_move(board, (6, 3), (4, 3)), "Should be True")
        self.assertFalse(is_valid_pawn_move(board, (6, 3), (4, 4)), "Should be False")
        board.move_figure((3, 2), (4, 3))
        self.assertFalse(is_valid_pawn_move(board, (6, 3), (4, 3)), "Should be False")
        self.assertFalse(is_valid_pawn_move(board, (6, 3), (1, 2)), "Should be False")
        board.move_figure((4, 3), (5, 3))
        self.assertFalse(is_valid_pawn_move(board, (6, 3), (4, 3)), "Should be False")
        self.assertFalse(is_valid_pawn_move(board, (6, 3), (6, 3)), "Should be False")
        self.assertFalse(is_valid_pawn_move(board, (6, 3), (7, 3)), "Should be False")

    def test_is_valid_knight_move(self):
        board = Board()
        white_knight1 = Knight(WHITE, 1, 1, figDict[WHITE][Knight])
        white_pawn1 = Pawn(WHITE, 2, 3, figDict[WHITE][Pawn])
        black_knight1 = Knight(BLACK, 3, 2, figDict[BLACK][Knight])
        black_pawn1 = Pawn(BLACK, 4, 2, figDict[BLACK][Pawn])
        board.add_figure(white_knight1)
        board.add_figure(white_pawn1)
        board.add_figure(black_knight1)
        board.add_figure(black_pawn1)
        print("--------- White Knight Tests")
        print("----------- Test series 1")
        self.assertTrue(is_valid_knight_move(board, (1, 1), (3, 2)), "Should be True")
        self.assertFalse(is_valid_knight_move(board, (1, 1), (-1, 0)), "Should be False")
        self.assertFalse(is_valid_knight_move(board, (1, 1), (5, 6)), "Should be False")
        self.assertFalse(is_valid_knight_move(board, (1, 1), (2, 3)), "Should be False")
        board.switch_turn()
        print("--------- Black Knight Tests")
        print("----------- Test series 1")
        self.assertTrue(is_valid_knight_move(board, (3, 2), (1, 1)), "Should be True")
        board.move_figure((3, 2), (2, 1))
        self.assertFalse(is_valid_knight_move(board, (2, 1), (1, -1)), "Should be False")
        self.assertFalse(is_valid_knight_move(board, (2, 1), (5, 6)), "Should be False")
        self.assertFalse(is_valid_knight_move(board, (2, 1), (4, 2)), "Should be False")

    def test_is_valid_bishop_move(self):
        board = Board()
        white_bishop1 = Bishop(WHITE, 3, 3, figDict[WHITE][Bishop])
        black_bishop1 = Bishop(BLACK, 4, 4, figDict[BLACK][Bishop])
        board.add_figure(white_bishop1)
        board.add_figure(black_bishop1)
        print("--------- White Bishop Tests")
        print("----------- Test series 1")
        self.assertTrue(is_valid_bishop_move(board, (3, 3), (4, 4)), "Should be True")
        self.assertTrue(is_valid_bishop_move(board, (3, 3), (1, 1)), "Should be True")
        self.assertFalse(is_valid_bishop_move(board, (3, 3), (6, 7)), "Should be False")
        self.assertFalse(is_valid_bishop_move(board, (3, 3), (5, 5)), "Should be False")
        self.assertFalse(is_valid_bishop_move(board, (3, 3), (8, 8)), "Should be False")
        board.switch_turn()
        print("--------- Black Bishop Tests")
        print("----------- Test series 1")
        self.assertTrue(is_valid_bishop_move(board, (4, 4), (3, 3)), "Should be True")
        self.assertTrue(is_valid_bishop_move(board, (4, 4), (2, 6)), "Should be True")
        self.assertFalse(is_valid_bishop_move(board, (4, 4), (2, 2)), "Should be False")
