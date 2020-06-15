import sys
sys.path.append("..")
from dataStruct.deque import Deque

"""
单调队列的应用
滑窗的最大值
[1, 3, -1], -3, 5, 3, 6, 7		3
1, [3, -1, -3], 5, 3, 6, 7		3
1, 3, [-1, -3, 5], 3, 6, 7		5
1, 3, -1, [-3, 5, 3], 6, 7		5
1, 3, -1, -3, [5, 3, 6], 7		6
1, 3, -1, -3, 5, [3, 6, 7]		7

"""

class MonoQueue:
    """单调队列, 对头元素用于最大"""
    __deque:Deque = None
    def __init__(self):
        self.__deque = Deque()

    def push(self, val):
        while(not self.__deque.isEmpty() and self.__deque.peek_tail() < val):
            self.__deque.deDeque_tail()
        self.__deque.enDeque_tail(val)
    
    def getMax(self):
        """对头元素就是最大"""
        return self.__deque.peek_head()

    def pop(self, val):
        if(not self.__deque.isEmpty() and self.__deque.peek_head() == val):
            self.__deque.deDeque_head()
        


class MaxSlidingWindow:
    """滑动窗口, 返回每次窗口最大值"""
    __window:MonoQueue = None
    def __init__(self):
        self.__window = MonoQueue()

    def execute(self, arr:list, size:int):
        result:list = []
        for i in range(len(arr)):
            if(i<size-1):
                self.__window.push(arr[i])
            else:
                self.__window.push(arr[i])
                result.append(self.__window.getMax())
                self.__window.pop(arr[i-size+1])
        return result



win = MaxSlidingWindow()
arr = win.execute([1, 3, -1, -3, 5, 3, 6, 7	], 3)
print(arr)