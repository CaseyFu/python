"""
二叉堆, 优先级队列, 最常用最大堆

插入: 在堆最后插入, 然后上浮
删除: 在堆顶插入, 然后下沉

"""


class BiHeap:
    # 优先级队列 最大堆
    def swimMax(self, heap: list, key: int):
        """上浮最大值, 成最大堆"""
        val = heap[key]
        while(key > 0 and heap[(key-1) >> 1] < val):
            heap[key] = heap[(key-1) >> 1]
            key = (key-1) >> 1
        heap[key] = val

    def sinkMax(self, arr: list, parentIndex: int, length: int):
        """下沉最大值, 用于构建最大堆"""
        val = arr[parentIndex]
        childIndex = 2*parentIndex + 1
        while(childIndex < length):
            if(childIndex+1 < length and arr[childIndex+1] > arr[childIndex]):
                childIndex += 1
            if(val >= arr[childIndex]):
                break
            arr[parentIndex] = arr[childIndex]
            parentIndex = childIndex
            childIndex = 2*parentIndex + 1
        arr[parentIndex] = val

    def insertMax(self, heap: list, e: int):
        """在堆底插入节点, 然后上浮"""
        heap.append(e)
        print(heap)
        self.swimMax(heap, len(heap)-1)

    def delMax(self, maxHeap: list):
        """删除最大值, 即删除最大堆的堆顶, 先把最大堆堆顶与最后一个节点对调, 删除最后一个节点, 堆顶下沉"""
        t = maxHeap[0]
        maxHeap[0] = maxHeap[len(maxHeap)-1]
        maxHeap[len(maxHeap)-1] = t
        maxHeap.pop()
        self.sinkMax(maxHeap, 0, len(maxHeap))

    def buildMaxHeap(self, arr: int):
        """构建最大堆, 从最后一个非叶子节点开始下沉"""
        for i in range((len(arr)-2) >> 1, -1, -1):
            self.sinkMax(arr, i, len(arr))

    # 最小堆操作
    def swimMin(self, arr: list, key: int):
        """上浮最小值, 成最小堆"""
        val = arr[key]
        while(key > 1 and arr[(key-1) >> 1] > val):
            arr[key] = arr[(key-1) >> 1]
            key = (key-1) >> 1
        arr[key] = val

    def sinkMin(self, arr: list, parentIndex: int, length: int):
        """最小堆的下沉"""
        val = arr[parentIndex]
        childIndex = 2*parentIndex + 1
        while(childIndex < length):
            if(childIndex+1 < length and arr[childIndex+1] < arr[childIndex]):
                childIndex += 1
            if(val <= arr[childIndex]):
                break
            arr[parentIndex] = arr[childIndex]
            parentIndex = childIndex
            childIndex = 2*parentIndex + 1
        arr[parentIndex] = val

    def insertMin(self, arr: list, e: int):
        """在堆底插入节点, 然后上浮"""
        arr.append(e)
        self.swimMin(arr, len(arr)-1)

    def buildMinHeap(self, heap: list):
        """构建最小堆, 从最后一个非叶子节点开始下沉"""
        for i in range((len(heap)-2) >> 1, -1, -1):
            self.sinkMin(heap, i, len(arr))

    def heapSort(self, arr: list):
        """堆排序"""
        self.buildMaxHeap(arr)
        print(arr)
        for i in range(len(arr)-1, 0, -1):
            t = arr[i]
            arr[i] = arr[0]
            arr[0] = t
            self.sinkMax(arr, 0, i)
        print(arr)

    def test(self) -> str:
        return 1


heap = BiHeap()
arr = [9, 1, 8, 2, 7, 3, 0, 4, 6, 5]
# heap.heapSort(arr)

# heap.buildMaxHeap(arr)
# # heap.delMax(arr)
# print(arr)
# heap.insertMax(arr, 10)
# print(arr)
print(type(heap.test()))
# print("type(heap.test())")
