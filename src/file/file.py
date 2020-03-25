import pickle


def testWrite():
    """写文件"""
    f = open("f:/test.txt", "w", 1024, "UTF-8")
    f.write("写一写东西\n第二行")
    f.close()


def testRead():
    """写文件"""
    try:
        f = open("f:/test.txt", "r", 1024, "UTF-8")
    except FileNotFoundError:
        print("文件不存在")
    else:
        str = f.read()
        print(str)
    finally:
        f.close()


def testPickle():
    """序列化对象"""
    d = {
        "arr": [1, 1.2, "3", "hhh", "汉字"],
        "tup": (1, 3, "h"),
        "set": {1, 2, "hhhh"},
        "nul": None
    }
    f = open("f:/data.pkl", "wb")
    pickle.dump(d, f)
    f.close()


def testRePickle():
    """反序列化对象"""
    f = open("f:/data.pkl", "rb")
    data = pickle.load(f)
    print(data)
    f.close()


if(__name__ == "__main__"):
    testRead()
