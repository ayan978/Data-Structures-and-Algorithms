#Time_Complexity : O(n^2)

def selection_sort(list1):
    for i in range(len(list1)-1):
        index = i
        for j in range(i+1,len(list1)):
            if list1[j] < list1[index]:
                index = j
        if index != i:
            swap(list1, index, i)

    return list1

def swap(list1, a, b):
    temp = list1[a]
    list1[a] = list1[b]
    list1[b] = temp

print(selection_sort([-300,10,5,1,-150,110,105,370]))
print(selection_sort([100,5,3,9,150,110,11]))
print(selection_sort([5,2,1,7,6,8,8,0]))
print(selection_sort([100,0,10,8,110,7,6,-2,105]))
