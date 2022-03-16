class Figure():
    field = None
    owner = None

    def __init__(self, owner):
        self.owner = owner

    def set_field(self, field, set_figure):
        self.field = field
        if set_figure:
            field.set_figure(self, not set_figure)
