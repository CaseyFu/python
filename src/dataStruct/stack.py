"""
栈的封装
"""

class Stack:

    __stack:list
    def __init__(self):
        self.__stack = []
    
    def push(self, val):
        self.__stack.append(val)
    
    def pop(self):
        return self.__stack.pop()
    
    def peek(self):
        return self.__stack[-1]

    def isEmpty(self):
        return False if len(self.__stack) else True

    def size(self):
        return len(self.__stack)
