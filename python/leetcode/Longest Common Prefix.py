from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for str in zip(*strs):
            if len(set(str)) == 1:
                res += str[0]
            else:
                return res
        return res
