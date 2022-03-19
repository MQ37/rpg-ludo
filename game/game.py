from .player import Player
from .field import Field
from .dice import Dice

class Game():
    num_players = None
    player_names = None
    players = None
    next_player = None

    dice = None

    num_fields = None
    fields = None

    turns = None
    running = None

    def __init__(self, num_players=4, player_names=["A", "B", "C", "D"],
                        num_fields=40):
        self.num_fields = num_fields
        self.fields = {}
        self._create_fields()

        self.num_players = num_players
        self.player_names = player_names
        self.players = {}
        self._create_players()
        # init as -1 so we can call _next_player first round
        self.next_player = -1

        self.dice = Dice()

        self.turns = 0
        self.running = True

    def _create_players(self):
        for i in range(self.num_players):
            p_field_index = i * (self.num_fields // self.num_players)
            p_home_field = self.fields[p_field_index]
            p_start_field = self.fields[p_field_index + 1]
            p_name = self.player_names[i]
            p = Player(p_name, p_home_field, p_start_field)
            self.players[p_name] = p

    def _create_fields(self):
        for i in range(self.num_fields):
            f = Field(i)
            self.fields[i] = f

    def _next_player(self):
        if self.next_player < self.num_players - 1:
            self.next_player += 1
        else:
            self.next_player = 0

        return list(self.players.keys())[self.next_player]

    def turn(self):
        self.turns += 1
        p_name = self._next_player() 
        player = self.players[p_name]
        print("TURN %s" % self.turns)
        print("PLAYING player %s" % player)

        roll = 6#self.dice.roll()
        print("Dice roll - %s" % roll)
        
        # Move figure from start home if roll is 6 and start field is empty
        if roll == 6 and player.is_start_field_empty():
            player.print_start_home_figures()
            input()

    def main_loop(self):
        while self.running:
            self.turn()
