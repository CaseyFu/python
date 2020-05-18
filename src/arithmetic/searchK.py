"""
寻找无序数组中第k大的数
1. 排序法, 把数组排序后寻找
2. 插入法, 维护一个长度为k的有序数组, 遍历无序数组加入元素, 最后一个元素为第k大
3. 最小堆法, 维护一个长度为k的最小堆, 堆顶为第k大
4. 分治法
"""


# def heapDownAdjust(arr, parentIndex, length):
#     val = arr[parentIndex]
#     childIndex = 2*parentIndex+1
#     while(childIndex < length):
#         if(childIndex+1 < length and arr[childIndex+1] < arr[childIndex]):
#             childIndex += 1
#         if(val <= arr[childIndex]):
#             break
#         arr[parentIndex] = arr[childIndex]
#         parentIndex = childIndex
#         childIndex = 2*parentIndex+1
#     arr[parentIndex] = val


# def buildMinHeap(arr, length):
#     """构建大小为length的堆"""
#     for i in range((length-2) >> 1, -1, -1):
#         heapDownAdjust(arr, i, length)
#     print(arr)


# def searchK(arr, k):
#     """寻找无序数组的第k大元素"""
#     if(k <= 0 or k > len(arr)):
#         return
#     buildMinHeap(arr, k)  # 原地生成有k个元素的堆
#     # buildMinHeap(arr, arr.length) [0,arr.length-1]
#     # buildMinHeap(arr, k) [0, k-1]
#     for i in range(k, len(arr)):
#         if(arr[0] < arr[i]):
#             arr[0] = arr[i]
#             heapDownAdjust(arr, 0, k)
#     print("第k大:", arr[0])


def downAdjust(arr, parentIndex, length):
    val = arr[parentIndex]
    childIndex = 2*parentIndex + 1
    while(childIndex < length):
        if(childIndex+1 < length and arr[childIndex+1] < arr[childIndex]):
            childIndex += 1
        if(arr[childIndex] >= val):
            break
        arr[parentIndex] = arr[childIndex]
        parentIndex = childIndex
        childIndex = 2*parentIndex+1
    arr[parentIndex] = val


def searchK(arr, k):
    if(k <= 0 or k > len(arr)):
        return
    for i in range((len(arr)-2) >> 1, -1, -1):
        downAdjust(arr, i, k)
    for i in range(k, len(arr)):
        if(arr[0] < arr[i]):
            arr[0] = arr[i]
            downAdjust(arr, 0, k)
    print(arr[0])


arr = [5, 0, 1, 8, 2, 4, 6, 3, 7, 9]
# arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# buildMinHeap(arr, 4)
searchK(arr, 11)
