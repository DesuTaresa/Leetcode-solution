class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        else:
            ls = strs[0]
            for i in range(len(ls)):
                ch = ls[i]
                for j in strs[1:]:
                    if i == len(j) or j[i] != ch:
                        return ls[:i]
                        
            return ls