class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0 for _ in range(n + 1)]

        for start, end, seats in bookings:
            result[start - 1] += seats
            result[end] -= seats

        _sum = 0
        for i in range(len(result)):
            result[i] += _sum
            _sum = result[i]

        return result[:-1]
