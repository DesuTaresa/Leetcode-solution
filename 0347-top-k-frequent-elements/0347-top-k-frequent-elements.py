class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        
        ls = dic.most_common(k)
        res =[i for i,v in ls ]
    
             
        return res


        