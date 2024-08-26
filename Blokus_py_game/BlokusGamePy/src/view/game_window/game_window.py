import pygame
import sys

from src.controller.game_controller import GameController
from src.model.map.game_map import GameMap, Placement


class GameWindow:
    def __init__(self, window_width, window_height, grid_size, grid_width, margin, players):
        pygame.init()
        self.__window_width = window_width
        self.__window_height = window_height
        self.__grid_size = grid_size
        self.__grid_width = grid_width
        self.__grid_height = grid_width
        self.__margin = margin

        self.__grid_area = self.__grid_size * self.__grid_width

        self.screen = pygame.display.set_mode((self.__window_width, self.__window_height))
        pygame.display.set_caption("Blokus Mankus")

        self.clock = pygame.time.Clock()

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.orange = (255, 165, 0)
        self.grid_color = (128, 128, 128)  # grey
        self.background_color = (173, 216, 230)  # light blue
        self.selected_color = (255, 255, 0)  # yellow

        self.button_width = 100
        self.button_height = 50
        self.place_button_x = 850
        self.place_button_y = 900
        self.place_button = pygame.Rect(self.place_button_x, self.place_button_y, self.button_width, self.button_height)
        self.place_button_color = self.black

        self.players = players
        self.current_player = players[0]
        self.map_model = GameMap()
        self.game_controller = GameController(self.map_model, self)
        self.map_model.set_controller(self.game_controller)

    def enum_to_color(self, placement):
        if placement == Placement.RED:
            return self.red
        elif placement == Placement.BLUE:
            return self.blue
        elif placement == Placement.GREEN:
            return self.green
        elif placement == Placement.ORANGE:
            return self.orange
        elif placement == Placement.SELECTED:
            return self.selected_color
        else:
            return self.black

    def draw_grid(self):
        pygame.draw.rect(self.screen, self.grid_color,
                         (self.__margin, self.__margin, self.__grid_area, self.__grid_area))

        self.draw_lines()

    def draw_map(self):
        for row in range(self.__grid_size):
            for col in range(self.__grid_size):
                placement = self.map_model.get_placement(row, col)

                if placement != Placement.NONE:
                    color = self.enum_to_color(placement)

                    cell_x = self.__margin + (col * self.__grid_width)
                    cell_y = self.__margin + (row * self.__grid_height)

                    pygame.draw.rect(self.screen, color, (cell_x, cell_y, self.__grid_width, self.__grid_height))
        self.draw_lines()

    def draw_lines(self):
        for x in range(0, self.__grid_area, self.__grid_width):
            pygame.draw.line(self.screen, self.white, (self.__margin + x, self.__margin),
                             (self.__margin + x, self.__grid_area + self.__margin))
        for y in range(0, self.__grid_area, self.__grid_height):
            pygame.draw.line(self.screen, self.white, (self.__margin, self.__margin + y),
                             (self.__grid_area + self.__margin, self.__margin + y))

    def draw_buttons(self):
        pygame.draw.rect(self.screen, self.place_button_color, self.place_button)

    def start_game(self, players):
        self.players = players
        self.current_player = players[0]
        self.game_loop()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(self.background_color)
            self.draw_grid()
            self.draw_map()
            self.draw_buttons()
            pygame.display.flip()
            self.clock.tick(60)
            self.game_controller.set_current_player(self.current_player)

            if self.current_player.is_user:
                self.game_controller.handle_turn()
            else:
                self.current_player.make_move(self.map_model)



    def repaint(self):
        self.screen.fill(self.background_color)
        self.draw_grid()
        self.draw_map()
        pygame.display.flip()
        self.clock.tick(60)
        self.game_controller.set_current_player(self.current_player)

    def set_current_player(self, player):
        self.current_player = player

    def get_grid_width(self):
        return self.__grid_width

    def get_grid_height(self):
        return self.__grid_height

    def get_margin(self):
        return self.__margin

    def get_grid_area(self):
        return self.__grid_area

    def next_player_turn(self):
        idx = (self.players.index(self.current_player) + 1) % len(self.players)
        self.current_player = self.players[idx]
        #print("player idx: " + str(idx))
