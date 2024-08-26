from abc import ABC, abstractmethod


def normalize_coordinates(coordinates):
    min_x = min([x for x, y in coordinates])
    min_y = min([y for x, y in coordinates])
    return [(x - min_x, y - min_y) for x, y in coordinates]


def mirror(coordinates):
    mirrored_shape = [(-x, y) for x, y in coordinates]
    return normalize_coordinates(mirrored_shape)


class Shape(ABC):
    def __init__(self, color, num_of_squares, num_of_rotations, can_flip, normalized_coordinates):
        self.__color = color
        self.__placed = False
        self.__placed_coordinates = None
        self.__num_of_squares = num_of_squares
        self.__num_of_rotations = num_of_rotations
        self.__can_flip = can_flip
        self.__normalized_coordinates = normalized_coordinates

    def set_placed(self, placed):
        self.__placed = placed

    def get_color(self):
        return self.__color

    def get_placed(self):
        return self.__placed

    def get_placed_coordinates(self):
        return self.__placed_coordinates

    def get_num_of_squares(self):
        return self.__num_of_squares

    def get_normalized_coordinates(self):
        return self.__normalized_coordinates

    def get_num_of_rotations(self):
        return self.__num_of_rotations

    # Returns the coordinates of the shape after rotating 90 degrees
    # Does not change the shape itself
    def rotate_90(self, coordinates=None):
        if coordinates is None:
            coordinates = self.get_normalized_coordinates()
        rotated_shape = [(y, -x) for x, y in coordinates]
        return normalize_coordinates(rotated_shape)

    def can_flip(self):
        return self.__can_flip

    def get_all_variations(self):
        current_variation = self.get_normalized_coordinates()
        variations = [current_variation]
        for _ in range(self.get_num_of_rotations()):
            variations.append(self.rotate_90(current_variation))
            current_variation = variations[-1]
        if self.can_flip():
            for variation in variations.copy():
                variations.append(mirror(variation))
        return variations
