import random
import keyword
import sys
import os
import math
import zlib
import re
# 导入整个模块
import arithmetic.fibonacci as FIB
# 导入一个模块的部分函数
from arithmetic.fibonacci import fibA
# 导入其它包的类
from xfk.myIterator import TestClass
import exception.error as error

# python练习手册
# sys.path.append('./')


def a():
    # 二维数组
    list = [[] for i in range(0, 3, 1)]
    list[0] = [1, 2, 3, 4, 5]
    list[1] = [1, 2, 3]
    list[2] = [1, 2, 3, 4]
    print(list)


def b():
    # dict
    d = {}  # 空字典
    d = {"a": 33, "b": 56, "c": 99}
    d["c"] = 100
    print(d.get("d", -1))


def c():
    # set
    s0 = set()  # 空集合
    s1 = set([1, 4, 2, 2, 3, 1, 4])
    s2 = {7, 4, 5, 6, 3, 5, 3}
    print(s1)
    print(s1 & s2)
    print(s1 | s2)
    print(s1 ^ s2)  # 交集的补集
    print(s1 - s2)


def d():
    # pass什么都不做, 占位
    i = 10
    if (i > 5):
        pass
    print(sys.platform)


def e(*num):
    # 可变参数*num, 可以有任意个参数, 如e()、e(1,2,3), 接受一个tuple
    for i in range(0, len(num), 1):
        print(num[i], end="  ")


def f(num, **kw):
    # 关键字参数**kw, 除了num之外传入任意键值对, 自动组装成dict, f(1, city="chongqing", prince="key")
    # 接收一个dict
    print(num, kw)
    if ("city" in kw):
        print("有城市")
    if ("princess" not in kw):
        print("没有princess")


def g(num, *, city, job="soft"):
    # 命名关键字, 限制键值对的名字, 初始化关键字
    print(city)
    print(job)


def h():
    # input
    i = input()
    print(i)


def i():
    # python保留关键字
    num = 1
    for i in keyword.kwlist:
        print(i, end="  ")
        if (num % 7 == 0):
            print()
        num += 1


def j():
    # 求幂
    print(2 ** 4)


def k():
    # 判断地址
    x = 2
    y = 3
    print(id(x))
    print(id(y))
    print(x is y)


def l():
    # map
    list = [1, 2, 3, 4]
    map()


def m():
    # 复数
    c = complex(2, 3)  # 表示复数2+3i
    print(abs(c))


def n():
    # 集合, 有序
    s = {7, 3, 8, 1, 9}
    print(s)


def o():
    # import
    # 导入其它包的模块
    # import arithmetic.fibonacci as FIB
    FIB.fibA(10)

    # 导入其它包的函数
    # from arithmetic.fibonacci import fibA
    # fibA(10)

    # 导入类
    # from xfk.myIterator import TestClass
    # 模块名小写、类名大写
    i = TestClass()
    for j in iter(i):
        print(j)


def p():
    """repr、rjust"""
    for i in range(1, 11, 1):
        print(repr(i).rjust(0), repr(i * i).center(1), repr(i * i * i).rjust(2))

    for i in range(1, 11, 1):
        print("{0:2d} {1:3d} {2:4d}".format(i, i * i, i * i * i))


def q():
    n = 1
    while (r(n) < 1000):
        n += 1
    print("不超过1000的最大n值为:", n - 1)


def r(n):
    num = 0
    for i in range(1, n + 1, 1):
        num += i ** 2
    return num


def s():
    arr = [1, 2, 3, 4]
    x = list(arr)
    for i in x:
        print(i)


def t(n):
    """yield存储当前变量,返回一个迭代器执行next()的时候+1"""
    a, b, counter = 0, 1, 0
    while (counter <= n):
        yield a
        a, b = b, a + b
        counter += 1


def u():
    """列表推导式"""
    matrix = [
        [1, 2, 3, 4, 5],
        [5, 6, 7, 8, 6],
        [9, 1, 2, 3, 7]
    ]
    # t = [[row[i] for row in matrix] for i in range(4)]
    # t = []
    # for i in range(0, 5, 1):
    #     t.append([row[i] for row in matrix])
    # del matrix[0][0]
    print(matrix[0][:])


def v():
    """list、tuple、set、dict"""
    # t = 123, "321", 1.2  # tuple
    # s1 = {1, 2, 3}  # set
    # s2 = {2, 3, 4}
    # d = {}  # 空字典
    # print(s1 ^ s2)  # 交集的补集
    # d1 = {"a": 1, "b": 2, "c": 3}  # 遍历dict
    # for k, v in d1.items():
    #     print(k, v)
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 7, 6, 6, 4]
    # for x, y in zip(list1, list2): # zip函数
    #     print("first is {0} and second is {1}.".format(x, y))
    it = iter(list2)
    for i in sorted(it):
        print(i)


def w():
    """格式化输出"""
    s = "xfk"
    a = 1.23
    print("十进制:{3:d} 二进制:{0:b} 八进制:{1:o} 十六进制:{2:x}".format(15, 15, 15, 15))
    print("my name is {0} and the fraction is {1:.3f}.".format(s, a))
    print("my name is %s and the fraction is %.2f." % (s, a))


def x():
    """异常"""
    i, j = 1, 0
    try:
        i = i / j
    except Exception as e:
        print(e)
    else:
        print("ok")
    finally:
        print("end")
    s = "i just want to fock you sh0t good"
    if (s.find("fuck") != -1):
        raise error.DirtyError("your words including f**k")
    if (s.find("shit") != -1):
        raise error.DirtyError("your words including s**t")
    if (s.find("good") != -1):
        raise error.MoralError("excellent")


def y():
    """assert, 相当于continue的作用, 满足则执行, 不满足则raise异常"""
    s = "abcdef"
    assert ("g" in s)
    print("hhhh")


def z():
    name = "I LOVE YOU"
    for x in range(0, len(name)):
        c = name[x]
        c = c.upper()
        if (c == "A"):
            print("..######..\n..#....#..\n..######..", end=" ")
            print("\n..#....#..\n..#....#..\n\n")
        elif (c == "B"):
            print("..######..\n..#....#..\n..#####...", end=" ")
            print("\n..#....#..\n..######..\n\n")
        elif (c == "C"):
            print("..######..\n..#.......\n..#.......", end=" ")
            print("\n..#.......\n..######..\n\n")
        elif (c == "D"):
            print("..#####...\n..#....#..\n..#....#..", end=" ")
            print("\n..#....#..\n..#####...\n\n")
        elif (c == "E"):
            print("..######..\n..#.......\n..#####...", end=" ")
            print("\n..#.......\n..######..\n\n")
        elif (c == "F"):
            print("..######..\n..#.......\n..#####...", end=" ")
            print("\n..#.......\n..#.......\n\n")
        elif (c == "G"):
            print("..######..\n..#.......\n..#.####..", end=" ")
            print("\n..#....#..\n..#####...\n\n")
        elif (c == "H"):
            print("..#....#..\n..#....#..\n..######..", end=" ")
            print("\n..#....#..\n..#....#..\n\n")
        elif (c == "I"):
            print("..######..\n....##....\n....##....", end=" ")
            print("\n....##....\n..######..\n\n")
        elif (c == "J"):
            print("..######..\n....##....\n....##....", end=" ")
            print("\n..#.##....\n..####....\n\n")
        elif (c == "K"):
            print("..#...#...\n..#..#....\n..##......", end=" ")
            print("\n..#..#....\n..#...#...\n\n")
        elif (c == "L"):
            print("..#.......\n..#.......\n..#.......", end=" ")
            print("\n..#.......\n..######..\n\n")
        elif (c == "M"):
            print("..#....#..\n..##..##..\n..#.##.#..", end=" ")
            print("\n..#....#..\n..#....#..\n\n")
        elif (c == "N"):
            print("..#....#..\n..##...#..\n..#.#..#..", end=" ")
            print("\n..#..#.#..\n..#...##..\n\n")
        elif (c == "O"):
            print("..######..\n..#....#..\n..#....#..", end=" ")
            print("\n..#....#..\n..######..\n\n")
        elif (c == "P"):
            print("..######..\n..#....#..\n..######..", end=" ")
            print("\n..#.......\n..#.......\n\n")
        elif (c == "Q"):
            print("..######..\n..#....#..\n..#.#..#..", end=" ")
            print("\n..#..#.#..\n..######..\n\n")
        elif (c == "R"):
            print("..######..\n..#....#..\n..#.##...", end=" ")
            print("\n..#...#...\n..#....#..\n\n")
        elif (c == "S"):
            print("..######..\n..#.......\n..######..", end=" ")
            print("\n.......#..\n..######..\n\n")
        elif (c == "T"):
            print("..######..\n....##....\n....##....", end=" ")
            print("\n....##....\n....##....\n\n")
        elif (c == "U"):
            print("..#....#..\n..#....#..\n..#....#..", end=" ")
            print("\n..#....#..\n..######..\n\n")
        elif (c == "V"):
            print("..#....#..\n..#....#..\n..#....#..", end=" ")
            print("\n...#..#...\n....##....\n\n")
        elif (c == "W"):
            print("..#....#..\n..#....#..\n..#.##.#..", end=" ")
            print("\n..##..##..\n..#....#..\n\n")
        elif (c == "X"):
            print("..#....#..\n...#..#...\n....##....", end=" ")
            print("\n...#..#...\n..#....#..\n\n")
        elif (c == "Y"):
            print("..#....#..\n...#..#...\n....##....", end=" ")
            print("\n....##....\n....##....\n\n")
        elif (c == "Z"):
            print("..######..\n......#...\n.....#....", end=" ")
            print("\n....#.....\n..######..\n\n")
        elif (c == " "):
            print("..........\n..........\n..........", end=" ")
            print("\n..........\n\n")
        elif (c == "."):
            print("----..----\n\n")


def aa():
    """filter"""
    l = [1, 2, 3, 4, 5, 6, 7, 12, 5, 24]
    l2 = list(filter(lambda i: i > 10, range(1, 12)))
    print(l2)


def ab():
    """正则表达式获取文件名、文件后缀"""
    fileName = "\\11.xfk\\xfk.min.txt"
    pattern = re.compile(r'.*[/\\](.+)\.(.+)$')
    matcher = pattern.match(fileName)
    if(matcher):
        print(matcher.group(2))
    else:
        print("匹配不成功")


def ac():
    path = "./xfkc"  # 如果目录不存在就返回False
    if(not os.path.exists(path)):
        os.makedirs(path)

if __name__ == "__main__":
    ac()