from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, color):
        self._color = color
        self._shapes = []
        self._is_game_over = False

    def get_color(self):
        return self._color

    def add_shapes(self, shapes):
        self._shapes.extend(shapes)

    def has_placed_any(self):
        return any([shape.get_placed() for shape in self._shapes])

    def has_unplaced_shape(self):
        return any([not shape.get_placed() for shape in self._shapes])

    def get_shapes(self):
        return self._shapes

    def get_is_game_over(self):
        return self._is_game_over

    def set_is_game_over(self, is_game_over):
        self._is_game_over = is_game_over