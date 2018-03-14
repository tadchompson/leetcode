"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p,q)]
        while stack:
            temp_node_1 , temp_node_2 = stack.pop()
            if temp_node_1 and temp_node_2 and temp_node_1.val == temp_node_2.val:
                stack.append((temp_node_1.left, temp_node_2.left))
                stack.append((temp_node_1.right, temp_node_2.right))
            elif not temp_node_1 and not temp_node_2:
                continue
            else:
                return False
        return True
            
        
