# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if original is None:
            return None
        if original == target:
            return cloned

        res = self.getTargetCopy(original.left, cloned.left, target)
        if res is not None:
            return res
        return self.getTargetCopy(original.right, cloned.right, target)
