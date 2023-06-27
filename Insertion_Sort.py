#Best Case: O(n), when the array is sorted
#Average Case: O(n^2)
#Worst Case: O(n^2), when the array is reversed

def insertion_sort(list1):
    for j in range(1,len(list1)):
        key = list1[j]
        i = j-1
        while i>-1 and list1[i]>key:
            list1[i+1] = list1[i]
            i -= 1
        list1[i+1] = key

    return list1


print(insertion_sort([-50,60,-2,25,-1,100,95,5000]))
print(insertion_sort([1000,10,19,5,400,7,350]))
