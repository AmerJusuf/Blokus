import pygame


class GameController:
    def __init__(self, map_model, map_view):
        self.__map_model = map_model
        self.__map_view = map_view
        self.__current_player = None

    def set_current_player(self, player):
        self.__current_player = player
        self.__map_view.set_current_player(player)

    def handle_turn(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.is_on_grid(mouse_x, mouse_y):
                    grid_x = (mouse_x - self.__map_view.get_margin()) // self.__map_view.get_grid_height()
                    grid_y = (mouse_y - self.__map_view.get_margin()) // self.__map_view.get_grid_width()
                    self.__map_model.grid_clicked(grid_x, grid_y, self.__current_player)
                else:
                    mouse_pos = event.pos
                    self.__map_model.check_button_clicked(mouse_pos, self.__map_view)
                    break

    def is_on_grid(self, x, y):
        return (self.__map_view.get_margin() <= x <= self.__map_view.get_margin() + self.__map_view.get_grid_area() and
                self.__map_view.get_margin() <= y <= self.__map_view.get_margin() + self.__map_view.get_grid_area())

    def handle_place_button_clicked(self, map_view, map_model):
        finished_turn = map_view.current_player.place(map_model)
        if finished_turn:
            map_view.next_player_turn()