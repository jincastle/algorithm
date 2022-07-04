class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
                            :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:   
            str1, str2 = max(strs), min(strs)
            i, j = 0, 0
            while i < len(i) and i < len(j) and str1[i] == str2[i]:
                i, match = i+1, j+1
            return str1[0:j]
