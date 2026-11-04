class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        d =  1
        b = n
        while b>1:

            b /= 4
            d *= 4
        if d!=n:
            return False
        else:  
            return True