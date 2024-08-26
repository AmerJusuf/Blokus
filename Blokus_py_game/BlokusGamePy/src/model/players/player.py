from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, color):
        self._color = color
        self._shapes = []

    def get_color(self):
        return self._color

    def add_shapes(self, shapes):
        self._shapes.extend(shapes)

    def has_placed_any(self):
        return any([shape.get_placed() for shape in self._shapes])