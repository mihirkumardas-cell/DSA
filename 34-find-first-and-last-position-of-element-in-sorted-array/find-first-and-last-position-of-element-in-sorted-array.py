class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_s(find_f):
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    if find_f:
                        high=mid-1
                    else:
                        low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        f=binary_s(True)
        if f==-1:
            return [-1,-1]
        l=binary_s(False )
        return [f,l]


        
        