from src.model.shapes.shape import Shape


class Square1(Shape):
    def __init__(self, color):
        num_of_squares = 1
        num_of_rotations = 0
        can_flip = False
        normalized_coordinates = [(0, 0)]
        super().__init__(color, num_of_squares, num_of_rotations, can_flip, normalized_coordinates)
