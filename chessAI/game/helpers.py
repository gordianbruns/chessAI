from chessAI.game.node import *

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
        leaf_nodes.append(child_node)
    return current_state_node, leaf_nodes


def random_strategy():
    return random.uniform(-5, 5)


def calculate_utility(board_node):
    maximum = None
    if board_node.get_depth() == 0:
        maximum = Node(board_node.get_board())
        maximum.set_utility(-math.inf)
        for child in board_node.get_children():
            if child.get_utility() > maximum.get_utility():
                maximum = child
        board_node.set_utility(maximum.get_utility())
    return maximum


def minimax(node):
    if node is None:
        return
    for child in node.get_children():
        minimax(child)
    action = calculate_utility(node)
    if action:
        return action
