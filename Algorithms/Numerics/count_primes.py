class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        count = 1
        for i in range(3, n):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, n):
        if n <= 1:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False

        return True
