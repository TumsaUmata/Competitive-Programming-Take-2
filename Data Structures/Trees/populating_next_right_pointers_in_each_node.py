# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def connect(self, root):
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                queue[i - 1].next = queue[i]

            queue[-1].next = None
            new_queue = deque()
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)

            queue = new_queue
        return root
