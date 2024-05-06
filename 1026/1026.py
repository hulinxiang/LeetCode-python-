# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        val = 0

        def dfs(node: Optional[TreeNode], mn: int, mx: int) -> None:
            nonlocal val
            if node is None:
                val = max(val, mx - mn)
                return

            mn = min(node.val, mn)
            mx = max(node.val, mx)
            dfs(node.left, mn, mx)
            dfs(node.right, mn, mx)

        dfs(root, root.val, root.val)
        return val
