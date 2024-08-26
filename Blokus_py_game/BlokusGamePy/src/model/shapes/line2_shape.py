from src.model.shapes.shape import Shape


class Line2Shape(Shape):
    def __init__(self, color):
        num_of_squares = 2
        num_of_rotations = 1
        can_flip = False
        normalized_coordinates = [(0, 0), (0, 1)]
        super().__init__(color, num_of_squares, num_of_rotations, can_flip, normalized_coordinates)