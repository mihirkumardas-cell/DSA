# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val==key:
            return self.deletion(root)
        temp=root
        while temp is not None:
            if temp.val>key:
                if temp.left is not None and temp.left.val==key:
                    temp.left=self.deletion(temp.left)
                    break
                else:
                    temp=temp.left
            else:
                if temp.right is not None and temp.right.val==key:
                    temp.right=self.deletion(temp.right)
                    break
                else:
                    temp=temp.right
        return root
    
    def deletion(self, node: TreeNode) -> Optional[TreeNode]:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        parent,succ=node,node.right
        while succ.left is not None:
            parent,succ=succ,succ.left
        if parent is not node:
            parent.left=succ.right
            succ.right=node.right
        succ.left=node.left
        return succ


            
    


        
        