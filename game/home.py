class Home():
    owner = None
    figures = None
    num_figures = None

    def __init__(self, owner, num_figures=4):
        self.owner = owner
        self.figures = [None] * num_figures
        self.num_figures = num_figures

    def is_full(self):
        if self.figures.count(None) == 0:
            return True
        return False

    def is_empty(self):
        if self.figures.count(None) == len(self.figures):
            return True
        return False

    def add_figure(self, figure, slot):
        if self.is_full():
            return False
        self.figures[slot] = figure

    def remove_figure(self, slot):
        if self.is_empty():
            return False
        figure = self.figures[slot]
        self.figures[slot] = None
        return figure

    def get_figures(self):
        return self.figures

    def print_figures(self):
        print("Home of player %s" % self.owner)
        for slot, figure in enumerate(self.figures):
            print("Slot %s has %s" % (slot, figure))
