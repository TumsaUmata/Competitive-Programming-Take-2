# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next

        reversed_stack = stack[::-1]
        return stack == reversed_stack
