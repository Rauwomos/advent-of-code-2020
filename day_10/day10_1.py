if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        numbers = sorted(list(map(int, f.readlines())))
    numbers.insert(0, 0)
    diffs_1 = 0
    diffs_3 = 1
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff == 1:
            diffs_1 += 1
        elif diff == 3:
            diffs_3 += 1
    print(diffs_1 * diffs_3)
