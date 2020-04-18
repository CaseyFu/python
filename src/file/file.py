import pickle
import os
import sys


def writeOrdinary():
    """写文件"""
    with open("f:/test.txt", "w", 1024, "UTF-8") as f:
        f.write("写一写东西\n第二行")


def readOrdinary():
    """读文件"""
    with open("f:/test.txt", "r", 1024, "UTF-8") as f:
        str = f.read()
        print(str)


def pickleSerialize():
    """序列化对象, 对象-->文本"""
    d = {
        "arr": [1, 1.2, "3", "hhh", "汉字"],
        "tup": (1, 3, "h"),
        "set": {1, 2, "hhhh"},
        "nul": None
    }
    with open("f:/data.pkl", "wb") as f:
        pickle.dump(d, f)


def pickleDeserialize():
    """反序列化对象, 文本-->对象"""
    with open("f:/data.pkl", "rb") as f:
        data = pickle.load(f)
        print(data)


def t():
    with open(os.path.dirname(__file__)+"\\xfk.txt", "r", 1024, "UTF-8") as f:
        s = f.read()
        print(s)


# pickleSerialize()
# pickleDeserialize()
input("输入学号")
input("输入学号")
