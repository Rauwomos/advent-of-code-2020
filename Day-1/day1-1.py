if __name__ == '__main__':
    with open("input.txt", "r") as f:
        numbers = list(map(int, f.readlines()))
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                print(numbers[i] * numbers[j])
