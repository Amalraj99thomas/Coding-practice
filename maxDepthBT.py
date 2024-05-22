class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def maxDepthBFS(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:

            for i in range(len(q)):
               node = q.popleft()
               if node.left: # is non null
                   q.append(node.left)
               if node.right:
                   q.append(node.right)

            level += 1
        return level
    
    def maxDepthDFs(self, root: TreeNode) -> int:
      return None  



