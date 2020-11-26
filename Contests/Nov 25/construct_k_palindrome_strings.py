class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        frequency_map = {}
        for char in s:
            if char not in frequency_map:
                frequency_map[char] = 0
            frequency_map[char] += 1

        count = 0
        for char in frequency_map.values():
            if char % 2 != 0:
                count += 1

        if count > k:
            return False
        else:
            return True
