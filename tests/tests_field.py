from context import game

def test_set_figure_non_empty():
    p = game.Player("Tonda", None, None)
    figure = game.Figure(p, 1)
    another_figure = game.Figure(p, 2)
    field = game.Field(1)

    field.set_figure(figure)

    assert field.get_figure() is figure

    assert not field.set_figure(another_figure)

    assert field.get_figure() is figure

def run_all():
    test_set_figure_non_empty()
    print("Field tests OK")

