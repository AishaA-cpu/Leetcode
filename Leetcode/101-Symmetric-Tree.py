# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymRec(root.left, root.right)
        
    def isSymRec(self,nodeLeft,nodeRight):
        if nodeLeft is None and nodeRight is None:
            return True
        if nodeLeft is None or nodeRight is None:
            return False
        if (nodeLeft.val != nodeRight.val):
            return False
        return self.isSymRec(nodeLeft.left, nodeRight.right) and self.isSymRec(nodeLeft.right, nodeRight.left)
    
    
        