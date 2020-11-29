# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque()
        queue.append(root)

        while queue:
            current_level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    current_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    current_level.append(None)

            mid = level_size // 2
            if mid != 0:
                if current_level[:mid] != current_level[-1:mid - level_size - 1:-1]:
                    return False
        return True
