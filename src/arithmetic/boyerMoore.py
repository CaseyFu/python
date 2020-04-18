"""
BM字符串匹配算法
[好字符规则]:待学习
[坏字符规则]:主串与模式串不匹配的字符
"""


def searchBadInPattern(pattern, c, i):
    """[i-->0)返回字符c在pattern中的位置, c不存在返回-1"""
    # [0, i-1]会产生死循环
    for j in range(i-1, -1, -1):
        if(pattern[j] == c):
            return j
    return -1


def bmBad(string, pattern):
    """坏字符规则"""
    sLen, pLen, start = len(string), len(pattern), 0
    while(start < sLen-pLen+1):
        # 从后往前找坏字符, i记录坏字符在主串的位置
        for i in range(pLen-1, -2, -1):
            if(pattern[i] != string[start+i]):
                break
        if(i < 0):
            # 没有找到坏字符, 匹配成功
            return start
        # 寻找坏字符再模式串中的位置
        badIndex = searchBadInPattern(pattern, string[start+i], i)
        start += i+1 if badIndex == -1 else i-badIndex
    return -1


s = "adsdacsdfer"
pattern = "abc"
print(bmBad(s, pattern))
# 1.
# adsdabcsdfer
# dadc
# 2.
# adsdabcsdfer
#         dadc
# 3.
# adsdabcsdfer
#     abc
