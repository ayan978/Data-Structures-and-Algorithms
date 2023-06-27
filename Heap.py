# Constructing max heap

from heapq import heappush, heappop, heapify

heap = []

arr1 = [12,3,-2,6,4,8,9]
heapify(arr1)

for i in arr1:
    heappush(heap, i)

print(heap)
print(arr1)

while heap:
    print(heappop(heap), end=' ')







