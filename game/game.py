from .player import Player
from .field import Field
from .dice import Dice

class Game():
    num_players = None
    player_name = None
    players = None

    dice = None

    num_fields = None
    fields = None

    def __init__(self, num_players=4, player_names=["A", "B", "C", "D"],
                        num_fields=40):
        self.num_players = num_players
        self.player_names = player_names
        self.players = []
        self._create_players()

        self.dice = Dice()

        self.num_fields = num_fields
        self.fields = {}
        self._create_fields()

    def _create_players(self):
        for i in range(self.num_players):
            p_name = self.player_names[i]
            p = Player(p_name)
            self.players.append(p)

    def _create_fields(self):
        for i in range(self.num_fields):
            f = Field(i)
            self.fields[i] = f
