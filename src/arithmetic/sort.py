

def bubbleSort(arr):
    # 冒泡排序
    lastIndex = len(arr) - 1
    length = len(arr) - 1
    for i in range(0, len(arr)-1, 1):
        sorted = True
        for j in range(0, length, 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                lastIndex = j
                sorted = False
        length = lastIndex
        if sorted:
            break
    print("冒泡排序结果: ", "\n", arr)


def insertSort(arr):
    # 插入排序
    for i in range(1, len(arr), 1):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            if arr[j] > val:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j+1] = val
    print("插入排序结果: ", "\n", arr)


def selectSort(arr):
    # 选择排序
    for i in range(0, len(arr)-1, 1):
        val = i
        for j in range(i+1, len(arr), 1):
            if arr[j] < arr[val]:
                val = j
        if val != i:
            temp = arr[val]
            arr[val] = arr[i]
            arr[i] = temp
    print("选择排序结果: ", "\n", arr)


# 堆排序结点下沉
def nodeDownAdjust(arr, parentIndex, length):
    val = arr[parentIndex]
    childIndex = 2*parentIndex + 1
    while childIndex < length:
        if childIndex+1 < length and arr[childIndex+1] > arr[childIndex]:
            childIndex += 1
        if val >= arr[childIndex]:
            break
        arr[parentIndex] = arr[childIndex]
        parentIndex = childIndex
        childIndex = 2*parentIndex+1
    arr[parentIndex] = val


# 堆排序
def heapSort(arr):
    # 构建最大堆
    for i in range((len(arr)-2) >> 1, -1, -1):
        nodeDownAdjust(arr, i, len(arr)-1)
    # 排序
    for i in range(len(arr)-1, 0, -1):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        nodeDownAdjust(arr, 0, i)
    print("堆排序结果: ", "\n", arr)


def mergeLinkA(left, right):
    temp = []
    i = 0
    j = 0
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    while(i < len(left)):
        temp.append(left[i])
        i += 1

    while(j < len(right)):
        temp.append(right[j])
        j += 1
    return temp


def mergeSortA(arr, left, right):
    # 归并排序
    if left == right:
        temp = [arr[left]]
        return temp
    mid = (left+right) >> 1
    leftArr = mergeSortA(arr, left, mid)
    rightArr = mergeSortA(arr, mid+1, right)
    return mergeLinkA(leftArr, rightArr)


def mergeLinkB(arr, left, mid, right):
    temp = []
    lStart = left
    rStart = mid + 1
    while(lStart < mid+1 and rStart < right+1):
        if(arr[lStart] < arr[rStart]):
            temp.append(arr[lStart])
            lStart += 1
        else:
            temp.append(arr[rStart])
            rStart += 1
    while(lStart < mid+1):
        temp.append(arr[lStart])
        lStart += 1
    while(rStart < right+1):
        temp.append(arr[rStart])
        rStart += 1
    for i in range(0, len(temp), 1):
        arr[i+left] = temp[i]


def mergeSortB(arr, left, right):
    if(left == right):
        return
    mid = (left+right) >> 1
    mergeSortB(arr, left, mid)
    mergeSortB(arr, mid+1, right)
    mergeLinkB(arr, left, mid, right)


def doMergeSort(arr):
    print("返回数组归并排序结果", mergeSortA(arr, 0, len(arr)-1))
    print("未排序", arr)
    mergeSortB(arr, 0, len(arr)-1)
    print("无返回类型归并排序结果", arr)


def divide(arr, left, right):
    val = arr[left]
    while(left < right):
        while(left < right and arr[right] >= val):
            right -= 1
        arr[left] = arr[right]
        while(left < right and arr[left] <= val):
            left += 1
        arr[right] = arr[left]
    arr[left] = val
    return left


def quickSort(arr, left, right):
    # 快排
    if(left >= right):
        return
    mid = divide(arr, left, right)
    quickSort(arr, left, mid-1)
    quickSort(arr, mid+1, right)


def countSortA(arr):
    # 计数排序, 只适用于整数, 不稳定版本
    max = 0
    min = 0
    for i in arr:
        if(i > max):
            max = i
        if(i < min):
            min = i
    countArr = [0]*(max-min+1)
    for i in range(0, len(arr), 1):
        countArr[arr[i]-min] += 1

    index = 0
    for i in range(0, len(countArr), 1):
        while(countArr[i] != 0):
            arr[index] = i+min
            index += 1
            countArr[i] -= 1
    print(arr)


def countSortB(arr):
    # 计数排序, 只适用于整数, 稳定版本
    max = 0
    min = 0
    for i in arr:
        if(i > max):
            max = i
        if(i < min):
            min = i
    countArr = [0]*(max-min+1)
    for i in range(0, len(arr), 1):
        countArr[arr[i]-min] += 1

    for i in range(1, len(countArr), 1):
        countArr[i] += countArr[i-1]

    temp = [0]*len(arr)
    for i in range(0, len(arr), 1):
        countArr[arr[i]-min] -= 1
        temp[countArr[arr[i]-min]] = arr[i]
    print(temp)


def getCharAsciiNumber(str, i):
    if(i < 0 or i >= len(str)):
        return 48
    return ord(str[i])


def radixSortNumber(arr):
    # 基数排序, 排序字符串, 数字版0(48), 9(57)
    offset = 48
    maxLen = 0
    for i in arr:
        if(len(i) > maxLen):
            maxLen = len(i)
    print("maxLen:", maxLen)
    for i in range(maxLen-1, -1, -1):
        countArr = [0]*10
        for j in range(len(arr)-1, -1, -1):
            index = getCharAsciiNumber(arr[j], i)
            countArr[index-offset] += 1

        for j in range(1, len(countArr), 1):
            countArr[j] += countArr[j-1]

        temp = [None]*len(arr)
        for j in range(len(arr)-1, -1, -1):
            index = getCharAsciiNumber(arr[j], i)
            countArr[index-offset] -= 1
            temp[countArr[index-offset]] = arr[j]
        arr = temp.copy()
    print(arr)


def getCharAsciiString(str, i):
    if(i < 0 or i >= len(str)):
        return 0
    return ord(str[i])


def radixSortString(arr):
    maxLen = 0
    for i in range(0, len(arr), 1):
        if(len(arr[i]) > maxLen):
            maxLen = len(arr[i])

    for i in range(maxLen-1, -1, -1):
        countArr = [0]*128
        for j in range(0, len(arr), 1):
            index = getCharAsciiString(arr[j], i)
            countArr[index] += 1
        for j in range(1, len(countArr), 1):
            countArr[j] += countArr[j-1]
        temp = [None]*len(arr)
        for j in range(len(arr)-1, -1, -1):
            index = getCharAsciiString(arr[j], i)
            countArr[index] -= 1
            temp[countArr[index]] = arr[j]
        arr = temp.copy()

    for i in range(0, len(arr), 1):
        print(arr[i], end="  ")


def bucketSort(arr, bucketNum):
    # 桶排序, 调用快排, 适合浮点数密集的群体
    maxValue = arr[0]
    minValue = arr[0]
    for i in range(0, len(arr), 1):
        if(arr[i] > maxValue):
            maxValue = arr[i]
        if(arr[i] < minValue):
            minValue = arr[i]

    # 根据桶计算元素区间
    rangeOfElement = (maxValue - minValue)/bucketNum
    span = minValue
    print("元素区间:", rangeOfElement)
    for i in range(0, bucketNum, 1):
        print("%d区间:[%.2f, %.2f)" % (i, span, span+rangeOfElement))
        span += rangeOfElement

    # 初始化列表
    list = [[]for i in range(0, bucketNum, 1)]
    for i in range(0, len(list), 1):
        list[i] = []

    # 放入元素
    for i in range(0, len(arr), 1):
        index = int((arr[i]-minValue)*(bucketNum-1)/(maxValue-minValue))
        list[index].append(arr[i])

    # 调用快排进行排序
    for i in range(0, len(list), 1):
        quickSort(list[i], 0, len(list[i])-1)

    # 打印
    for i in range(0, len(list), 1):
        for j in range(0, len(list[i]), 1):
            print("%.2f" % list[i][j], end="  ")


def test(arr):
    print("我"+"A")


if __name__ == "__main__":
    arr = [9, 3, 7, 1, 8, 5, 0, 6, 2, 4]
    flo = [9.2, 3.5, 7.1, 1.2, 8.65, 5.77, 0.6, 6.8, 2.3, 4.12]
    strNumber = ["139", "187", "152", "110"]
    strString = ["bc", "abcd", "ab", "xyz"]
    temp = []
    # bubbleSort(arr)
    # insertSort(arr)
    # selectSort(arr)
    # heapSort(arr)
    # doMergeSort(arr)
    # quickSort(arr, 0, len(arr)-1)
    # countSortA(arr)
    # countSortB(arr)
    # radixSortNumber(strNumber)
    radixSortString(strString)
    # bucketSort(flo, 5)
    # print(ord("abcd"[0]))
    # print(arr)
    # test("arr")
