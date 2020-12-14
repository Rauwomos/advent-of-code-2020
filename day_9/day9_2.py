from typing import List

from day_9.day9_1 import find_invalid


def find_weakness(inv: int, nums: List[int]) -> int:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums) + 1):
            res = sum(nums[i:j])
            if res == inv:
                return min(nums[i:j]) + max(nums[i:j])
            elif res > inv:
                break
    raise Exception("Didn't find result")


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        numbers = list(map(int, f.readlines()))

    invalid = find_invalid(numbers)
    print(find_weakness(invalid, numbers))
