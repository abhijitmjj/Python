class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    """
    Main Idea:
    We need to reverse a portion of a singly linked list between two given positions left and right.
    The rest of the list should remain unchanged.

    Steps:

    Identify the portion to reverse:

    Traverse the list to find the nodes at positions left and right.
    Reverse the identified portion:

    Use pointers to reverse the sublist.
    Reconnect the reversed portion:

    Link the reversed sublist back into the original list at the correct positions.
    
    Detailed Steps:
    
    1. Initialization:

    Create a dummy node to simplify edge cases.
    Use pointers to traverse to the node just before the left position (left-1).
    
    2. Traverse and Reverse:

    Use additional pointers to reverse the nodes between left and right.
    
    3. Reconnection:

    Adjust pointers to reconnect the reversed sublist back to the original list.
    """
    # Step 1: Initialization
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Step 2: Traverse to the left-1 position
    for _ in range(left - 1):
        prev = prev.next
    
    # Step 3: Reverse the sublist from left to right
    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    
    # Step 4: Return the modified list
    return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values
def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# Example usage:
head = create_linked_list([1, 2, 3, 4, 5])
left, right = 2, 4
new_head = reverseBetween(head, left, right)
result = linked_list_to_list(new_head)
print(result)  # Output: [1, 4, 3, 2, 5]
