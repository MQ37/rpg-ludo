from context import game

def test__get_num_moves_to_home():
    home_field = game.Field(10)
    p = game.Player("Tonda", home_field, None, None)

    figure = game.Figure(p, 1)
    start_field = game.Field(11)
    start_field.set_figure(figure, True)

    num_fields = 40
    assert p._get_num_moves_to_home(figure, num_fields) == 39

    home_field = game.Field(10)
    p = game.Player("Tonda", home_field, None, None)

    figure = game.Figure(p, 1)
    start_field = game.Field(31)
    start_field.set_figure(figure, True)

    num_fields = 40
    assert p._get_num_moves_to_home(figure, num_fields) == 19


def run_all():
    test__get_num_moves_to_home()
    print("Player tests OK")

