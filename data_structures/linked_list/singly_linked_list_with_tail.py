from typing import Any

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next : Node  | None = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, data: Any):
        """Append a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """Prepend a node with the given data to the start of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_node(self, key):
        """Delete the first node with the given data."""
        current = self.head
        if current and current.data == key:
            self.head = current.next
            if self.head is None:  # List becomes empty
                self.tail = None
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        if current.next is None:  # Deleted node was the tail
            self.tail = prev
        current = None

    def search(self, key):
        """Search for a node with the given data."""
        current = self.head
        while current and current.data != key:
            current = current.next
        return current

    def print_list(self):
        """Print the entire list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_after_node(self, prev_node, data):
        """Insert a node with the given data after a specified node."""
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        if new_node.next is None:  # New node becomes the tail
            self.tail = new_node

    def length(self):
        """Return the length of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        current = self.head
        self.tail = self.head  # Update the tail to be the old head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example usage
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.prepend(0)
    linked_list.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

    linked_list.delete_node(2)
    linked_list.print_list()  # Output: 0 -> 1 -> 3 -> None

    print("Length:", linked_list.length())  # Output: Length: 3

    linked_list.reverse()
    linked_list.print_list()  # Output: 3 -> 1 -> 0 -> None

    found_node = linked_list.search(1)
    print("Found:", found_node.data if found_node else "Not Found")  # Output: Found: 1

    linked_list.insert_after_node(found_node, 2)
    linked_list.print_list()  # Output: 3 -> 1 -> 2 -> 0 -> None
