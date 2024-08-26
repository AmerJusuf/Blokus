from src.model.players.player import Player


class botPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.is_user = False

    def make_move(self, game_map):
        # TODO document why this method is empty
        pass