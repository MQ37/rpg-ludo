from .figure import Figure
from .home import Home

class Player():
    name = None
    num_figures = None
    # Figures on field - playable
    figures = None
    # Starting home figures container
    start_home = None
    # Target home figures container
    target_home = None

    # Field where figures can enter target home
    home_field = None
    # Field where figures start from start home
    start_field = None

    game = None

    def __init__(self, name, home_field, start_field, game, num_figures=4):
        self.name = name

        self.home_field = home_field
        self.start_field = start_field

        self.num_figures = num_figures
        self.figures = {}
        self.start_home = Home(self, num_figures)
        self.target_home = Home(self, num_figures)
        self._create_figures()

        self.game = game

    def __str__(self):
        return "Player %s" % self.name

    def __repr__(self):
        return str(self)

    # Creates all player figures and moves them to start home
    def _create_figures(self):
        for i in range(self.num_figures):
            f = Figure(self, i)
            self.start_home.add_figure(f, i)

    def get_home_field(self):
        return self.home_field

    def get_start_field(self):
        return self.start_field

    def get_start_home(self):
        return self.start_home

    def get_target_home(self):
        return self.target_home

    def get_figure(self, f_id):
        return self.figures[f_id]

    def get_name(self):
        return self.name

    # If all player figures are in start home
    def is_initial_round(self):
        return self.start_home.is_full()

    def is_start_field_empty(self):
        return self.start_field.is_empty()

    # Move figure from start home
    def move_figure_from_home(self, slot):
        figure = self.start_home.remove_figure(slot)
        self.figures[figure.get_id()] = figure
        print("%s - removed figure %s from starting home" % (self, figure))
        return figure

    # Move figure to target home
    def move_figure_to_home(self, figure, slot):
        figure.get_field().remove_figure()
        figure.remove_field()
        self.target_home.add_figure(figure, slot)
        del self.figures[figure.get_id()]
        print("%s - moved figure %s to target home at slot %s" % (self, figure, slot))
        self.target_home.print_figures()

    def move_figure_to_field(self, figure, field):
        if figure.get_field():
            figure.get_field().remove_figure()
        if field.is_empty():
            print("%s - moving figure %s from field %s to field %s" % (self, figure, figure.get_field(), field))
            figure.set_field(field, True)
        else:
            print("%s - field %s not empty - cannot move figure %s there" % (self, field, figure))
            return False
        return True

    def move_figure(self, figure, moves, num_fields):
        field = figure.get_field()
        field_pos = field.get_id()

        can_enter, slot = self.can_enter_home(figure, moves, num_fields, ret_slot=True)
        if can_enter:
            self.move_figure_to_home(figure, slot)
        else:
            pos = field_pos + moves
            if pos > num_fields - 1:
                field = self.game.get_field(pos - num_fields)
            else:
                field = self.game.get_field(pos)

            self.move_figure_to_field(figure, field)

    # Returns number of moves to home_field (home enterance)
    def _get_num_moves_to_home(self, figure, num_fields):
        field = figure.get_field()
        field_pos = field.get_id()
        home_field_pos = self.home_field.get_id()

        num_moves = 0
        #if field_pos < num_fields:
        if field_pos > home_field_pos:
            num_moves += num_fields - field_pos

        if field_pos < home_field_pos:
            num_moves += home_field_pos - field_pos
        else:
            num_moves += home_field_pos

        return num_moves

    # Returns if figure can enter home and slot
    def can_enter_home(self, figure, moves, num_fields, ret_slot=False):
        home_delta = self._get_num_moves_to_home(figure, num_fields)
        print("HOME DELTA - %s" % home_delta)

        slot_delta = moves - home_delta
        print("SLOT DELTA - %s" % slot_delta)
        if slot_delta > 0 and slot_delta < self.num_figures + 1:
            # Check if specific slot in home is free
            slot = moves - home_delta - 1
            if self.target_home.is_slot_empty(slot):
                # This figure can enter target home
                if ret_slot:
                    return True, slot
                return True

        if ret_slot:
            return False, None
        return False

    def can_move(self, figure, moves, num_fields):
        home_delta = self._get_num_moves_to_home(figure, num_fields)
        return home_delta - moves > -1

    # Get figure that can move this number of moves
    def get_playable_figure(self, moves, num_fields, excluded=None):
        possible = []
        for figure in self.figures.values():
            if self.can_enter_home(figure, moves, num_fields):
                return figure

            #if home_delta - moves > 0 :
            if self.can_move(figure, moves, num_fields):
                possible.append(figure)

        # TODO get best figure to move from possible

        if possible:
            return possible[0]

        return None

