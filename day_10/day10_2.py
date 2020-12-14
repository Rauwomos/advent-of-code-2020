if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        numbers = sorted(list(map(int, f.readlines())))
    numbers.insert(0, 0)
    end = numbers[-1] + 3
    numbers.append(end)
    ways_to_make = {i: 0 for i in numbers}
    ways_to_make[0] = 1
    for i in ways_to_make:
        for j in range(1, 4):
            if i - j in ways_to_make:
                ways_to_make[i] += ways_to_make[i - j]
    print(ways_to_make[end])
