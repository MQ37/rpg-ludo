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

    def __init__(self, name, home_field, start_field, num_figures=4):
        self.name = name

        self.home_field = home_field
        self.start_field = start_field

        self.num_figures = num_figures
        self.figures = {}
        self.start_home = Home(self)
        self.target_home = Home(self)
        self._create_figures()

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

    # If all player figures are in start home
    def is_initial_round(self):
        return self.start_home.is_full()

    def is_start_field_empty(self):
        return self.start_field.is_empty()

    def print_start_home_figures(self):
        self.start_home.print_figures()
