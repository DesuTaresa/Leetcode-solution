class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            nums=list(set(nums))
            nums.sort()
            counter = 1
            _max = 0
            for i in range(1,len(nums)):
                if nums[i]-nums[i-1]==1:
                    counter += 1
                   
                else:
                    _max = max(_max, counter)
                    counter = 1
            _max = max(_max, counter)
            return _max
            