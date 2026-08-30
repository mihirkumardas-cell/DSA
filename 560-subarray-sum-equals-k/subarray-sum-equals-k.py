class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        cnt_map={0:1}
        res=0
        for i in nums:
            prefix_sum+=i
            if (prefix_sum-k) in cnt_map:
                res+=cnt_map[prefix_sum-k]
            cnt_map[prefix_sum]=cnt_map.get(prefix_sum,0)+1
        return res
        
        