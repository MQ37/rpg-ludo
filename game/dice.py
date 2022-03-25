import random

class Dice():
    sides = None

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        val = random.randint(1, self.sides)
        print("Rolling dice - %s" % val)
        return val
