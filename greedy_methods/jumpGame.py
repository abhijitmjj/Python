"""
Approach
A greedy approach works well for this problem.
The idea is to keep track of the farthest index that can be reached as we iterate through the array.
If, at any point, the current index exceeds the farthest reachable index, we can conclude that it's not possible to reach the last index.

Algorithm
Initialize a variable farthest to 0, representing the farthest index we can reach.
Iterate through the array using a loop.
At each index i, check if i is greater than farthest. If it is, return false because it means we can't proceed further.
Update farthest to be the maximum of farthest and i + nums[i].
If farthest is greater than or equal to the last index by the end of the loop, return true.

Explanation of the Code
Initialization:

farthest is initialized to 0, representing the farthest index we can reach from the start.
Iteration:

Loop through each index i of the array.
If i is greater than farthest, it means we cannot reach index i, so return false.
Update farthest to be the maximum of its current value and i + nums[i], representing the new farthest index we can reach from the current position.
Final Check:

After the loop, check if farthest is greater than or equal to the last index (len(nums) - 1). If it is, return true, indicating that we can reach the last index.
This greedy approach ensures that we efficiently determine whether reaching the last index is possible by keeping track of the farthest reachable index at each step."""



from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for idx, elem in enumerate(nums):
            if idx > farthest:
                return False
            farthest = max(farthest, idx+elem)
        return farthest >= len(nums) - 1
    

# Example usage
nums = [2, 3, 1, 1, 4]
print(Solution().canJump(nums))  # Output: True