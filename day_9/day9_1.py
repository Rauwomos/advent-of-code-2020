from typing import List


def has_sum(value: int, nums: List[int]) -> bool:
    """Returns true if there are two numbers in nums that sum to value"""
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == value:
                return True
    return False


def find_invalid(nums: List[int], window_size: int = 25) -> int:
    for i in range(window_size, len(nums)):
        if not has_sum(nums[i], nums[i - window_size:i]):
            return nums[i]
    raise Exception("No invalid numbers found")


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        numbers = list(map(int, f.readlines()))

    print(find_invalid(numbers))
