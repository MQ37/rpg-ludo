from context import game

def test_home_add_remove_figure():
    p = game.Player("Tonda", None, None, None)
    h = game.Home(p, num_figures=4)
    f = game.Figure(p, 1)

    assert h.is_empty()

    h.add_figure(f, 0)
    assert not h.is_empty()

    # Popped figure from home is Figure f
    assert h.remove_figure(0) is f

    h.add_figure(game.Figure(p, 1), 0)
    h.add_figure(game.Figure(p, 2), 1)
    h.add_figure(game.Figure(p, 3), 2)
    h.add_figure(game.Figure(p, 4), 3)

    assert h.is_full()

def run_all():
    test_home_add_remove_figure()
    print("Home tests OK")
