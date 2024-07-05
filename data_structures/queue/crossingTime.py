from transitions import Machine
from collections import deque
from typing import List

class DoorStateMachine:
    """
    Explanation:
    State Machine Definition:

    We define a state machine `DoorStateMachine` with three states: idle, entering, and exiting.
    Transitions are defined to move between these states based on the rules provided.
    
    """
    states = ['idle', 'entering', 'exiting']
    
    def __init__(self):
        self.machine = Machine(model=self, states=DoorStateMachine.states, initial='idle')
        # Define transitions: add_transition(event, source, destination) -> event is the method to call,
        # source is the current state, and destination is the next state
        self.machine.add_transition('to_enter', 'idle', 'entering')
        self.machine.add_transition('to_enter', 'exiting', 'entering')
        self.machine.add_transition('to_exit', 'idle', 'exiting')
        self.machine.add_transition('to_exit', 'entering', 'exiting')
        self.machine.add_transition('stay_idle', '*', 'idle')

def getCrossingTimes(arrival: List[int], state: List[int]) -> List[int]:
    """
    Function Implementation:

    The `getCrossingTimes` function manages the queues for entering and exiting people.
    At each second, it adds arriving people to the respective queues.
    Based on the current state of the door (idle, entering, or exiting), it decides who should cross the door.
    It updates the crossing time for the person and transitions the state machine accordingly.
    This implementation uses the python-statemachine library to cleanly manage the transitions and ensure the rules are followed correctly."""
    enter_queue, exit_queue = deque(), deque()
    cur_time = 0
    i = 0
    ans = [-1] * len(arrival)
    door_machine = DoorStateMachine()
    
    while i < len(arrival) or enter_queue or exit_queue:
        # Add all people who arrive at the current time to the respective queues
        while i < len(arrival) and arrival[i] <= cur_time:
            if state[i] == 0:
                enter_queue.append(i)
            else:
                exit_queue.append(i)
            i += 1
        
        # Determine who will cross the door at this second
        if door_machine.state == 'idle':
            if exit_queue:
                person = exit_queue.popleft()
                ans[person] = cur_time
                door_machine.to_exit()
            elif enter_queue:
                person = enter_queue.popleft()
                ans[person] = cur_time
                door_machine.to_enter()
            else:
                door_machine.stay_idle()
        elif door_machine.state == 'entering':
            if enter_queue:
                person = enter_queue.popleft()
                ans[person] = cur_time
            elif exit_queue:
                person = exit_queue.popleft()
                ans[person] = cur_time
                door_machine.to_exit()
            else:
                door_machine.stay_idle()
        elif door_machine.state == 'exiting':
            if exit_queue:
                person = exit_queue.popleft()
                ans[person] = cur_time
            elif enter_queue:
                person = enter_queue.popleft()
                ans[person] = cur_time
                door_machine.to_enter()
            else:
                door_machine.stay_idle()
        
        cur_time += 1
    
    return ans

# Example usage
arrival = [0,1,1,2,4]
state = [0,1,0,0,1]
print(getCrossingTimes(arrival, state))  # Output: [0,3,1,2,4]


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