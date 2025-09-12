class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for c in s:
            if (0x104111 >> (ord(c) - 97)) & 1:
                return True
        return False