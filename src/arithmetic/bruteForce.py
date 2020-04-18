"""
暴力字符串匹配
缺点:主串aaaaaaaaaaaaabb, 模式串abb, 效率太低
"""


def bruteForce(string, pattern):
    for i in range(0, len(string)):
        if(string[i] == pattern[0]):
            isSubstr = True
            for j in range(1, len(pattern)):
                if(string[i+j] != pattern[j]):
                    isSubstr = False
                    break
            if(isSubstr):
                return i
    return -1


string = "aaaab"
pattern = "ac"
print(bruteForce(string, pattern))
