from context import game

def test_figure_set_field_field_set_figure():
    p = game.Player("Tonda", None, None, None)

    figure = game.Figure(p, 1)
    field = game.Field(1)

    figure.set_field(field, True)
    assert figure.get_field() is field
    assert field.get_figure() is figure

    figure = game.Figure(p, 1)
    field = game.Field(1)
    figure.set_field(field, False)
    assert figure.get_field() is field
    assert field.get_figure() is not figure

    figure = game.Figure(p, 1)
    field = game.Field(1)
    field.set_figure(figure, True)
    assert figure.get_field() is field
    assert field.get_figure() is figure

    figure = game.Figure(p, 1)
    field = game.Field(1)
    field.set_figure(figure, False)
    assert figure.get_field() is not field
    assert field.get_figure() is figure

def test_figure_remove_field_field_remove_figure():
    p = game.Player("Tonda", None, None, None)

    figure = game.Figure(p, 1)
    field = game.Field(1)

    figure.set_field(field, True)

    # Check if not empty
    assert figure.get_field()
    assert field.get_figure()

    figure.remove_field()
    field.remove_figure()

    # Check if empty
    assert not figure.get_field()
    assert not field.get_figure()

def run_all():
    test_figure_set_field_field_set_figure()
    test_figure_remove_field_field_remove_figure()
    print("General tests OK")
