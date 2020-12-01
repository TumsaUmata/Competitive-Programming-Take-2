class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if (K % 2 == 0) or (K % 5 == 0):
            return -1

        remainder = 0
        for N in range(1, K + 1):
            remainder = (remainder * 10 + 1) % K

            if remainder == 0:
                return N
