from game import Game

g = Game()
print(g.players)

f = g.fields[0]

fig = g.players[0].figures[0]

f.set_figure(fig, True)

print(f.figure)
print(fig)
print(fig.field)
print(f)

fig.set_field(f, True)
print(f.figure)
print(fig)
print(fig.field)
print(f)
