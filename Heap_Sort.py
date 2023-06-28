from heapq import heappush, heappop, heapify


def heap_sort(list1):
    heapify(list1)
    heap = list1.copy()
    list1.clear()

    while heap:
        item = heappop(heap)
        list1.append(item)

    return list1





list1 = [90,85,92,70,10,1,6,9,18,130,115,136]

print(heap_sort(list1))

