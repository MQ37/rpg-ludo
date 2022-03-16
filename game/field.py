class Field():
    figure = None
    f_id = None

    def __init__(self, f_id):
        self.f_id = f_id

    def set_figure(self, figure, set_field=False):
        self.figure = figure
        if set_field:
            figure.set_field(self, not set_field)

    def remove_figure(self):
        pass
