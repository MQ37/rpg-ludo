from .figure import Figure
from .home import Home

class Player():
    name = None
    num_figures = None
    figures = None
    start_home = None
    target_home = None

    def __init__(self, name, num_figures=4):
        self.name = name
        self.num_figures = num_figures
        self.figures = []
        self._create_figures()

        self.start_home = Home(self)
        self.target_home = Home(self)

    def __str__(self):
        return "Player %s" % self.name

    def __repr__(self):
        return str(self)

    def _create_figures(self):
        for _ in range(self.num_figures):
            f = Figure(self)
            self.figures.append(f)
