class Node:
    def __init__(self, board):
        self.state = board
        self.children = []
        self.parent = None
        self.move = None
        self.depth = 0
        self.utility_estimate = 0.0

    def get_board(self):
        return self.state

    def get_children(self):
        return self.children

    def get_depth(self):
        return self.depth

    def set_depth(self, depth):
        self.depth = depth

    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_move(self):
        return self.move

    def set_move(self, move):
        self.move = move

    def get_utility(self):
        return self.utility_estimate

    def set_utility(self, utility):
        self.utility_estimate = utility
