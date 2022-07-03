class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
                            :rtype: int
        """
        # a = list(s)
        # b = {"I" : 1, "V" : 5, "X" :10, "L": 50, "C":100, "D":500, "M":1000}
        # total = 0
        # for i in range(len(a)):
        #     num = b[a[i]]
        #     nextnum = b[a[i + 1]]

        #     if !nextnum:
        #         return total + num

        #     total += num >= nextnum ? num : -num
        #     return total

        roman = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0

        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]

        return z + roman[s[-1]]
