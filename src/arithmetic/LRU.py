
"""
LRU(Least Recently Used)最近最少使用算法
建立字典与双向链表的映射, 双向链表为字典的底层
时间复杂度为O(1)
"""


class Node:
    prev, next = None, None
    __k, __v = None, None

    def __init__(self, k: int, v: int):
        self.__k, self.__v = k, v

    def getV(self):
        return self.__v

    def getK(self):
        return self.__k

    def __str__(self) -> str:
        return "<"+str(self.__k)+", "+str(self.__v)+">"


class DoubleList:
    """含头节点和尾节点的双向链表"""
    __size = 0
    __head: Node = None
    __last: Node = None

    def __init__(self):
        self.__head = Node(0, 0)
        self.__last = self.__head

    def append(self, node: Node):
        """在表尾追加节点"""
        self.__last.next = node
        node.prev = self.__last
        self.__last = node
        self.__size += 1

    def removeFirst(self) -> Node:
        """删除第一个节点, 并返回节点"""
        if(self.__size == 0):
            return None
        p: Node = self.__head.next
        if(self.__size == 1):
            self.__head.next = None
        else:
            p.next.prev = self.__head
            self.__head.next = p.next
        self.__size -= 1
        return p

    def remove(self, node: Node):
        """删除指定Node, 要调用这个函数要保证node必然存在"""
        if(node.next == None):
            # 是最后一个节点
            node.prev.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        del node
        self.__size -= 1

    def size(self) -> int:
        return self.__size

    def traverse(self) -> list:
        p: Node = self.__head.next
        while(p):
            print(p, end="\t")
            p = p.next


class LRU:
    __map: dict = {}
    __list: DoubleList = None
    __capacity: int = 0

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__list = DoubleList()

    def get(self, key: int) -> int:
        if(not self.__map.__contains__(key)):
            return -1
        node: Node = self.__map[key]
        self.put(Node(key, node.getV()))
        return node.getV()

    def put(self, node: Node):
        """放到双链表的表尾, 也就是优先级高, 改映射"""
        if(self.__map.__contains__(node.getK())):
            # 如果map中包含key, 那么就移除<k, v>
            self.__list.remove(self.__map[node.getK()])
        elif(self.__capacity == self.__list.size()):
            # 如果满容量, 那么就移除表头
            first = self.__list.removeFirst()
            self.__map.pop(first.getK())
        # 加入表尾, 并添加映射
        self.__list.append(node)
        self.__map[node.getK()] = node

    def printMap(self):
        print(self.__map)

    def traverse(self):
        self.__list.traverse()
        print()


lru = LRU(5)
n1 = Node(1, 1)
n2 = Node(2, 2)
n3 = Node(3, 3)
n4 = Node(4, 4)
n5 = Node(5, 5)
n6 = Node(6, 6)
lru.put(n1)
lru.put(n2)
lru.put(n3)
lru.put(n4)
lru.put(n5)
lru.put(n6)
lru.traverse()
lru.get(3)
lru.traverse()
