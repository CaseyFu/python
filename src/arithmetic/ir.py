from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """判断两颗二叉树是否相同"""

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p: TreeNode, q: TreeNode):
            if (not p and not q):
                return True
            if (not p or not q):
                return False
            if (p.val != q.val):
                return False
            return True

        queue = deque([(p, q), ])
        while (queue):
            p, q = queue.popleft()
            if (not check(p, q)):
                return False
            if(p):
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True

    def traverse(self, p: TreeNode):
        if (p.left):
            self.traverse(p.left)
        print(p.val, end="\t")
        if (p.right):
            self.traverse(p.right)

    def test(self):
        print("hhh")

    def constructTree(self, node: list):
        root = TreeNode(node[0])
        r1 = TreeNode(node[1])
        r2 = TreeNode(node[2])
        r3 = TreeNode(node[3])
        r4 = TreeNode(node[4])
        r5 = TreeNode(node[5])
        r6 = TreeNode(node[6])
        root.left, root.right = r1, r2
        r1.left, r1.right = r3, r4
        r2.left, r2.right = r5, r6
        return root


inlet = Solution()
r1 = inlet.constructTree([1, 2, 3, 4, 5, 6, 7])
r2 = inlet.constructTree([1, 2, 3, 4, 5, 6, 7])
print(inlet.isSameTree(r1, r2))
# inlet.test()
