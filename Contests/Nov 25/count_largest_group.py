class Solution:
    def countLargestGroup(self, n: int) -> int:
        digits_sum_map = {}
        for i in range(1, n + 1):
            num = i
            count = 0
            while num >= 10:
                count += num % 10
                num //= 10
            count += num

            if count in digits_sum_map:
                digits_sum_map[count] += 1
            else:
                digits_sum_map[count] = 1

        max_val = max(digits_sum_map.values())
        count_group = 0
        for val in digits_sum_map.values():
            if val == max_val:
                count_group += 1
        return count_group
