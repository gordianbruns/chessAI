from chessAI.game.helpers import *

import chess


ties = 0
white = 0
black = 0


def run():
    board = chess.Board()
    for i in range(50):
        play_game(Node(board), "function2", "function1")
    print("Ties:", ties)
    print("White:", white)
    print("Black:", black)


def play_game(node: Node, function1: str, function2: str) -> None:
    print(node.get_board())
    print()
    outcome = node.get_board().outcome()
    print(outcome)
    if outcome is not None:
        if outcome.winner is None:
            print("Tie!")
            global ties
            ties += 1
            return
        if outcome.winner:
            print("White won!")
            global white
            white += 1
        else:
            print("Black won!")
            global black
            black += 1
        return
    tree, leaf_nodes = create_state_tree(node.get_board())
    if tree.get_board().turn == chess.WHITE:
        if function1 == "random":
            for node in leaf_nodes:
                node.set_utility(random_strategy())
        elif function1 == "function1":
            for node in leaf_nodes:
                node.set_utility(evaluation_function1(tree, node))
        elif function1 == "function2":
            for node in leaf_nodes:
                node.set_utility(evaluation_function2(tree, node))
    else:
        if function2 == "random":
            for node in leaf_nodes:
                node.set_utility(random_strategy())
        elif function2 == "function1":
            for node in leaf_nodes:
                node.set_utility(evaluation_function1(tree, node))
        elif function2 == "function2":
            for node in leaf_nodes:
                node.set_utility(evaluation_function2(tree, node))
    next_node = minimax(tree)
    play_game(next_node, function1, function2)


if __name__ == '__main__':
    run()
