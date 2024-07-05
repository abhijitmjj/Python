def find_numbers(nums: list[int]) -> list[int]:
    """
    Given an array of two integers, find all the unique numbers x in nums
    that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
    """
    nums_set = set(nums)
    return [num for num in nums if num + 1 not in nums_set and num - 1 not in nums_set]
