class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        res = s.split(" ")
        r = len(res)-1
      
        while r>=0:
            if res[r]!= "":
                return len(res[r])
                break
            r -= 1
        