from typing import List


def hit_count(slope: List[str], x_inc: int, y_inc: int) -> int:
    x = 0
    width = len(slope[0])
    count = 0
    for row in range(0, len(slope), y_inc):
        if slope[row][x] == '#':
            count += 1
        x = (x + x_inc) % width
    return count


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        slope = list(map(lambda x: x.strip(), f.readlines()))
    print(hit_count(slope, 3, 1))
