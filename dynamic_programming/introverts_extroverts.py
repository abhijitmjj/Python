from functools import lru_cache
from typing import Tuple
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, I: int, E: int) -> int:
        # Constants for gains and losses
        InG, ExG, InL, ExL = 120, 40, -30, 20
        # Interaction effects between neighboring cells
        fine = [[0, 0, 0], [0, 2*InL, InL+ExL], [0, InL+ExL, 2*ExL]]
        @lru_cache(None)
        def dp(i: int, j: int, row: Tuple[int], I: int, E: int) -> int:
            # Base case
            if i == m:
                return 0
            # Move to the next row if we are at the end of the current row
            if j == n:
                return dp(i + 1, 0, row, I, E)
            ans = []
            # Possible placements: (value, remaining introverts, remaining extroverts, gain)
            neibs = [(1, I-1, E, InG), (2, I, E-1, ExG), (0, I, E, 0)]
            # Evaluate each placement
            for val, dx, dy, gain in neibs:
                # Check if we can place an introvert or extrovert
                if dx >= 0 and dy >= 0:
                    # Recursive DP call with updated state
                    new_row = (val,) + row[:-1]
                    tmp = dp(i, j+1, new_row, dx, dy) + gain
                    # Add interaction effects from right neighbor
                    if j > 0:
                        tmp += fine[val][row[0]]
                    # Add interaction effects from down neighbor
                    if i > 0:
                        tmp += fine[val][row[-1]]
                    ans.append(tmp)
            return max(ans)
        
        # Start the DP with initial state
        return dp(0, 0, tuple([0] * n), I, E)
# Example usage
solution = Solution()
print(solution.getMaxGridHappiness(2, 2, 4, 0)) # Expected: 240
print(solution.getMaxGridHappiness(2, 3, 1, 2)) # Expected: 240
print(solution.getMaxGridHappiness(3, 1, 2, 1)) # Expected: 260
print(solution.getMaxGridHappiness(2, 2, 0, 2)) # Expected: 120

# class Solution:
#     def getMaxGridHappiness(self, m: int, n: int, I: int, E: int) -> int:
#         InG, ExG, InL, ExL = 120, 40, -30, 20
#         fine = [[0, 0, 0], [0, 2*InL, InL+ExL], [0, InL+ExL, 2*ExL]]

#         @lru_cache(None)
#         def dp(index: int, row: Tuple[int], I: int, E: int) -> int:
#             if index == -1: 
#                 return 0

#             R, C = divmod(index, n)
#             ans = []
#             neibs = [(1, I-1, E, InG), (2, I, E-1, ExG), (0, I, E, 0)]  
            
#             for val, dx, dy, gain in neibs:
#                 if dx >= 0 and dy >= 0:
#                     tmp = dp(index - 1, (val,) + row[:-1], dx, dy) + gain
#                     if C < n - 1: 
#                         tmp += fine[val][row[0]]  # right neighbor
#                     if R < m - 1: 
#                         tmp += fine[val][row[-1]] # down neighbor
#                     ans.append(tmp)

#             return max(ans)
        
#         if m < n: 
#             m, n = n, m
            
#         return dp(m * n - 1, tuple([0] * n), I, E)