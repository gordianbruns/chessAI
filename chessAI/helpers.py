from .game.board import *
from .game.figures import *
from .common.constants import *

import copy


figDict = {WHITE: {Pawn: "♟", Rook: "♜", Knight: "♞", Bishop: "♝", King: "♚", Queen: "♛"},
           BLACK: {Pawn: "♙", Rook: "♖", Knight: "♘", Bishop: "♗", King: "♔", Queen: "♕"}}


def initial_state():
    board = Board()
    for i in range(COLUMNS):
        board.add_figure(Pawn(WHITE, 1, i, figDict[WHITE][Pawn]))
        board.add_figure(Pawn(BLACK, ROWS - 2, i, figDict[BLACK][Pawn]))

    placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

    for i in range(COLUMNS):
        board.add_figure(placers[i](WHITE, 0, i, figDict[WHITE][placers[i]]))
        board.add_figure(placers[i](BLACK, ROWS - 1, i, figDict[BLACK][placers[i]]))

    return board


def print_board(board):
    for i in range(ROWS):
        for j in range(COLUMNS):
            figure = board.get_figure(i, j)
            if figure is None:
                print(" - ", end='')
            else:
                print("", figure, "", end='')
        print()


def transition_function(board, start_position, end_position):
    copy_board = copy.deepcopy(board)
    copy_board.move_figure(start_position, end_position)
    copy_board.switch_turn()
    return copy_board


def is_in_bounds(position):
    return (0 <= position[0] <= ROWS - 1) and (0 <= position[1] <= COLUMNS - 1)


def move_generator(board):
    moves = []
    if board.get_turn() == WHITE:
        for pos, figure in board.get_white_figures().items():
            if type(figure) == Pawn:
                moves.extend(generate_pawn_moves(board, pos))
            if type(figure) == Knight:
                moves.extend(generate_knight_moves(board, pos))
            if type(figure) == Bishop:
                moves.extend(generate_bishop_moves(board, pos))
            if type(figure) == Rook:
                moves.extend(generate_rook_moves(board, pos))
            if type(figure) == Queen:
                moves.extend(generate_queen_moves(board, pos))
            if type(figure) == King:
                moves.extend(generate_king_moves(board, pos))
    else:
        for pos, figure in board.get_black_figures().items():
            if type(figure) == Pawn:
                moves.extend(generate_pawn_moves(board, pos))
            if type(figure) == Knight:
                moves.extend(generate_knight_moves(board, pos))
            if type(figure) == Bishop:
                moves.extend(generate_bishop_moves(board, pos))
            if type(figure) == Rook:
                moves.extend(generate_rook_moves(board, pos))
            if type(figure) == Queen:
                moves.extend(generate_queen_moves(board, pos))
            if type(figure) == King:
                moves.extend(generate_king_moves(board, pos))
    moves.append(generate_castle_moves(board))
    return moves


def generate_pawn_moves(board, position):   # assumes that it is a pawn
    moves = []
    if board.get_turn() == WHITE:
        if is_valid_pawn_move(board, position, (position[0] + 1, position[1] - 1)):
            if not is_check(transition_function(board, position, (position[0] + 1, position[1] - 1))):
                moves.append([position, (position[0] + 1, position[1] - 1)])
        if is_valid_pawn_move(board, position, (position[0] + 1, position[1])):
            if not is_check(transition_function(board, position, (position[0] + 1, position[1]))):
                moves.append([position, (position[0] + 1, position[1])])
        if is_valid_pawn_move(board, position, (position[0] + 1, position[1] + 1)):
            if not is_check(transition_function(board, position, (position[0] + 1, position[1] + 1))):
                moves.append([position, (position[0] + 1, position[1] + 1)])
    else:
        if is_valid_pawn_move(board, position, (position[0] - 1, position[1] - 1)):
            if not is_check(transition_function(board, position, (position[0] - 1, position[1] - 1))):
                moves.append([position, (position[0] - 1, position[1] - 1)])
        if is_valid_pawn_move(board, position, (position[0] - 1, position[1])):
            if not is_check(transition_function(board, position, (position[0] - 1, position[1]))):
                moves.append([position, (position[0] - 1, position[1])])
        if is_valid_pawn_move(board, position, (position[0] - 1, position[1] + 1)):
            if not is_check(transition_function(board, position, (position[0] - 1, position[1] + 1))):
                moves.append([position, (position[0] - 1, position[1] + 1)])
    return moves


def is_valid_pawn_move(board, start_position, end_position):    # assumes that it is a pawn
    if is_in_bounds(end_position):    # within bounds
        diff_vertical = start_position[0] - end_position[0]
        diff_horizontal = start_position[1] - end_position[1]
        if abs(diff_vertical) == 1:     # one box away
            if abs(diff_horizontal) == 1:   # diagonal
                if board.get_figure(end_position[0], end_position[1]) is not None:  # figure at the position
                    if board.get_turn() == WHITE and diff_vertical == -1:   # checks whether white is going forward
                        if board.get_figure(end_position[0], end_position[1]).get_color() == BLACK:
                            # diagonal figure must be black
                            return True
                    elif board.get_turn() == BLACK and diff_vertical == 1:  # checks whether black is going forward
                        if board.get_figure(end_position[0], end_position[1]).get_color() == WHITE:
                            # diagonal figure must be white
                            return True
            elif abs(diff_horizontal) == 0:     # straight forward
                if board.get_turn() == WHITE and diff_vertical == -1:   # checks whether white is going forward
                    if board.get_figure(end_position[0], end_position[1]) is None:  # no figure can be at the position
                        return True
                elif board.get_turn() == BLACK and diff_vertical == 1:  # checks whether black is going forward
                    if board.get_figure(end_position[0], end_position[1]) is None:  # no figure can be at the position
                        return True
        elif abs(diff_vertical) == 2:   # 2 boxes away
            if abs(diff_horizontal) == 0:   # must be straight forward
                if board.get_turn() == WHITE and diff_vertical == -2:   # checks whether white is going forward
                    if start_position[0] == 1 and board.get_figure(end_position[0], end_position[1]) is None\
                            and board.get_figure(end_position[0] - 1, end_position[1]) is None:
                        # no figures can be in the way
                        return True
                elif board.get_turn() == BLACK and diff_vertical == 2:  # checks whether black is going forward
                    if start_position[0] == 6 and board.get_figure(end_position[0], end_position[1]) is None\
                            and board.get_figure(end_position[0] + 1, end_position[1]) is None:
                        # no figures can be in the way
                        return True
    return False


def generate_knight_moves(board, position):     # assumes that it is a knight
    moves = []
    if is_valid_knight_move(board, position, (position[0] - 2, position[1] + 1)):
        if not is_check(transition_function(board, position, (position[0] - 2, position[1] + 1))):
            moves.append([position, (position[0] - 2, position[1] + 1)])
    if is_valid_knight_move(board, position, (position[0] - 2, position[1] - 1)):
        if not is_check(transition_function(board, position, (position[0] - 2, position[1] - 1))):
            moves.append([position, (position[0] - 2, position[1] - 1)])
    if is_valid_knight_move(board, position, (position[0] + 2, position[1] + 1)):
        if not is_check(transition_function(board, position, (position[0] + 2, position[1] + 1))):
            moves.append([position, (position[0] + 2, position[1] + 1)])
    if is_valid_knight_move(board, position, (position[0] + 2, position[1] - 1)):
        if not is_check(transition_function(board, position, (position[0] + 2, position[1] - 1))):
            moves.append([position, (position[0] + 2, position[1] - 1)])
    if is_valid_knight_move(board, position, (position[0] - 1, position[1] + 2)):
        if not is_check(transition_function(board, position, (position[0] - 1, position[1] + 2))):
            moves.append([position, (position[0] - 1, position[1] + 2)])
    if is_valid_knight_move(board, position, (position[0] + 1, position[1] + 2)):
        if not is_check(transition_function(board, position, (position[0] + 1, position[1] + 2))):
            moves.append([position, (position[0] + 1, position[1] + 2)])
    if is_valid_knight_move(board, position, (position[0] - 1, position[1] - 2)):
        if not is_check(transition_function(board, position, (position[0] - 1, position[1] - 2))):
            moves.append([position, (position[0] - 1, position[1] - 2)])
    if is_valid_knight_move(board, position, (position[0] + 1, position[1] - 2)):
        if not is_check(transition_function(board, position, (position[0] + 1, position[1] - 2))):
            moves.append([position, (position[0] + 1, position[1] - 2)])
    return moves


def is_valid_knight_move(board, start_position, end_position):  # assumes that it is a knight
    if is_in_bounds(end_position):
        diff = abs(start_position[0] - end_position[0]) + abs(start_position[1] - end_position[1])
        if diff != 3:
            return False
        if board.get_figure(end_position[0], end_position[1]) is None:
            return True
        if board.get_turn() == WHITE:
            if board.get_figure(end_position[0], end_position[1]).get_color() == BLACK:
                return True
        else:
            if board.get_figure(end_position[0], end_position[1]).get_color() == WHITE:
                return True
    return False


def generate_rook_moves(board, position):
    moves = []
    for i in range(1, 8):
        if is_valid_rook_move(board, position, (position[0] + i, position[1])):
            if not is_check(transition_function(board, position, (position[0] + i, position[1]))):
                moves.append((position, (position[0] + i, position[1])))
        if is_valid_rook_move(board, position, (position[0] - i, position[1])):
            if not is_check(transition_function(board, position, (position[0] - i, position[1]))):
                moves.append((position, (position[0] - i, position[1])))
        if is_valid_rook_move(board, position, (position[0], position[1] + i)):
            if not is_check(transition_function(board, position, (position[0], position[1] + i))):
                moves.append((position, (position[0], position[1] + i)))
        if is_valid_rook_move(board, position, (position[0], position[1] - i)):
            if not is_check(transition_function(board, position, (position[0], position[1] - i))):
                moves.append((position, (position[0], position[1] - i)))
    return moves


def is_valid_rook_move(board, start_position, end_position):
    if is_in_bounds(end_position):
        go_y = start_position[0] - end_position[0]
        go_x = start_position[1] - end_position[1]
        if go_y != 0 and go_x != 0:
            return False
        if board.get_figure(end_position[0], end_position[1]) is not None:
            if board.get_figure(end_position[0], end_position[1]).get_color() == board.get_turn():
                return False
        for i in range(1, abs(go_x) + abs(go_y)):
            pos1 = 0
            pos2 = 0
            if go_y < 0:
                pos1 = end_position[0] - i
                pos2 = 0
            if go_y > 0:
                pos1 = end_position[0] + i
                pos2 = 0
            if go_x < 0:
                pos1 = 0
                pos2 = end_position[1] - i
            if go_x > 0:
                pos1 = 0
                pos2 = end_position[1] + i
            if board.get_figure(pos1, pos2) is not None:
                return False
        return True
    return False


def generate_bishop_moves(board, position):
    moves = []
    for i in range(1, 8):
        if is_valid_bishop_move(board, position, (position[0]+i, position[1]+i)):
            if not is_check(transition_function(board, position, (position[0]+i, position[1]+i))):
                moves.append((position, (position[0]+i, position[1]+i)))
        if is_valid_bishop_move(board, position, (position[0]+i, position[1]-i)):
            if not is_check(transition_function(board, position, (position[0]+i, position[1]-i))):
                moves.append((position, (position[0]+i, position[1]-i)))
        if is_valid_bishop_move(board, position, (position[0]-i, position[1]+i)):
            if not is_check(transition_function(board, position, (position[0]-i, position[1]+i))):
                moves.append((position, (position[0]-i, position[1]+i)))
        if is_valid_bishop_move(board, position, (position[0]-i, position[1]-i)):
            if not is_check(transition_function(board, position, (position[0]-i, position[1]-i))):
                moves.append((position, (position[0]-i, position[1]-i)))
    return moves


def is_valid_bishop_move(board, start_position, end_position):
    if is_in_bounds(end_position):
        go_y = start_position[0] - end_position[0] < 0
        go_x = start_position[1] - end_position[1] < 0
        if abs(start_position[0] - end_position[0]) != abs(start_position[1] - end_position[1]):
            return False
        for i in range(1, abs(start_position[0] - end_position[0])):
            if go_y:
                pos1 = end_position[0] - i
            else:
                pos1 = end_position[0] + i
            if go_x:
                pos2 = end_position[1] - i
            else:
                pos2 = end_position[1] + i
            if board.get_figure(pos1, pos2) is not None:
                return False
        if board.get_figure(end_position[0], end_position[1]) is not None:
            if board.get_figure(end_position[0], end_position[1]).get_color() == board.get_turn():
                return False
        return True
    return False


def generate_queen_moves(board, position):
    moves = []
    moves.extend(generate_bishop_moves(board, position))
    moves.extend(generate_rook_moves(board, position))
    return moves


def is_valid_queen_move(board, start_position, end_position):
    return is_valid_bishop_move(board, start_position, end_position) or \
           is_valid_rook_move(board, start_position, end_position)


def generate_king_moves(board, position):
    moves = []
    if is_valid_king_move(board, position, (position[0] + 1, position[1])):
        if not is_check(transition_function(board, position, (position[0] + 1, position[0]))):
            moves.append((position, (position[0] + 1, position[1])))
    if is_valid_king_move(board, position, (position[0] - 1, position[1])):
        if not is_check(transition_function(board, position, (position[0] - 1, position[0]))):
            moves.append((position, (position[0] - 1, position[1])))
    if is_valid_king_move(board, position, (position[0], position[1] + 1)):
        if not is_check(transition_function(board, position, (position[0], position[0] + 1))):
            moves.append((position, (position[0], position[1] + 1)))
    if is_valid_king_move(board, position, (position[0], position[1] - 1)):
        if not is_check(transition_function(board, position, (position[0], position[0] - 1))):
            moves.append((position, (position[0], position[1] - 1)))
    if is_valid_king_move(board, position, (position[0] + 1, position[1] + 1)):
        if not is_check(transition_function(board, position, (position[0] + 1, position[0] + 1))):
            moves.append((position, (position[0] + 1, position[1] + 1)))
    if is_valid_king_move(board, position, (position[0] - 1, position[1] - 1)):
        if not is_check(transition_function(board, position, (position[0] - 1, position[0] - 1))):
            moves.append((position, (position[0] - 1, position[1] - 1)))
    if is_valid_king_move(board, position, (position[0] + 1, position[1] - 1)):
        if not is_check(transition_function(board, position, (position[0] + 1, position[0] - 1))):
            moves.append((position, (position[0] + 1, position[1] - 1)))
    if is_valid_king_move(board, position, (position[0] - 1, position[1] + 1)):
        if not is_check(transition_function(board, position, (position[0] - 1, position[0] + 1))):
            moves.append((position, (position[0] - 1, position[1] + 1)))
    return moves


def is_valid_king_move(board, start_position, end_position):
    if is_in_bounds(end_position):
        go_y = start_position[0] - end_position[0]
        go_x = start_position[1] - end_position[1]
        if abs(go_y) > 1 or abs(go_x) > 1:
            return False
        if board.get_figure(end_position[0], end_position[1]) is not None:
            if board.get_figure(end_position[0], end_position[1]).get_color() == board.get_turn():
                return False
        return True
    return False


def generate_castle_moves(board):
    moves = []
    if board.get_turn() == WHITE:
        if board.get_figure(0, 1) is None and board.get_figure(0, 2) is None and board.get_figure(0, 3) is None:
            if board.white_can_castle() == 1 or board.white_can_castle() == 3:
                if is_valid_king_move(board, (0, 4), (0, 3)):
                    next_state = transition_function(board, (0, 4), (0, 3))
                    if not is_check(next_state) and is_valid_king_move(next_state, (0, 3), (0, 2)):
                        next_state.switch_turn()
                        if not is_check(transition_function(next_state, (0, 3), (0, 2))):
                            moves.append("Left_Castling")
        if board.get_figure(0, 5) is None and board.get_figure(0, 6) is None:
            if board.white_can_castle() == 2 or board.white_can_castle() == 3:
                if is_valid_king_move(board, (0, 4), (0, 5)):
                    next_state = transition_function(board, (0, 4), (0, 5))
                    if not is_check(next_state) and is_valid_king_move(next_state, (0, 5), (0, 6)):
                        next_state.switch_turn()
                        if not is_check(transition_function(next_state, (0, 5), (0, 6))):
                            moves.append("Right_Castling")
    else:
        if board.get_figure(7, 1) is None and board.get_figure(7, 2) is None and board.get_figure(7, 3) is None:
            if board.black_can_castle() == 1 or board.black_can_castle() == 3:
                if is_valid_king_move(board, (7, 4), (7, 3)):
                    next_state = transition_function(board, (7, 4), (7, 3))
                    if not is_check(next_state) and is_valid_king_move(next_state, (7, 3), (7, 2)):
                        next_state.switch_turn()
                        if not is_check(transition_function(next_state, (7, 3), (7, 2))):
                            moves.append("Left_Castling")
        if board.get_figure(7, 5) is None and board.get_figure(7, 6) is None:
            if board.black_can_castle() == 2 or board.black_can_castle() == 3:
                if is_valid_king_move(board, (7, 4), (7, 5)):
                    next_state = transition_function(board, (7, 4), (7, 5))
                    if not is_check(next_state) and is_valid_king_move(next_state, (7, 5), (7, 6)):
                        next_state.switch_turn()
                        if not is_check(transition_function(next_state, (7, 5), (7, 6))):
                            moves.append("Right_Castling")
    return moves


def is_check(board):
    return True
