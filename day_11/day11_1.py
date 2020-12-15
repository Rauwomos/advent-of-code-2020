from day_11.seats import Seats

if __name__ == '__main__':
    seats = Seats("input.txt", 4)
    seats.run()
    print(seats.occupied_count())
