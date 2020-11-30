# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []
        self.traverse(root, to_delete_set, True, result)
        return result

    def traverse(self, node, to_delete, is_valid, result):
        if not node:
            return None

        node_to_delete = node.val in to_delete
        if is_valid and not node_to_delete:
            result.append(node)

        node.left = self.traverse(node.left, to_delete, node_to_delete, result)
        node.right = self.traverse(node.right, to_delete, node_to_delete, result)
        return None if node_to_delete else node
