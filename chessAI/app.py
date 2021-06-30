from chessAI.game.helpers import *
from chessAI.game.board import *


def run():
    board = Board()
    board.initialize()
    play_game(Node(board), "random", "random")


def play_game(node, function1, function2):
    print(node.get_board().get_turn())
    node.get_board().print()
    print()
    if node.get_board().is_terminal():
        print(node.get_board().get_turn(), "won!")
        return
    tree, leaf_nodes = create_state_tree(node.get_board())
    if tree.get_board().get_turn() == WHITE:
        if function1 == "random":
            for node in leaf_nodes:
                node.set_utility(random_strategy())
    else:
        if function2 == "random":
            for node in leaf_nodes:
                node.set_utility(random_strategy())
    next_node = minimax(tree)
    play_game(next_node, function1, function2)
