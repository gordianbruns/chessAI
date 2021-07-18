from chessAI.game.helpers import *

import chess


def run():
    board = chess.Board()
    board.is_check()
    play_game(Node(board), "finisher", "finisher")


def play_game(node, function1, function2):
    print(node.get_board())
    print()
    outcome = node.get_board().outcome()
    print(outcome)
    if outcome is not None:
        if outcome.winner is None:
            print("Tie!")
            return
        if outcome.winner:
            print("White won!")
        else:
            print("Black won!")
        return
    tree, leaf_nodes = create_state_tree(node.get_board())
    if tree.get_board().turn == chess.WHITE:
        if function1 == "random":
            for node in leaf_nodes:
                node.set_utility(random_strategy())
        elif function1 == "killer":
            for node in leaf_nodes:
                node.set_utility(killer_strategy(tree, node))
        elif function1 == "finisher":
            for node in leaf_nodes:
                node.set_utility(killer_and_finisher(tree, node))
    else:
        if function2 == "random":
            for node in leaf_nodes:
                node.set_utility(random_strategy())
        elif function2 == "killer":
            for node in leaf_nodes:
                node.set_utility(killer_strategy(tree, node))
        elif function2 == "finisher":
            for node in leaf_nodes:
                node.set_utility(killer_and_finisher(tree, node))
    next_node = minimax(tree)
    play_game(next_node, function1, function2)


if __name__ == '__main__':
    run()
