# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def reverse_postord(node,level,ans):
            if node is None:
                return 
            if len(ans)==level:
                ans.append(node.val)
            if node.right:
                reverse_postord(node.right,level+1,ans)
            if node.left:
                reverse_postord(node.left,level+1,ans)
        ans=[]
        reverse_postord(root,0,ans)
        return ans


        