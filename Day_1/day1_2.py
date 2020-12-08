if __name__ == '__main__':
    with open("input.txt", "r") as f:
        numbers = list(map(int, f.readlines()))
    for i in range(0, len(numbers)-2):
        for j in range(i+1, len(numbers)-1):
            for k in range(j+1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    print(numbers[i] * numbers[j] * numbers[k])
