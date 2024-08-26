from src.model.map.game_map import Placement
from src.model.players.player import Player
from src.model.shapes.shape import normalize_coordinates


def shape_equals_variety_of_shape(shape, selected_coordinates):
    normalized__selected_coordinates = normalize_coordinates(selected_coordinates)
    for variation in shape.get_all_variations():
        is_matching = True
        for coordinate in variation:
            if coordinate not in normalized__selected_coordinates:
                is_matching = False
                break
        if is_matching:
            return True
    return False


class User(Player):
    def __init__(self, color):
        super().__init__(color)
        self.is_user = True

    def place(self, map_model):
        shape = self.has_shape(map_model)
        if shape:
            for row in range(0, 20):
                for col in range(0, 20):
                    if map_model.get_map()[row][col] == Placement.SELECTED:
                        map_model.get_map()[row][col] = self._color
            map_model.clear_selected_squares()
            shape.set_placed(True)
            return True
        else:
            map_model.clear_selected_squares()
            return False

    # returns the shape if the selected squares matches to one of the shapes the user has
    def has_shape(self, map_model):
        selected_coordinates = map_model.get_selected_squares()
        normalized__selected_coordinates = normalize_coordinates(selected_coordinates)
        for shape in self._shapes:
            if not shape.get_placed():
                if shape.get_num_of_squares() == len(normalized__selected_coordinates):
                    if shape_equals_variety_of_shape(shape, normalized__selected_coordinates):
                        return shape
        return None
