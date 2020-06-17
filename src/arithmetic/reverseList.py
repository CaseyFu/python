"""反转单链表"""


class Node:
    val = None
    next = None

    def __init__(self, val: int):
        self.val = val

    def __str__(self):
        return str(self.val)


def reverseList1(head: Node):
    if(not head.next):
        return
    p: Node = head.next.next
    q: Node = p.next
    head.next.next = None
    while(p):
        p.next = head.next
        head.next = p
        p = q
        if(q):
            q = q.next


def reverseList2(head: Node):
    p: Node = head.next
    while(p.next):
        q: Node = p.next
        p.next = q.next
        q.next = head.next
        head.next = q


def reverseListRange(head: Node, m: int, n: int):
    """
    [m, n]范围内一趟转置单链表
    这是一个带头节点的单链表, 
    头 1 2 3 4 5 6 7
    [3, 5]
    头 1 2 5 4 3 6 7 
    """
    











    
    # if(not head.next):
    #     return
    # pre: Node = head
    # for i in range(m-1):
    #     pre = pre.next
    # p: Node = pre.next
    # for i in range(m, n):
    #     q: Node = p.next
    #     p.next = q.next
    #     q.next = pre.next
    #     pre.next = q


def reverseList_Recursion(head: Node):
    if not head.next:
        return head
    last: Node = reverseList_Recursion(head.next)
    head.next.next = head
    head.next = None
    return last


successor = None


def reverseListN(head: Node, n: int):
    """逆转前n个"""
    if n <= 0:
        return
    if n == 1 or not head.next:
        global successor
        successor = head.next
        return head
    last: Node = reverseListN(head.next, n-1)
    head.next.next = head
    head.next = successor
    return last


def reverseList_Recursion2(head: Node, m: int, n: int):
    """逆转[m, n]个 m<list.size()-1"""
    if m >= n:
        return
    if not head.next:
        return head
    if m == 1:
        return reverseListN(head, n)
    head.next = reverseList_Recursion2(head.next, m-1, n-1)
    return head


def printList(head: Node):
    p: Node = head.next
    while(p):
        print(p, end="\t")
        p = p.next
    print()


head = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

# printList(head)
reverseListRange(head, 3, 5)
# head.next = reverseList_Recursion(head.next)
# head.next = reverseList_Recursion2(head.next, 6, 7)
# printList(head)
