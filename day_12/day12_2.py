from os import path
from day_12.ship2 import Ship2

if __name__ == '__main__':
    ship = Ship2()
    ship.run(path.abspath("input.txt"))
    print(ship.manhattan_dist())
