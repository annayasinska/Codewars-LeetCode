from collections import deque
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if not node:
        return []
    result = []
    q = deque([node])
    while q :
        c = q.popleft()
        result.append(c.value)
        if c.left:
            q.append(c.left)
        if c.right:
            q.append(c.right)
    return result