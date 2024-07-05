"""Sliding Window Technique
The sliding window technique involves maintaining a window that can expand and contract as needed to meet the conditions of the problem. Here's the step-by-step approach:

Initialize Variables:

left pointer starting at the beginning of the array.
current_sum to keep track of the sum of the current window.
min_length to store the minimum length of the valid subarray found.
Expand and Contract the Window:

Expand the window by moving the right pointer and adding the element at the right pointer to current_sum.
Once current_sum is greater than or equal to target, contract the window from the left side to see if we can get a smaller valid window.
Update min_length whenever a valid window is found.
Return the Result:

If min_length is not updated, return 0 indicating no valid subarray was found.
Otherwise, return min_length."""

def min_sub_array_len(target: int, nums: list[int]):
    n = len(nums)
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(n):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return 0 if min_length == float('inf') else min_length

# Example usage
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(min_sub_array_len(target, nums))  # Output: 2

target = 4
nums = [1, 4, 4]
print(min_sub_array_len(target, nums))  # Output: 1

target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(min_sub_array_len(target, nums))  # Output: 0

"""
Explanation of the Code
Initialization:

left is initialized to 0.
current_sum starts at 0.
min_length is set to infinity to ensure any valid subarray length found will be smaller.
Main Loop:

The right pointer iterates over the array.
current_sum is updated to include nums[right].
Inner While Loop:

Checks if current_sum is greater than or equal to target.
If true, it updates min_length and contracts the window from the left by incrementing left and subtracting nums[left] from current_sum.
Return Result:

If min_length remains infinity, it means no valid subarray was found, so return 0.
Otherwise, return min_length.
Time Complexity:
The time complexity is O(n) since both the left and right pointers traverse the array at most once."""