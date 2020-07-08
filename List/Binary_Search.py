pos = -1


def binarysearch(List, n):
    lower = 0
    upper = len(List) - 1

    while lower <= upper:
        mid = (lower + upper) // 2

        if n == List[mid]:
            globals()['pos'] = mid
            return True
        else:
            if n<List[mid]:
               upper = mid - 1
            else:
               lower = mid + 1
    return False 


List = []
num = int(input("Enter number of elements in list : "))
print("Enter the elements in sorted order : ")

for i in range(num):
    List.append(int(input()))

x = int(input("Enter an element to search : "))
if binarysearch(List, x):
    print("Element is found at index", pos)
else:
    print("Element is not found")


