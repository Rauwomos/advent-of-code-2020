from copy import deepcopy


class Seats:
    def __init__(self, file_path: str, max_visible: int):
        with open(file_path, 'r') as f:
            self.seats = list(map(lambda x: list(x.strip()), f.readlines()))
        self.max_visible = max_visible
        self.changed = True

    def _valid_location(self, i: int, j: int) -> bool:
        return not (i < 0 or j < 0 or i >= len(self.seats) or j >= len(self.seats[i]))

    def _surrounding_occupied_count(self, i: int, j: int) -> int:
        occupied = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if x == i and y == j:
                    continue
                if self._valid_location(x, y) and self.seats[x][y] == '#':
                    occupied += 1
        return occupied

    def _update(self, i: int, j: int) -> str:
        if self.seats[i][j] == '.':
            return '.'
        surrounding_occupied_count = self._surrounding_occupied_count(i, j)
        if self.seats[i][j] == 'L':
            if surrounding_occupied_count == 0:
                return '#'
            return 'L'
        elif self.seats[i][j] == '#':
            if surrounding_occupied_count >= self.max_visible:
                return 'L'
            return '#'
        raise Exception("Unexpected character found")

    def _tick(self):
        next_seats = deepcopy(self.seats)
        self.changed = False
        for i in range(len(self.seats)):
            for j in range(len(self.seats[i])):
                next_seats[i][j] = self._update(i, j)
                if next_seats[i][j] != self.seats[i][j]:
                    self.changed = True
        self.seats = next_seats

    def run(self):
        while self.changed:
            self._tick()

    def occupied_count(self) -> int:
        occupied = 0
        for i in range(len(self.seats)):
            for j in range(len(self.seats[i])):
                if self.seats[i][j] == '#':
                    occupied += 1
        return occupied

    def __str__(self):
        return "\n".join(list(map(lambda x: "".join(x), self.seats)))
