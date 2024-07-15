from collections import deque, defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rob(root):
    if not root:
        return 0

    # Dictionaries to store the maximum values for robbing and not robbing each node
    dp_rob = defaultdict(int)
    dp_not_rob = defaultdict(int)

    # BFS queue
    queue = deque([(root, 0)])  # (node, level)
    levels = defaultdict(list)

    while queue:
        node, level = queue.popleft()
        levels[level].append(node)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    # Process nodes from the bottom level up to the root
    max_level = max(levels.keys())

    for level in range(max_level, -1, -1):
        for node in levels[level]:
            # If we rob this node, we cannot rob its children
            dp_rob[node] = node.val + dp_not_rob[node.left] + dp_not_rob[node.right]

            # If we do not rob this node, we take the max value from robbing or not robbing its children
            dp_not_rob[node] = max(dp_rob[node.left], dp_not_rob[node.left]) + max(dp_rob[node.right], dp_not_rob[node.right])

    return max(dp_rob[root], dp_not_rob[root])

# Example usage
# Tree structure:
#       3
#      / \
#     2   3
#      \   \
#       3   1

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

print(rob(root))  # Output: 7
