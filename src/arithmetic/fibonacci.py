
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
    """返回一个第1到第n的斐波拉契数列列表[1,n]"""
    arr = [0]*n
    arr[0], arr[1] = 1, 1
    for i in range(2, n, 1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr


def fibC(n):
    if(n == 1 or n == 2):
        return 1
    return fibC(n-1) + fibC(n-2)


print(list(fibC(i)for i in range(1, 21)))
