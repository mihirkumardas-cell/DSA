# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count=0
        def dfs(TreeNode):
            if not TreeNode:
                return (0,0)
            ls,lc=dfs(TreeNode.left)
            rs,rc=dfs(TreeNode.right)
            ts=ls+rs+TreeNode.val
            tc=lc+rc+1
            if ts//tc==TreeNode.val:
                self.count+=1
            return(ts,tc)
        dfs(root)
        return self.count
        