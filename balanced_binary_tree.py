# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance_and_height(node):
            if not node:
                return (True, 0) 
            
            left_balanced, left_height = check_balance_and_height(node.left)
            if not left_balanced:
                return (False, 0)  
            
            right_balanced, right_height = check_balance_and_height(node.right)
            if not right_balanced:
                return (False, 0)  
            
            if abs(left_height - right_height) > 1:
                return (False, 0)
            
            return (True, max(left_height, right_height) + 1)
        
        balanced, _ = check_balance_and_height(root)
        return balanced
