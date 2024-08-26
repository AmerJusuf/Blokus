import copy
from enum import Enum, auto

from src.model.shapes.shape import is_edge_coordinate


class Placement(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    ORANGE = auto()
    NONE = auto()
    SELECTED = auto()


class GameMap:
    COLOR_MAP = {Placement.NONE: 0, Placement.RED: 1, Placement.BLUE: 2, Placement.GREEN: 3, Placement.ORANGE: 4}

    def __init__(self):
        self.__map = [[Placement.NONE for _ in range(20)] for _ in range(20)]
        self.__selected_squares = []
        self.controller = None

    def get_map(self):
        return self.__map

    def get_selected_squares(self):
        return self.__selected_squares

    def color_to_int(self, color):
        return self.COLOR_MAP[color]

    def select_square(self, row, col):
        self.__selected_squares.append((row, col))

    def get_placement(self, x, y):
        return self.__map[x][y]

    def set_controller(self, controller):
        self.controller = controller

    def can_click(self, row, col, player):
        if self.__selected_squares.__contains__((row, col)) or self.__map[row][col] != Placement.NONE:
            return False
        if len(self.__selected_squares) != 0 and not self.is_next_to(row, col, Placement.SELECTED):
            return False
        if self.is_next_to(row, col, player.get_color()):
            return False
        if player.has_placed_any() and len(self.__selected_squares) == 0 and not self.has_apex(row, col,
                                                                                               player.get_color()):
            return False
        if not player.has_placed_any() and len(self.__selected_squares) == 0 and not self.is_in_corner(row, col):
            return False
        return True

    def is_in_corner(self, row, col):
        return (row, col) == (0, 0) or (row, col) == (0, 19) or (row, col) == (19, 0) or (row, col) == (19, 19)

    def grid_clicked(self, col, row, player):
        if self.can_click(row, col, player):
            self.__selected_squares.append((row, col))
            self.__map[row][col] = Placement.SELECTED
        # print("row col:" + str(row) + " " + str(col))

    def check_button_clicked(self, pos, map_view):
        if map_view.place_button.collidepoint(pos):
            self.controller.handle_place_button_clicked(map_view, self)

    def clear_selected_squares(self):
        for row in range(0, 20):
            for col in range(0, 20):
                if self.__map[row][col] == Placement.SELECTED:
                    self.__map[row][col] = Placement.NONE
        self.__selected_squares = []


    # next or upper/below
    def is_next_to(self, row, col, placement, _map=None):
        if _map is None:
            _map = self.__map
        if row > 0 and _map[row - 1][col] == placement:
            return True
        if row < 19 and _map[row + 1][col] == placement:
            return True
        if col > 0 and _map[row][col - 1] == placement:
            return True
        if col < 19 and _map[row][col + 1] == placement:
            return True
        return False

    def has_apex(self, row, col, placement):
        if row > 0 and col > 0 and self.__map[row - 1][col - 1] == placement:
            return True
        if row < 19 and col > 0 and self.__map[row + 1][col - 1] == placement:
            return True
        if row > 0 and col < 19 and self.__map[row - 1][col + 1] == placement:
            return True
        if row < 19 and col < 19 and self.__map[row + 1][col + 1] == placement:
            return True
        return False

    def get_free_apexes(self, player):
        free_apexes = []
        for row in range(0, 20):
            for col in range(0, 20):
                if self.__map[row][col] == Placement.NONE and self.has_apex(row, col, player.get_color()):
                    free_apexes.append((row, col))
        return free_apexes

    def can_put_any_shape(self, player):
        if not player.has_unplaced_shape():
            player.set_is_game_over(True)
            return False
        if not player.has_placed_any():
            return True
        for shape in player.get_shapes():
            coordinates = self.get_free_apexes(player)
            for row, col in coordinates:
                if self.can_put_shape_at(shape, row, col, player):
                    print("CAN PUT SHAPE: ")
                    print("player: " + str(player.get_color()))
                    for x, y in shape.get_normalized_coordinates():
                        print(x, y)
                    return True
        print("CANNOT PUT SHAPE")
        player.set_is_game_over(True)
        return False

    def can_put_shape_at(self, shape, row, col, player):
        for current_shape in shape.get_all_variations():
            current_apexes = self.get_apexes_of_shape(current_shape)
            for x, y in current_apexes:
                print("current_shape", current_shape)
                squares_to_select = []

                for n_x, n_y in current_shape:
                    print("x : " + str(row+ n_x - x))
                    print("y : " + str(col + n_y - y))
                    squares_to_select.append((row + n_x - x, col + n_y - y))
                if self.could_place_shape(squares_to_select, player):
                    return True
        return False

    def could_place_shape(self, selected_coordinates, player):
        tmp_map = copy.deepcopy(self.__map)
        for row, col in selected_coordinates:
            if row >= 20 or row < 0 or col >=20 or col < 0 or tmp_map[row][col] != Placement.NONE:
                return False
            tmp_map[row][col] = Placement.SELECTED
        for row in range(0, 20):
            for col in range(0, 20):
                if tmp_map[row][col] == Placement.SELECTED:
                    if not self.is_next_to(row, col, Placement.SELECTED, tmp_map):
                        return False
                    if self.is_next_to(row, col, player.get_color(), tmp_map):
                        return False
        return True

    def get_apexes_of_shape(self, coordinates):
        apexes = []
        for x, y in coordinates:
            if is_edge_coordinate(coordinates,x, y):
                apexes.append((x, y))
        return apexes

