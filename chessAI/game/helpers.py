from chessAI.game.node import *

import chess
import copy
import random
import math


def transition_function(board, move):
    copy_board = copy.deepcopy(board)
    copy_board.push(move)
    return copy_board


def create_state_tree(board):
    leaf_nodes = []
    current_state_node = Node(board)
    moves = board.legal_moves
    for move in moves:
        child = transition_function(board, move)
        child_node = Node(child)
        current_state_node.add_child(child_node)
        child_node.set_depth(1)
        child_node.set_parent(current_state_node)
        child_node.set_move(move)
        leaf_nodes.append(child_node)
    return current_state_node, leaf_nodes


def random_strategy():
    return random.uniform(-5, 5)


def ending(current_node, node):
    outcome = node.get_board().outcome()
    if outcome is None:
        return 0
    if outcome.winner == current_node.get_board().turn:
        return 9999
    else:
        return -9999


def material(current_node, node, weight):
    board = node.get_board()
    white_pawns = len(board.pieces(chess.PAWN, chess.WHITE))
    black_pawns = len(board.pieces(chess.PAWN, chess.BLACK))
    white_knights = len(board.pieces(chess.KNIGHT, chess.WHITE))
    black_knights = len(board.pieces(chess.KNIGHT, chess.BLACK))
    white_bishops = len(board.pieces(chess.BISHOP, chess.WHITE))
    black_bishops = len(board.pieces(chess.BISHOP, chess.BLACK))
    white_rooks = len(board.pieces(chess.ROOK, chess.WHITE))
    black_rooks = len(board.pieces(chess.ROOK, chess.BLACK))
    white_queens = len(board.pieces(chess.QUEEN, chess.WHITE))
    black_queens = len(board.pieces(chess.QUEEN, chess.BLACK))
    material_num = (9 * (white_queens - black_queens)
                    + 5 * (white_rooks - black_rooks)
                    + 3 * (white_bishops - black_bishops)
                    + 3 * (white_knights - black_knights)
                    + (white_pawns - black_pawns)) * weight
    if current_node.get_board().turn == chess.WHITE:
        return material_num
    return -material_num


def evaluation_function1(current_node, node):
    evaluation = material(current_node, node, 1) + ending(current_node, node) + random.uniform(0, 1)
    return evaluation


def choose_action(node):
    maximum = None
    if node.get_depth() == 0:
        maximum = Node(node.get_board())
        maximum.set_utility(-math.inf)
        for child in node.get_children():
            if child.get_utility() > maximum.get_utility():
                maximum = child
    return maximum


def minimax(node):
    for child in node.get_children():
        minimax(child)
    action = choose_action(node)
    return action
