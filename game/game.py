from .player import Player
from .field import Field
from .dice import Dice
import time

class Game():
    num_players = None
    player_names = None
    players = None
    next_player = None
    num_figures = None

    dice = None

    num_fields = None
    fields = None

    turns = None
    running = None
    winners = None

    def __init__(self, num_players=4, player_names=["A", "B", "C", "D"],
                        num_fields=40, num_figures=4):
        self.num_fields = num_fields
        self.fields = {}
        self._create_fields()

        self.num_players = num_players
        self.player_names = player_names
        self.players = {}
        self.num_figures = num_figures
        self._create_players()
        # init as -1 so we can call _next_player first round
        self.next_player = -1

        self.dice = Dice()

        self.turns = 0
        self.running = True
        self.winners = []

    def _create_players(self):
        print("Creating players")
        for i in range(self.num_players):
            p_field_index = i * (self.num_fields // self.num_players)
            p_home_field = self.fields[p_field_index]
            p_start_field = self.fields[p_field_index + 1]
            p_name = self.player_names[i]
            print("%s - hf %s sf %s" % (p_name, p_home_field, p_start_field))
            p = Player(p_name, p_home_field, p_start_field, self, num_figures=self.num_figures)
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

    def _pick_start_figure(self, player):
        sh = player.get_start_home()
        sh.print_figures()
        ###slot = input("Select slot: ")
        ###while not slot.isdigit() or int(slot) < 0 or int(slot) > sh.get_size():
        ###    print("Invalid input")
        ###    slot = input("Select slot: ")
        ###slot = int(slot)

        for i in range(sh.get_size()):
            if sh.figures[i] is not None:
                print("AUTOPICKED SLOT %s" % i)
                return i

        return slot

    def get_field(self, f_id):
        return self.fields[f_id]

    def turn(self):
        #time.sleep(1)
        self.turns += 1
        print("------------------- TURN %s -------------------" % self.turns)
        for p_name in self.players:
        #p_name = self._next_player() 
            player = self.players[p_name]
            print("----------- PLAYING player %s" % player)

            roll = self.dice.roll()

            if player.is_initial_round():
                num_rolls = 1
                while num_rolls < 3 and roll != 6:
                    roll = self.dice.roll()
                    num_rolls += 1

            # Move figure from start home if roll is 6 and start field is empty
            if roll == 6 and player.is_start_field_empty() and not player.get_start_home().is_empty():
                slot = self._pick_start_figure(player)
                figure = player.move_figure_from_home(slot)
                player.move_figure_to_field(figure, player.get_start_field())
            else:
                figure = player.get_playable_figure(roll, self.num_fields)
                print("Playable figure %s" % figure)
                if figure:
                    player.move_figure(figure, roll, self.num_fields)

            if player.get_target_home().is_full() and player.get_name() not in self.winners:
                self.winners.append(player.get_name())
                print("WON player %s" % player)
                input()

        if len(self.winners) == self.num_players:
            print("GAME ENDED")
            print(self.winners)
            self.running = False

    def main_loop(self):
        while self.running:
            self.turn()
