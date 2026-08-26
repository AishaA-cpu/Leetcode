# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        return self.maxDepthRec(depth, root)
        
    def maxDepthRec(self, val, root):
        if root is None:
            return val
        left = self.maxDepthRec(val, root.left) + 1
        right = self.maxDepthRec(val, root.right) + 1
        val = max(left, right)
        return val