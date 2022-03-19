class Figure():
    field = None
    owner = None
    f_id = None

    def __init__(self, owner, f_id):
        self.owner = owner
        self.f_id = f_id

    def __str__(self):
        return "Figure %s of player %s at field %s" % (self.f_id, self.owner, self.field)

    def __repr__(self):
        return str(self)

    def set_field(self, field, set_figure):
        self.field = field
        if set_figure:
            field.set_figure(self, not set_figure)

    def remove_field(self):
        field = self.field
        self.field = None
        return field

    def get_field(self):
        return self.field

    def get_owner(self):
        return self.owner

    def get_id(self):
        return self.f_id
