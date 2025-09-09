# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def visited(tree1, tree2):
            if (tree1 is None and tree2 is None):
                return True
            if tree1 is None or tree2 is None:
                return False
            if (tree1.val != tree2.val  ):
                return False    
            return visited(tree1.left, tree2.left) and visited(tree1.right, tree2.right)

        return visited(p,q)
            
        