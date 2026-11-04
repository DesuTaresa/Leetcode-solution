class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        st = "abcdefghijklmnopqrstuvwxyz"
        counter = 1
       
        d = 1
        for i in range(1,len(s)):
            if st.index(s[i])-st.index(s[i-1])==1:
                counter += 1
                d = max(d, counter)
            else:
                counter = 1
        return d        