# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrder(self, root, k, arr):
        # answer is found
        if len(arr) == k:
            return arr[-1]
        
        if root == None:
            return None
            
        temp = self.inOrder(root.left, k, arr)
        if temp != None:
            return temp
            
        arr.append(root.val)
        
        temp = self.inOrder(root.right, k, arr)
        if temp != None:
            return temp
            
        
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        return self.inOrder(root, k, [])
        