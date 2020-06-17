"""队列的封装"""

class Node:
    val = None
    next = None

    def __init__(self, val):
        self.val = val

    def __str__(self) -> str:
        return str(self.val)


class Queue:
    __size = 0
    __head, __tail= None, None
    def __init__(self):
        self.__head = Node(0)
        self.__tail = self.__head

    def enQueue(self, val):
        node:Node = Node(val)
        self.__tail.next = node
        self.__tail = node
        self.__size += 1

    def deQueue(self):
        """删除首元节点"""
        if(not self.__head.next):
            return None
        p:Node = self.__head.next 
        self.__head.next = p.next
        self.__size -= 1
        return p

    def peek(self):
        return self.__head.next

    def size(self):
        return self.__size

    def isEmpty(self):
        return True if self.__size==0 else False

    def printQueue(self)->list:
        p:Node = self.__head.next
        l:list = []
        while(p):
            print(p, end="\t")
            l.append(p)
            p = p.next
        return l

# q = Queue()
# q.enQueue(1)
# q.enQueue(2)
# q.enQueue(3)
# q.deQueue()
# q.enQueue(4)
# q.enQueue(5)
# l = q.printQueue()
# print(q.size())
# print(q.isEmpty())

