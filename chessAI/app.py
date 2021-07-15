from chessAI.game.helpers import *

import chess


def run():
    board = chess.Board()
    play_game(Node(board), "killer", "killer")


def play_game(node, function1, function2):
    print(node.get_board())
    print()
    if node.get_board().is_stalemate():
        print("Tie!")
        return
    if node.get_board().is_checkmate():
        if node.get_board().turn == chess.WHITE:
            print("Black won!")
        else:
            print("White won!")
        return
    tree, leaf_nodes = create_state_tree(node.get_board())
    if tree.get_board().turn == chess.WHITE:
        if function1 == "random":
            for node in leaf_nodes:
                node.set_utility(random_strategy())
        if function1 == "killer":
            for node in leaf_nodes:
                node.set_utility(killer_strategy(tree, node))
    else:
        if function2 == "random":
            for node in leaf_nodes:
                node.set_utility(random_strategy())
        if function2 == "killer":
            for node in leaf_nodes:
                node.set_utility(killer_strategy(tree, node))
    next_node = minimax(tree)
    play_game(next_node, function1, function2)


if __name__ == '__main__':
    run()
