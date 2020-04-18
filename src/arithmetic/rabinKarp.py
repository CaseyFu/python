"""字符串匹配算法"""
"""
Rabin-Karp算法, 利用自制的hash
缺点:hash冲突, 遇到相同hash的子串比如abc bac cba会对子串和模式串进行逐个字符比对,
比如, 主串acbbcabcabaccabcba, 模式串abc, 大约有10次hash冲突, 性能并不稳定
退化成BF(brute-force)算法, 整体效果比BF好, 时间复杂度O(n)
"""


def rabinKarp(string, pattern):
    """相互匹配就返回模式串在主串中的位置, 不匹配就返回-1"""
    sLen = len(string)
    pLen = len(pattern)
    stringHash = formulateHash(string[0:pLen])
    patternHash = formulateHash(pattern)
    for i in range(0, sLen-pLen+1):
        # 比较了hash之后再比较字符串是否相等, abc, acb, bac的hash相等
        if(stringHash == patternHash and compareString(i, string, pattern)):
            return i
        if(i < sLen-pLen):
            # 如果不是最后一趟, 更新主串从i到i+n的hash值
            stringHash = nextHash(string, stringHash, i, pLen)
    return -1


def formulateHash(string):
    """计算hash值, 把每个字母的ASCII码相加, 把a当作0, b当作1, c当作2, 依次类推"""
    # "abc"的hash为3
    hashcode = 0
    for i in range(0, len(string)):
        hashcode += (ord(string[i])-ord('a'))
    return hashcode


def nextHash(string, hashcode, i, n):
    hashcode -= (ord(string[i]) - ord('a'))
    hashcode += (ord(string[i+n]) - ord('a'))
    return hashcode


def compareString(i, string, pattern):
    """判断字符串是否相等"""
    return string[i:i+len(pattern)] == pattern


s = "aabcdsdsdfer"
pattern = "abc"
print(rabinKarp(s, pattern))
