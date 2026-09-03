class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_o=min_e=None
        has_o=has_e=False
        for i in nums1:
            if i%2==1:
                has_o=True
                if min_o is None or i<min_o:
                    min_o=i
            else:
                has_e=True
                if min_e is None or i<min_e:
                    min_e=i
        all_e=not has_o
        all_o=not has_e or (has_o and min_o < min_e)
        return all_o or all_e
            
            
        