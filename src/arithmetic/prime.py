import math


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


def prime(val):
    """判断素数、质数"""
    i = 2
    while(i <= math.sqrt(val)):
        if(val % i == 0):
            break
        i += 1
    else:
        print("%d是素数" % (val))
        return
    print("%d不是素数" % (val))


if(__name__ == "__main__"):
    prime(8)
else:
    print("素数")
