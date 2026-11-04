class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        num = nums1 + nums2
        num.sort()
        if len(num)%2!=0:
            return num[len(num)//2]
        else:
            d = num[len(num)//2]
            m = num[len(num)//2-1]
            return (d+m)/2
               