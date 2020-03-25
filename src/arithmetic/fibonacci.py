
# 斐波拉契模块

# 打印第1到第n的斐波拉契数列[1,n]


def fibA(n):
    """打印第1到第n的斐波拉契数列[1,n]"""
    x, y = 0, 1
    for i in range(0, n, 1):
        print(y, end=" ")
        x, y = y, x+y
    print()


def fibB(n):
    # 打印第1到第n的斐波拉契数列[1,n]
    x, y = 0, 1
    for i in range(0, n, 1):
        x = x+y
        print(x, end="\t")
        y = x-y


def fibC(n):
    # 返回一个第1到第n的斐波拉契数列列表[1,n]
    arr = [0]*n
    arr[0], arr[1] = 1, 1
    for i in range(2, n, 1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr


def fibD(n):
    # 返回一个第1到第n的斐波拉契数列列表[1,n]
    arr = []
    x, y = 0, 1
    for i in range(0, n, 1):
        arr.append(y)
        x, y = y, x+y
    return arr


if(__name__ == "__main__"):
    print("本程序中运行")
