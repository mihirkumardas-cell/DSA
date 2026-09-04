class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        for i in range(n):
            l_max=max(nums[0:i+1])
            r_min=min(nums[i:n])
            if l_max-r_min<=k:
                return i
        return -1

        