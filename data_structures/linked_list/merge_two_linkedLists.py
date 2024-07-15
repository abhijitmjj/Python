from dataclasses import dataclass
from typing import Optional

@dataclass
class ListNode:
    val: int
    next: Optional['ListNode'] = None

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next, list1 = list1, list1.next
        else:
            current.next, list2 = list2, list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return dummy.next

def create_linked_list(arr: list[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head: Optional[ListNode]) -> None:
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(" -> ".join(elements) + " -> None")

# Example usage
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged_list = mergeTwoLists(list1, list2)
print_linked_list(merged_list)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
