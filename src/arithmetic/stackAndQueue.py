

import sys
sys.path.append("..")
from dataStruct.stack import Stack
from dataStruct.queue import Queue

class StackToQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, val):
        """push进stack1"""
        self.stack1.push(val)

    def pop(self):
        self.peek()
        return self.stack2.pop()

    def peek(self):
        """stack1的元素push进stack2"""
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def isEmpty(self):
        return False if (not self.stack1.isEmpty() or not self.stack2.isEmpty()) else True

    def printQueue(self):
        while not self.isEmpty():
            print(self.pop(), end="\t")


class QueueToStack:
    stackTop = None

    def __init__(self):
        self.queue = Queue()

    def push(self, val):
        """记录最后push的元素为栈顶元素"""
        self.stackTop = val
        self.queue.enQueue(val)

    def pop(self):
        """将size - 1个元素先deQueue再enQueue"""
        size = self.queue.size()
        while size > 1:
            if size == 2:
                self.stackTop = self.queue.peek()
            self.queue.enQueue(self.queue.deQueue())
            size -= 1
        return self.queue.deQueue()

    def peek(self):
        return self.stackTop

    def isEmpty(self):
        return False if self.queue.size() else True

    def printStack(self):
        while not self.isEmpty():
            print(self.pop(), end="\t")


qts = QueueToStack()
qts.push(1)
qts.push(2)
qts.push(3)
print(qts.pop())
qts.push(4)
qts.push(5)
qts.printStack()
