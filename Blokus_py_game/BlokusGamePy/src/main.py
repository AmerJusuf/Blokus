from src.model.map.game_map import Placement
from src.model.players.user import User
from src.model.shapes import *
from src.view.game_window.game_window import GameWindow


def initialize_all_shapes(color):
    s1 = Branch(color)
    s2 = Chair(color)
    s3 = LShape(color)
    s4 = Line2Shape(color)
    s5 = SmallL(color)
    s6 = Square1(color)
    s7 = TShape(color)
    s8 = Zigzag(color)
    s9 = Locker(color)
    s10 = Plus(color)
    s11 = Podium(color)
    s12 = LongPodium(color)
    s13 = Stair(color)
    s14 = LongStair(color)
    s15 = Line3Shape(color)
    s16 = Line4Shape(color)
    s17 = Line5Shape(color)
    s18 = MediumL(color)
    s19 = LargeL(color)
    s20 = SmallStair(color)
    s21 = Square4(color)
    return [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21]


def main():
    window_width = 1000
    window_height = 1000
    grid_size = 20
    grid_width = 35
    margin = 150
    red_shapes = initialize_all_shapes(Placement.RED)
    blue_shapes = initialize_all_shapes(Placement.BLUE)
    player1 = User(Placement.RED)
    player1.add_shapes(red_shapes)
    player2 = User(Placement.BLUE)
    player2.add_shapes(blue_shapes)
    players = [player1, player2]
    game_window = GameWindow(window_width, window_height, grid_size, grid_width, margin, players)
    game_window.game_loop()


if __name__ == "__main__":
    main()

