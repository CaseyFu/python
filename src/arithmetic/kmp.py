"""
KMP算法
master =  GTGTGAGCTGGTGTGTGCFAA
pattern = GTGTGCF
坏字符前缀GTGTG
最长可匹配后缀GTG
最长可匹配前缀GTG
next[]
下标:已匹配前缀的下一个位置
值:最长可匹配前缀的下一个位置
1. 对模式串尽心预处理, 生成next[]

"""
master = "GTGTGAGCTGGTGTGTGCFAA"
pattern = "GTGTGCF"


def kmp(master, pattern):
    next = genNext(pattern)
    print("生成的next[]:", next)
    j = 0
    for i in range(0, len(master)):
        while(j > 0 and master[i] != pattern[j]):
            j = next[j]
        if(master[i] == pattern[j]):
            j += 1
        if(j == len(pattern)):
            return i-len(pattern)+1
    return -1


def genNext(pattern):
    next = [0]*len(pattern)
    j = 0
    for i in range(2, len(pattern)):
        while(j != 0 and pattern[j] != pattern[i-1]):
            j = next[j]
        if(pattern[j] == pattern[i-1]):
            j += 1
        next[i] = j
    return next


print(kmp(master, pattern))

# 1.   ↓
# GTGTGAGCTGGTGTGTGCFAA
# GTGTGCF
# 2.   ↓
# GTGTGAGCTGGTGTGTGCFAA
#   GTGTGCF
# 3.   ↓
# GTGTGAGCTGGTGTGTGCFAA
#     GTGTGCF
# 4.   ↓
# GTGTGAGCTGGTGTGTGCFAA
#      GTGTGCF
# 5.     ↓
# GTGTGAGCTGGTGTGTGCFAA
#       GTGTGCF
# 6.     ↓
# GTGTGAGCTGGTGTGTGCFAA
#        GTGTGCF
# 7.      ↓
# GTGTGAGCTGGTGTGTGCFAA
#         GTGTGCF
# 8.        ↓
# GTGTGAGCTGGTGTGTGCFAA
#          GTGTGCF
# 9.             ↓
# GTGTGAGCTGGTGTGTGCFAA
#           GTGTGCF
# 10.                ↓
# GTGTGAGCTGGTGTGTGCFAA
#             GTGTGCF
