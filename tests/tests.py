from context import game

def test_figure_set_field_field_set_figure():
    p = game.Player("Tonda")

    figure = game.Figure(p)
    field = game.Field(1)

    figure.set_field(field, True)
    assert figure.field is field
    assert field.figure is figure

    field.figure = None
    figure.field = None
    figure.set_field(field, False)
    assert figure.field is field
    assert field.figure is not figure

    field.figure = None
    figure.field = None
    field.set_figure(figure, True)
    assert figure.field is field
    assert field.figure is figure

    field.figure = None
    figure.field = None
    field.set_figure(figure, False)
    assert figure.field is not field
    assert field.figure is figure

def main():
    test_figure_set_field_field_set_figure()

if __name__ == "__main__":
    main()
