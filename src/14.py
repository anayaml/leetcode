class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        else:
            shrt = min(strs,key=len)
            for i, char in enumerate(shrt):
                for s in strs:
                    if s[i] != char:
                        return shrt[:i]
            return shrt