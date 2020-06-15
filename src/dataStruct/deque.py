"""
双端队列的封装 底层双向循环队列
head- - - - - - -tail- - - - - -head
enQueue         enQueue
deQueue         deQueue

"""


class Node:
    val = None
    next, prev = None, None

    def __init__(self, val):
        self.val = val

    def __str__(self) -> str:
        return str(self.val)


class Deque:
    __size = 0
    __head = None   # 只设头节点

    def __init__(self):
        self.__head = Node(0)
        self.__head.next = self.__head
        self.__head.prev = self.__head

    def enDeque_head(self, val):
        node: Node = Node(val)
        node.prev = self.__head
        node.next = self.__head.next
        self.__head.next.prev = node
        self.__head.next = node
        self.__size += 1

    def enDeque_tail(self, val):
        node: Node = Node(val)
        node.prev = self.__head.prev
        node.next = self.__head
        self.__head.prev.next = node
        self.__head.prev = node
        self.__size += 1

    def deDeque_head(self):
        """删除首元节点"""
        if(not self.__head.next):
            return None
        p: Node = self.__head.next
        self.__head.next = p.next
        p.next.prev = self.__head
        self.__size -= 1
        return p.val

    def deDeque_tail(self):
        """删除最后一个节点"""
        if(not self.__head.next):
            return None
        p: Node = self.__head.prev
        p.prev.next = self.__head
        self.__head.prev = p.prev
        self.__size -= 1
        return p.val

    def peek_head(self):
        return self.__head.next.val

    def peek_tail(self):
        return self.__head.prev.val

    def size(self):
        return self.__size

    def isEmpty(self):
        return True if self.__size == 0 else False

    def printDeque(self) -> list:
        p: Node = self.__head.next
        result: list = []
        while(p != self.__head):
            print(p, end="\t")
            result.append(p)
            p = p.next
        return result


# d = Deque()
# d.enDeque_head(1)
# d.enDeque_head(2)
# d.enDeque_tail(3)
# d.enDeque_tail(4)
# print(d.peek_head())
# print(d.peek_tail())
# print(d.deDeque_tail())
# print(d.deDeque_head())

# d.printDeque()


# print()
# print("size:", d.size())
# print("isEmpty:", d.isEmpty())
