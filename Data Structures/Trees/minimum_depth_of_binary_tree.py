# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        min_depth = 0
        while queue:
            min_depth += 1
            level_length = len(queue)
            for _ in range(level_length):
                current_node = queue.popleft()

                if not current_node.left and not current_node.right:
                    return min_depth

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
