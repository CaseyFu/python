import sys
sys.path.append("../")
from dataStruct.stack import Stack

"""单调栈"""


class MonoStack:
    def __init__(self):
        pass

    def nextGreaterElement(self, arr: list):
        """
        右边第一个比元素大的值
        [2, 1, 2, 4, 3]返回结果[4, 2, 4, -1, -1]
        从左到右:
        比2大的第一个为4
        比1大的第一个为2
        比2大的第一个为4
        比4大的第一个没有-1
        比3大的第一个没有-1
        时间复杂度: O(n)
        """
        result: list = [None]*len(arr)
        stack = Stack()
        for i in range(len(arr)-1, -1, -1):
            while(not stack.isEmpty() and stack.peek() <= arr[i]):
                stack.pop()
            result[i] = stack.peek() if not stack.isEmpty() else -1  # 这里stack[-1]为右边第一个最大值
            stack.push(arr[i])  # 值入栈
        return result

    def prevGreaterElement(self, arr: list):
        """
        左边第一个比元素大的值
        [2, 1, 2, 4, 3]返回结果[-1, 2, -1, -1, 4]
        """
        result: list = [None]*len(arr)
        stack = Stack()

        for i in range(len(arr)):
            while(not stack.isEmpty() and stack.peek() <= arr[i]):
                stack.pop()
            result[i] = stack.peek() if not stack.isEmpty() else -1
            stack.push(arr[i])
        return result

    def nextGreaterGap(self, arr: list):
        """
        [2, 1, 2, 4, 3]返回结果[3, 1, 1, 0, 0]
        从左到右:
        比2大的为右边第3个
        比1大的为右边第1个
        比2大的为右边第1个
        比4大的为右边第0个, 即没有
        比3大的为右边第0个, 即没有
        """
        result: list = [None]*len(arr)
        stack = Stack()
        for i in range(len(arr)-1, -1, -1):
            while(not stack.isEmpty() and arr[stack.peek()] <= arr[i]):  # 操作索引
                stack.pop()
            # 这里stack[-1]为右边第一个最大值的索引
            result[i] = stack.peek()-i if not stack.isEmpty() else 0
            stack.push(i)  # 索引入栈
        return result

    def prevGreaterGap(self, arr: list):
        """
        左边第一个最大元素的距离
        [2, 1, 2, 4, 3]返回结果[0, 1, 0, 0, 1]
        """
        result: list = [None]*len(arr)
        stack = Stack()
        for i in range(len(arr)):
            while(not stack.isEmpty() and arr[stack.peek()] <= arr[i]):
                stack.pop()
            result[i] = i-stack.peek() if not stack.isEmpty() else 0
            stack.push(i)
        return result

    def clockwiseNextGreaterElement(self, arr: list):
        """
        循环数组下的, 右边最大元素, 即顺时针方向的第一个最大元素
        [2, 1, 2, 4, 3]返回结果[4, 2, 4, -1, 4]
        """
        result: list = [None]*len(arr)
        stack = Stack()
        n: int = len(arr)
        # 假设数组长度*2, 使用%, 其实还是一倍长
        for i in range(2*len(arr)-1, -1, -1):
            while(not stack.isEmpty() and stack.peek() <= arr[i % n]):
                stack.pop()
            result[i % n] = stack.peek() if not stack.isEmpty() else -1
            stack.push(arr[i % n])
        return result

    def anticlockwiseNextGreaterElement(self, arr: list):
        """
        循环数组下的, 左边最大元素, 即逆时针方向的第一个最大元素
        [2, 1, 2, 4, 3]返回结果[3, 2, 3, -1, 4]
        """
        result: list = [None]*len(arr)
        stack = Stack()
        n = len(arr)
        for i in range(len(arr)*2):
            while(not stack.isEmpty() and stack.peek() <= arr[i % n]):
                stack.pop()
            result[i % n] = stack.peek() if not stack.isEmpty() else -1
            stack.push(arr[i % n])
        return result


monoStack = MonoStack()
next = monoStack.anticlockwiseNextGreaterElement([2, 1, 2, 4, 3])
print(next)

