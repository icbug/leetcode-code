# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, level = [root], 1
        res = []
        if not root:
            return res
        
        while queue:
            if level % 2 != 0:
                res.append([node.val for node in queue])
            else:
                res.append([node.val for node in queue][::-1])
            pairs = [(node.left, node.right) for node in queue]
            queue = [leaf for lr in pairs for leaf in lr if leaf]
            level += 1
        
        return res