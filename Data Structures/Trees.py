# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            level_max = float('-inf')
            for _ in range(level_size):
                current_node = queue.popleft()
                level_max = max(level_max, current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            result.append(level_max)

        return result
