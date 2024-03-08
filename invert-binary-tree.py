# 1st binary tree problem

# most of tree questions will use recursive
class TreeNode():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Solution():
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        #swap process
        temp = root.left
        root.left = root.right
        root.right = temp

        #for all subtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    

# run this using driver functions

# understand traversal and insertion from NeuralNine