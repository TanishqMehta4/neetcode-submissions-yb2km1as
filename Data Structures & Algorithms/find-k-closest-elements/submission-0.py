class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []

        for i,num in enumerate(arr):
            heapq.heappush(minHeap,(abs(num-x),i))

        res = []

        while k > 0:
            idx = heapq.heappop(minHeap)[1]
            res.append(arr[idx])
            k-=1
        res.sort()
        return res