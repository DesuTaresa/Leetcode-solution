class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        r = 0
        l = 0

        while l < len(nums):
            if nums[l] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                r += 1

            l += 1
        return nums