class Field():
    figure = None
    f_id = None

    def __init__(self, f_id):
        self.f_id = f_id

    def __str__(self):
        return "Field %s containing %s" % (self.f_id, self.figure)

    def __repr__(self):
        return str(self)

    def set_figure(self, figure, set_field=False):
        if self.figure:
            return False

        self.figure = figure
        if set_field:
            figure.set_field(self, not set_field)

    def remove_figure(self):
        figure = self.figure
        self.figure = None
        return figure

    def get_figure(self):
        return self.figure

    def get_id(self):
        return self.f_id

    def is_empty(self):
        return self.figure is None
