#Time Complexity(Best Case, Average Case) : O( nlogn)
#Time Complexity(Best Case, Average Case) : O(n^2)
def swap(list1,a,b):
    temp = list1[a]
    list1[a] = list1[b]
    list1[b] = temp

def partition(list1,p,r):
    x = list1[r]
    j = p-1
    for i in range(p,r):
        if list1[i] <= x:
            j += 1
            swap(list1,j,i)
    swap(list1,j+1,r)
    return j+1


def Quick_Sort(list1,p,r):
    if p<r:
        q = partition(list1,p,r)
        Quick_Sort(list1,p,q-1)
        Quick_Sort(list1,q+1,r)


list1 = [10,9,-30,-35,56,-10,75,70,110,100]
list2 = [500,110,105,75,130,650,600]
Quick_Sort(list1,0,9)
Quick_Sort(list2,0,6)
print(list1)
print(list2)