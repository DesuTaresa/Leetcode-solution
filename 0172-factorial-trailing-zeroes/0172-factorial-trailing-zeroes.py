import sys


sys.set_int_max_str_digits(0)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        else:
            d  = 1
            for i in range(1, n+1):
                d *= i
            s = str(d)
            m = 0
            for j in range(len(s)-1, -1, -1):
                if s[j]=="0":
                    m += 1
                else:
                    break
            return m


        