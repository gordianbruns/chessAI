from ..common.constants import *
from .figures import *


class Board:

    def __init__(self):
        self.turn = WHITE
        self.white_figures = {}
        self.black_figures = {}
        self._castle_white = [0, 0, 0]  # 0: rook in row 0, 1: rook in row 7, 2: king
        self._castle_black = [0, 0, 0]  # 0: rook in row 0, 1: rook in row 7, 2: king
        self.white_king_pos = None
        self.black_king_pos = None

    def get_white_king_pos(self):
        return self.white_king_pos

    def get_black_king_pos(self):
        return self.black_king_pos

    def get_white_figures(self):
        return self.white_figures

    def get_black_figures(self):
        return self.black_figures

    def white_can_castle(self):
        counter = 0     # represents with how many rooks white can castle
        if self._castle_white[0] == 0 and self._castle_white[2] == 0:
            counter = 1
        if self._castle_white[1] == 0 and self._castle_white[2] == 0:
            counter += 2
        return counter

    def black_can_castle(self):
        counter = 0     # represents with how many rooks black can castle
        if self._castle_black[0] == 0 and self._castle_black[2] == 0:
            counter = 1
        if self._castle_black[1] == 0 and self._castle_black[2] == 0:
            counter += 2
        return counter

    def add_figure(self, figure):
        if figure.get_color() == WHITE:
            if type(figure) == King:
                self.white_king_pos = figure.get_position()
            self.white_figures[figure.get_position()] = figure
        else:
            if type(figure) == King:
                self.black_king_pos = figure.get_position()
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
        figure = self.get_figure(start_position[0], start_position[1])
        if figure.get_color() == WHITE:
            if type(figure) == Rook:
                if start_position == (0, 0):
                    self._castle_white[0] += 1
                if start_position == (0, 7):
                    self._castle_white[1] += 1
            if type(figure) == King:
                self.white_king_pos = end_position
                if start_position == (0, 4):
                    self._castle_white[2] += 1
        else:
            if type(figure) == Rook:
                if start_position == (7, 0):
                    self._castle_black[0] += 1
                if start_position == (7, 7):
                    self._castle_black[1] += 1
            if type(figure) == King:
                self.black_king_pos = end_position
                if start_position == (7, 4):
                    self._castle_black[2] += 1
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
