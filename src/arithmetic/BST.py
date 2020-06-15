"""
二叉搜索树, BST
判断合法性, 增, 删, 改(不用), 查
"""


class TreeNode:
    val: int
    left, right = None, None

    def __init__(self, val: int):
        self.val = val


def traverse(root: TreeNode):
    """遍历二叉树"""
    if(not root):
        return None
    print(root.val, end="\t")
    traverse(root.left)
    traverse(root.right)


def buildTree(list: list) -> TreeNode:
    """按列表顺序构造一颗长度为7二叉树, 非BST"""
    root = TreeNode(list[0])
    n1 = TreeNode(list[1])
    n2 = TreeNode(list[2])
    n3 = TreeNode(list[3])
    n4 = TreeNode(list[4])
    n5 = TreeNode(list[5])
    n6 = TreeNode(list[6])
    root.left, root.right = n1, n2
    n1.left, n1.right = n3, n4
    n2.left, n2.right = n5, n6
    return root


def isSame(t1: TreeNode, t2: TreeNode) -> bool:
    """判断两颗二叉树是否相同"""
    if(not t1 and not t2):
        return True
    elif(not t1 or not t2):
        return False
    elif(t1.val != t2.val):
        return False
    return isSame(t1.left, t2.left) and isSame(t1.right, t2.right)


def plusOne(node: TreeNode):
    """给二叉树的每一个节点+1"""
    if(not node):
        return None
    node.val += 1
    plusOne(node.left)
    plusOne(node.right)


def validBST(root: TreeNode):
    """合法的BST"""
    print(validBST_Recur(root, None, None))


def validBST_Recur(root: TreeNode, min: TreeNode, max: TreeNode):
    """min为整个左子树的最小值, max为整个右子树的最大值"""
    if(not root):
        return True
    else:
        if(min and root.val < min.val):
            return False
        if(max and root.val > max.val):
            return False
    return validBST_Recur(root.left, min, root) and validBST_Recur(root.right, root, max)


def isInBST(root: TreeNode, target: int):
    """在BST中查找是否有target"""
    if(not root):
        return False
    elif(target == root.val):
        return True
    elif(target < root.val):
        return isInBST(root.left, target)
    elif(target > root.val):
        return isInBST(root.right, target)


def bstFramework(root: TreeNode, target: int):
    """BST遍历框架"""
    if(target == root.val):
        print("这就是目标节点, 做点什么")
    elif(target < root.val):
        bstFramework(root.left, target)
    elif(target > root.val):
        bstFramework(root.right, target)


def insertIntoBST(root: TreeNode, val: int):
    """在BST中插入val"""
    if(not root):
        return TreeNode(val)
    # if(val == root.val) 一般不会插入已存在的元素
    elif(val < root.val):
        root.left = insertIntoBST(root.left, val)
    elif(val > root.val):
        root.right = insertIntoBST(root.right, val)
    return root


def deleteNode(root: TreeNode, val: int):
    """删除BST中的val"""
    if(not root):
        return None
    if(root.val == val):
        # 1. 要删除的节点没有孩子, 直接return None
        # 2. 要删除的节点只有一个孩子, 返回这个孩子
        # 3. 要删除的节点有左右两个孩子, 找到右子树最小的孩子, 用这个最小的孩子覆盖当前root, 删除最小孩子
        if(not root.left):
            return root.right
        if(not root.right):
            return root.left
        root.val = getMin(root.right).val  # 把右子树最小孩子赋给当前
        root.right = deleteNode(root.right, root.val)
    elif(val < root.val):
        root.left = deleteNode(root.left, val)
    elif(val > root.val):
        root.right = deleteNode(root.right, val)
    return root
    


def getMin(root: TreeNode) -> TreeNode:
    """返回树的最小节点, 即最左边"""
    while(root.left):
        root = root.left
    return root


r1 = buildTree([3, 1, 5, 0, 2, 4, 7])
# r2 = buildTree([3, 1, 5, 0, 2, 4, 7])
traverse(r1)
# print()
# traverse(r2)
validBST(r1)
# print(isSame(r1, r2))
# plusOne(r1)
# traverse(r1)
# print()
# validBST(r1)
# print(isInBST(r1, 6))
# insertIntoBST(r1, -1)
# insertIntoBST(r1, 6)
# traverse(r1)
# print()
# deleteNode(r1, 6)
# deleteNode(r1, 3)
# traverse(r1)
