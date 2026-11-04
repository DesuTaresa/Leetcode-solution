class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
      
        if 1 not in nums:
            return 1
        else:
            for i in range(1,len(nums)):
                if nums[i]-nums[i-1]>1 and nums[i-1]>0 and nums[i]>0:
                    return nums[i-1]+1
                    break
            else:
                return nums[len(nums)-1]+ 1
        