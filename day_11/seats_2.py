from day_11.seats import Seats


class Seats2(Seats):

    def _surrounding_occupied_count(self, i: int, j: int) -> int:
        occupied_count = 0
        # Up
        for x in range(i-1, -1, -1):
            if self.seats[x][j] == '#':
                occupied_count += 1
                break
            elif self.seats[x][j] == 'L':
                break

        # Down
        for x in range(i+1, len(self.seats)):
            if self.seats[x][j] == '#':
                occupied_count += 1
                break
            elif self.seats[x][j] == 'L':
                break
        # Left
        for y in range(j-1, -1, -1):
            if self.seats[i][y] == '#':
                occupied_count += 1
                break
            elif self.seats[i][y] == 'L':
                break

        # Right
        for y in range(j+1, len(self.seats[i])):
            if self.seats[i][y] == '#':
                occupied_count += 1
                break
            elif self.seats[i][y] == 'L':
                break

        # Diagonals
        # Up left
        x = i - 1
        y = j - 1
        while x >= 0 and y >= 0:
            if self.seats[x][y] == '#':
                occupied_count += 1
                break
            elif self.seats[x][y] == 'L':
                break
            x -= 1
            y -= 1

        # Up right
        x = i - 1
        y = j + 1
        while x >= 0 and y < len(self.seats[x]):
            if self.seats[x][y] == '#':
                occupied_count += 1
                break
            elif self.seats[x][y] == 'L':
                break
            x -= 1
            y += 1

        # Down left
        x = i + 1
        y = j - 1
        while x < len(self.seats) and y >= 0:
            if self.seats[x][y] == '#':
                occupied_count += 1
                break
            elif self.seats[x][y] == 'L':
                break
            x += 1
            y -= 1

        # Up right
        x = i + 1
        y = j + 1
        while x < len(self.seats) and y < len(self.seats[x]):
            if self.seats[x][y] == '#':
                occupied_count += 1
                break
            elif self.seats[x][y] == 'L':
                break
            x += 1
            y += 1
        return occupied_count
