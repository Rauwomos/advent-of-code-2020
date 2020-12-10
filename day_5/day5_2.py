from day_5.day5_1 import get_seat_id

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        seats = list(map(lambda x: x.strip(), f.readlines()))
    seat_ids = list(map(get_seat_id, seats))
    seat_ids = sorted(seat_ids)
    for i in range(1, len(seat_ids)):
        if seat_ids[i] != seat_ids[i-1] + 1:
            print(f"Gap: {seat_ids[i] - 1}")
