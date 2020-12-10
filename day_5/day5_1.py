import re

valid_seat_pattern = re.compile(r"^[FB]{7}[LR]{3}$")


def is_valid_seat(seat: str) -> bool:
    return bool(valid_seat_pattern.match(seat))


def get_seat_id(seat: str) -> int:
    """Returns -1 for invalid seats"""
    if not is_valid_seat(seat):
        return -1
    bin_seat = seat.replace('F', '0')
    bin_seat = bin_seat.replace('B', '1')
    bin_seat = bin_seat.replace('L', '0')
    bin_seat = bin_seat.replace('R', '1')
    return int(bin_seat, 2)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        seats = list(map(lambda x: x.strip(), f.readlines()))
    seat_ids = list(map(get_seat_id, seats))
    print(f"Max: {max(seat_ids)}")
    print(f"Min: {min(seat_ids)}")
