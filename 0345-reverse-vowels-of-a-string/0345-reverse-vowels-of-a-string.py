class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        d = "aeiouAEIOU"
        s = list(s)
        
        while l<=r:
            if s[l] in d and s[r] in d:
                s[l], s[r] =s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in d and s[r] not in d:
                r -= 1
            elif s[l] not in d and s[r] in d:

                l += 1
            else:
                l += 1
                r -= 1
        return "".join(s)
        