from day_3.day3_1 import hit_count

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        slope = list(map(lambda x: x.strip(), f.readlines()))

    res_1_1 = hit_count(slope, 1, 1)
    res_3_1 = hit_count(slope, 3, 1)
    res_5_1 = hit_count(slope, 5, 1)
    res_7_1 = hit_count(slope, 7, 1)
    res_1_2 = hit_count(slope, 1, 2)

    print(res_1_1 * res_3_1 * res_5_1 * res_7_1 * res_1_2)
