class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def check(string):
            for s in string:
                if s == '0':
                    return False
            return True

        for i in range (1,n):
            if check(str(n-i)) and check(str(i)):
                return [i, n-i]
        