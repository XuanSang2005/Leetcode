class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        def count_bits(n):
            cnt = 0
            while n:
                cnt += n & 1
                n >>= 1
            return cnt

        for k in range(1, 61):
            x = num1 - num2 * k
            if x < 0:  # không thể âm
                continue
            if k >= count_bits(x) and k <= x:  # điều kiện chuẩn
                return k
        return -1
