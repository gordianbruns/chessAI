import chess


class Node:
    def __init__(self, board: chess.Board):
        self.state = board
        self.children = []
        self.parent = None
        self.move = None
        self.depth = 0
        self.utility_estimate = 0.0

    def get_board(self) -> chess.Board:
        return self.state

    def get_children(self) -> list:
        return self.children

    def get_depth(self) -> int:
        return self.depth

    def set_depth(self, depth: 'int > 0'):
        self.depth = depth

    def add_child(self, node: 'Node'):
        self.children.append(node)

    def get_parent(self) -> 'Node':
        return self.parent

    def set_parent(self, parent: 'Node'):
        self.parent = parent

    def get_move(self) -> chess.Move:
        return self.move

    def set_move(self, move: chess.Move):
        self.move = move

    def get_utility(self) -> float:
        return self.utility_estimate

    def set_utility(self, utility: float):
        self.utility_estimate = utility
