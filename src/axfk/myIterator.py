class TestClass:
    """一个自己写的测试迭代器类"""

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if(self.a <= 20):
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


if(__name__ == "__main__"):
    myClass = TestClass()
    for i in iter(myClass):
        print(i)
