class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        for mask in range(1 << n):
            subset = [nums[i] for i in range(n) if (mask & (1 << i))]
            res.append(subset)
            
        return res