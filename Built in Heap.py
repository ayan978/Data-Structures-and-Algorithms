from heapq import *

#Defining a list

nums = [10,2,3,14,12,22,25,5]

heap = []

heappush(heap,nums)
heapify(heap)
while heap:
    print(heappop(heap))
