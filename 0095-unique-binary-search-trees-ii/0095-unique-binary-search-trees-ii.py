# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        memo = {}

        def build_trees(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            
            if (start, end) in memo:
                return memo[(start, end)]

            all_trees = []

            for root_val in range(start, end + 1):
                # Generate all valid left and right subtrees
                left_subtrees = build_trees(start, root_val - 1)
                right_subtrees = build_trees(root_val + 1, end)

                # Connect every left and right subtree to root node
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_trees.append(root)

            memo[(start, end)] = all_trees
            return all_trees

        return build_trees(1, n)