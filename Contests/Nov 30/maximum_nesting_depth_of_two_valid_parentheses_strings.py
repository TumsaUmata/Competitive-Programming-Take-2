class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = []
        level = 0
        for char in seq:
            if char == '(':
                level += 1
                result.append(level % 2)
            else:
                result.append(level % 2)
                level -= 1
        return result
