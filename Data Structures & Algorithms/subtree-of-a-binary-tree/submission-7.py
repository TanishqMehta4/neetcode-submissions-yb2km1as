# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def Subtree(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False

            return Subtree(root.left,subRoot.left) and Subtree(root.right,subRoot.right)

        if not subRoot:
            return True
        if not root:
            return False

        q = deque([root])

        while q:
            node = q.popleft()
            if Subtree(node,subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


        return False