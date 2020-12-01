class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return float(1)
        elif n == 1:
            return float(x)
        elif n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            half = self.myPow(x, n / 2)
            return half * half
        else:
            half = self.myPow(x, (n - 1) / 2)
            return half * half * x
