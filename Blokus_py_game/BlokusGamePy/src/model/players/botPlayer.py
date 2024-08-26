from src.model.players.player import Player


class botPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.is_user = False

    def make_move(self, map_model):
        if not map_model.can_put_any_shape(map_model.get_current_player()):
            return
        # TODO document why this method is empty
        return