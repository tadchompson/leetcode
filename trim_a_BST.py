"""
Given a binary search tree and the lowest and highest
boundaries as L and R, trim the tree so that all its
elements lies in [L, R] (R >= L). You might need to
change the root of the tree, so the result should 
return the new root of the trimmed binary search tree.
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1


"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root:
            if root.val > R or root.val < L:
                root = self.trimBST(root.left,L,R) or self.trimBST(root.right,L,R)
            else:
                root.left = self.trimBST(root.left,L,R)
                root.right = self.trimBST(root.right, L, R)
                return root
        return root
