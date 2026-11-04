class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        t = [i for i in range(s+1)]
        for j in t:
            if j not in nums:
                return j