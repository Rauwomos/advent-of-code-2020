from os import path
from day_12.ship import Ship

if __name__ == '__main__':
    ship = Ship()
    ship.run(path.abspath("input.txt"))
    print(ship.manhattan_dist())
