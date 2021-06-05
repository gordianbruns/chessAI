from ..common.constants import *


class Board:

    def __init__(self):
        self.turn = WHITE
        self.white_figures = {}
        self.black_figures = {}

    def get_white_figures(self):
        return self.white_figures

    def get_black_figures(self):
        return self.black_figures

    def add_figure(self, figure):
        if figure.get_color() == WHITE:
            self.white_figures[figure.get_position()] = figure
        else:
            self.black_figures[figure.get_position()] = figure

    def get_figure(self, x, y):
        key = (x, y)
        if key in self.white_figures:
            return self.white_figures[(x, y)]
        elif key in self.black_figures:
            return self.black_figures[(x, y)]
        else:
            return None

    def get_turn(self):
        return self.turn

    def move_figure(self, start_position, end_position):
        if end_position in self.white_figures:
            del self.white_figures[end_position]
        if end_position in self.black_figures:
            del self.black_figures[end_position]
        if start_position in self.white_figures:
            figure = self.white_figures[start_position]
            figure.set_position(end_position[0], end_position[1])
            self.white_figures[end_position] = figure
            del self.white_figures[start_position]
        else:
            figure = self.black_figures[start_position]
            figure.set_position(end_position[0], end_position[1])
            self.black_figures[end_position] = figure
            del self.black_figures[start_position]

    def switch_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    # mainly for testing
    def clear_board(self):
        self.white_figures.clear()
        self.black_figures.clear()
