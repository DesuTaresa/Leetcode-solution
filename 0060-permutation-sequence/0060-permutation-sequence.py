class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ls = []
        for i in range(1, n+1):
            ls.append(i)
        ans = ""
        for j in range(n-1, -1, -1):
            d = 1
            for x in range(1, j+1):
                d *= x
            index = (k-1)//d
            ans += str(ls[index])
            ls.pop(index)
            k = (k-1)%d+1
        return ans

        