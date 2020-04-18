import math
"""
round()四舍五入
ceil()向上取整
floor()向下取整
int()向下取整
素数,质数,prime,指的是:数n不能被[2,n-1]之间数整除
for(int i=2; i<=floor(sqrt(n)); i++)
"""


def prime(n):
    """[3,n]的素数"""
    for i in range(3, n+1, 1):
        j = 2
        while(j <= math.sqrt(i)):
            if(i % j == 0):
                break
            j += 1
        else:
            # 素数
            print(i, end=" ")


def prime():
    """判断素数、质数"""
    val = eval(input("输入一个数:"))
    i = 2
    while(i <= math.sqrt(val)):
        if(val % i == 0):
            break
        i += 1
    else:
        print("%d是素数" % (val))
        return
    print("%d不是素数" % (val))


prime()
