class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ls = [1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                ls[j] += ls[j-1] 
        return ls    