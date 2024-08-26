from enum import Enum, auto


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
        print("row, col: " + str(row) + " " + str(col))
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

    def is_next_to(self, row, col, placement):
        if row > 0 and self.__map[row - 1][col] == placement:
            return True
        if row < 19 and self.__map[row + 1][col] == placement:
            return True
        if col > 0 and self.__map[row][col - 1] == placement:
            return True
        if col < 19 and self.__map[row][col + 1] == placement:
            return True
        return False

    def has_apex(self, row, col, placement):
        if row > 0 and col > 0 and self.__map[row - 1][col - 1] == placement:
            print("ok1")
            return True
        if row < 19 and col > 0 and self.__map[row + 1][col - 1] == placement:
            print("ok2")
            return True
        if row > 0 and col < 19 and self.__map[row - 1][col + 1] == placement:
            print("ok3")
            return True
        if row < 19 and col < 19 and self.__map[row + 1][col + 1] == placement:
            print("ok4")
            return True
        print("ok")
        return False
