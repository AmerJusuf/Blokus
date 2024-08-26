from src.model.shapes.shape import Shape


class TShape(Shape):
    def __init__(self, color):
        num_of_squares = 5
        num_of_rotations = 3
        can_flip = False
        normalized_coordinates = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)]
        super().__init__(color, num_of_squares, num_of_rotations, can_flip, normalized_coordinates)
