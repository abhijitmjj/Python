def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target."""

    nums_dict: dict[int,int] = {}
    for i, num in enumerate(nums):
        if target - num in nums_dict:
            return [nums_dict[target - num], i]
        nums_dict[num] = i
    return [-1, -1]