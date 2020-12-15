from day_11.seats_2 import Seats2

if __name__ == '__main__':
    seats = Seats2("input.txt", 5)
    seats.run()
    print(seats.occupied_count())
