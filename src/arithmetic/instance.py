import datetime
import calendar
import unicodedata
import math
import cmath
import random


def testSqrt():
    """平方根"""
    number = -4
    if(number >= 0):
        print(math.sqrt(number))
    else:
        c = cmath.sqrt(number)
        print("%.2f + %.2fj" % (c.real, c.imag))
        print(complex(c.real, c.imag))


def testEquation():
    """一元二次方程"""
    a, b, c = 1.0, 0.0, 1.0
    beta = b*b - 4*a*c
    print("<|=", beta)
    if(beta >= 0):
        r1 = (-b+math.sqrt(beta))/(2*a)
        r2 = (-b-math.sqrt(beta))/(2*a)
        print("r1=", r1)
        print("r2=", r2)
    else:
        alpha = -b/(2*a)
        r = cmath.sqrt(beta)/(2*a)
        print(complex(r.real, (-1)*r.imag))
        print(complex(r.real, r.imag))


def tripleArea():
    x, y, z = 3.0, 3.0, 3.0
    if(x+y <= z or x+z <= y or z+y <= x):
        print("不能构成三角形")
        return
    else:
        s = (x+y+z)/2
        area = (s*(s-x)*(s-y)*(s-z))**0.5
        print(area)


def circleArea():
    r = 1
    print(math.pi*r*r)


def randomNum():
    a = b = c = d = 0
    for i in range(0, 100, 1):
        i = random.randint(1, 4)
        if(i == 1):
            a += 1
        elif(i == 2):
            b += 1
        elif(i == 3):
            c += 1
        else:
            d += 1
    print("A:", a/100.0)
    print("B:", b/100.0)
    print("C:", c/100.0)
    print("D:", d/100.0)


def verdictNumber():
    val = "一十一二"
    try:
        float(val)
    except Exception:
        pass

    try:
        import unicodedata
        for i in val:
            unicodedata.numeric(i)
        print("是数字")
        return
    except Exception:
        pass
    print("不是数字")


def oddAndEven():
    val = 1.0
    assert ("int" in str(type(val))), "非整数异常"
    print("奇数" if(val & 1) else "偶数")


def leapYear():
    year = 2000
    if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        print("leapYear")
    else:
        print("not leapYear")


def multiplyTable():
    for i in range(1, 10, 1):
        for j in range(1, i+1, 1):
            print("%dx%d=%d" % (j, i, i*j), end="\t")
        print()


def narcissus():
    """153=1**3 + 5**3 + 3**3"""
    for i in range(1, 1000, 1):
        times = len(str(i))
        num = 0
        t = i
        for j in range(0, times, 1):
            num += (i % 10)**times
            i //= 10
        if(num == t):
            print(t)


def baseTransfer():

    val = 17
    # 二进制
    result = []
    data = val
    while(data):
        result.append(data % 2)
        data //= 2
    result.reverse()
    print("二进制", result)
    result.clear()
    # 八进制
    # 12/8 = 1...4
    # 1/8 = 0...1
    data = val
    while(data):
        result.append(data % 8)
        data //= 8
    result.reverse()
    print("八进制", result)
    result.clear()

    data = val
    while(data):
        t = data % 16
        if(t == 10):
            result.append("A")
        elif(t == 11):
            result.append("B")
        elif(t == 12):
            result.append("C")
        elif(t == 13):
            result.append("D")
        elif(t == 14):
            result.append("E")
        elif(t == 15):
            result.append("F")
        else:
            result.append(t)
        data //= 16
    result.reverse()
    print("十六进制", result)
    result.clear()


def charToAscII():
    val = 'a'
    i = 65
    print(ord(val))
    print(chr(i))


def maxRestrition2():
    """最大公约数, 辗转相除法"""
    x, y = 24, 54
    while(y != 0):
        x, y = y, x % y
    print(x)


def maxRestrition3():
    """最大公约数, 相减术"""
    x, y = 54, 24
    while(x != y):
        x, y = min(x, y), abs(x-y)
    print(y)


def minMultiple():
    """最小公倍数, 乘积/最大公约数"""
    x, y = 54, 24
    m = x*y
    while(y):
        x, y = y, x % y
    print(m//x)


def testCalendar():
    year = 2020
    month = 4
    print(calendar.month(year, month))


def fib(n):
    if(n <= 1):
        return n
    else:
        return fib(n-1)+fib(n-2)


def josefu():
    l = list(range(1, 31))
    leave = []
    num = 1
    index = num - 1
    print(l)
    while(len(leave) != 15):
        if(index == len(l)):
            index = 0
        if(num == 9):
            leave.append(l[index])
            l.remove(l[index])
            num = 1
        else:
            num += 1
            index += 1
    print(leave)


def four():
    list1 = [[x, y, z]for x in range(1, 21)for y in range(
        1, 34)for z in range(1, 100)if(x+y+z == 100 and z % 3 == 0 and 5*x+3*y+z/3 == 100)]
    print(list1)


four()
