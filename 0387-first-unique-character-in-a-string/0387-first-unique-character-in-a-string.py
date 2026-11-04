class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)

        for i, j in enumerate(s):
            if dic[j]==1:
                return i
        return -1



        