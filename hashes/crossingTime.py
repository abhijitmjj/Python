"""
2534. Time Taken to Cross the Door
Attempted
Hard

Topics

Companies

Hint
There are n persons numbered from 0 to n - 1 and a door. Each person can enter or exit through the door once, taking one second.

You are given a non-decreasing integer array arrival of size n, where arrival[i] is the arrival time of the ith person at the door. You are also given an array state of size n, where state[i] is 0 if person i wants to enter through the door or 1 if they want to exit through the door.

If two or more persons want to use the door at the same time, they follow the following rules:

If the door was not used in the previous second, then the person who wants to exit goes first.
If the door was used in the previous second for entering, the person who wants to enter goes first.
If the door was used in the previous second for exiting, the person who wants to exit goes first.
If multiple persons want to go in the same direction, the person with the smallest index goes first.
Return an array answer of size n where answer[i] is the second at which the ith person crosses the door.

Note that:

Only one person can cross the door at each second.
A person may arrive at the door and wait without entering or exiting to follow the mentioned rules.
 

Example 1:

Input: arrival = [0,1,1,2,4], state = [0,1,0,0,1]
Output: [0,3,1,2,4]
Explanation: At each second we have the following:
- At t = 0: Person 0 is the only one who wants to enter, so they just enter through the door.
- At t = 1: Person 1 wants to exit, and person 2 wants to enter. Since the door was used the previous second for entering, person 2 enters.
- At t = 2: Person 1 still wants to exit, and person 3 wants to enter. Since the door was used the previous second for entering, person 3 enters.
- At t = 3: Person 1 is the only one who wants to exit, so they just exit through the door.
- At t = 4: Person 4 is the only one who wants to exit, so they just exit through the door.
Example 2:

Input: arrival = [0,0,0], state = [1,0,1]
Output: [0,2,1]
Explanation: At each second we have the following:
- At t = 0: Person 1 wants to enter while persons 0 and 2 want to exit. Since the door was not used in the previous second, the persons who want to exit get to go first. Since person 0 has a smaller index, they exit first.
- At t = 1: Person 1 wants to enter, and person 2 wants to exit. Since the door was used in the previous second for exiting, person 2 exits.
- At t = 2: Person 1 is the only one who wants to enter, so they just enter through the door.
 

Constraints:

n == arrival.length == state.length
1 <= n <= 105
0 <= arrival[i] <= n
arrival is sorted in non-decreasing order.
state[i] is either 0 or 1."""

from collections import deque
from typing import List

from collections import deque


def getCrossingTimes(arrival, state):
    # Queues to store people waiting to enter or exit
    enter_pool, exit_pool = deque(), deque()
    cur_time = 0     # Current time (starts at 0)
    prev_state = 1   # Previous state of the door (1 indicates no one crossed previously)
    i = 0             # Index to track people in arrival array
    ans = [0] * len(arrival)  # Result array (initialized with all 0s)

    # Main loop: Continues until everyone has crossed or is waiting in a queue
    while i < len(arrival) or enter_pool or exit_pool:
        
        # Enqueue people who arrive at the current time
        while i < len(arrival) and arrival[i] <= cur_time:
            (enter_pool if state[i] == 0 else exit_pool).append(i)  # Ternary operator for queue selection
            i += 1

        # Determine who crosses the door based on previous state
        if prev_state == 1:  # If the door was unused or last used for exiting
            if exit_pool:    # Prioritize exiting if possible
                ans[exit_pool.popleft()] = cur_time 
            elif enter_pool: # Otherwise, allow entering
                ans[enter_pool.popleft()] = cur_time
                prev_state = 0 
        else:  # If the door was last used for entering
            if enter_pool:   # Prioritize entering if possible
                ans[enter_pool.popleft()] = cur_time
            elif exit_pool: # Otherwise, allow exiting
                ans[exit_pool.popleft()] = cur_time
                prev_state = 1
            else:         # If both queues are empty, reset prev_state to allow exit next
                prev_state = 1 

        cur_time += 1  # Increment time for the next iteration

    return ans


# Example usage
arrival = [0, 1, 2, 3, 4]
state = [0, 1, 1, 0, 1]
print(getCrossingTimes(arrival, state))  # Output: [0, 1, 2, 4, 3]


# Example usage
arrival = [0, 1, 1, 2, 4]
state = [0, 1, 0, 0, 1]
print(getCrossingTimes(arrival, state))  # Output: [0, 3, 1, 2, 4]

"""
Input: arrival = [0,1,1,2,4], state = [0,1,0,0,1]
Output: [0,3,1,2,4]"""

# Example usage
arrival = [0,1,1,2,4]
state = [0,1,0,0,1]
print(getCrossingTimes(arrival, state))  # Output: [0, 3, 1, 2, 4]

# Example usage
arrival = [0,0,0]
state = [1,0,1]
"""
Input: arrival = [0,0,0], state = [1,0,1]
Output: [0,2,1]"""
print(getCrossingTimes(arrival, state))  # Output: [0, 2, 1]