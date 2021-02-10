class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ###递归算法从叶节点往根节点推###先找到最后的叶子结点，从叶子结点开始一步步返回是否平衡##
        if root == None:
            return True
        elif abs(self.height(root.left)-self.height(root.right))>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self,root):
        if root == None:
            return 0
        else:
            #l = 1 + self.height(root.left)
            #r = 1 + self.height(root.right)
            #return max(l,r)
            return max(self.height(root.left),self.height(root.right))+1