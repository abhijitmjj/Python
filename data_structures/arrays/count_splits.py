from typing import List

def count_splits(nums: List[int]) -> int:
    total_sum = sum(nums)
    first_part_sum = 0
    count = 0
    
    # Iterate through the array up to the second-to-last element
    for i in range(len(nums) - 1):
        first_part_sum += nums[i]
        second_part_sum = total_sum - first_part_sum
        
        if first_part_sum >= second_part_sum:
            count += 1

    return count

# Example usage
nums = [10, 4, -8, 7]
print(count_splits(nums))  # Output: 2
