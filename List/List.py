numbers = [3,12,5,6,8,14]

Students = ["John","Michael","Ricky","Steven","George"]

print(Students)

print(Students[2])

print(Students[-1])

print(Students[2:]) #Will print the element at index 2 and all the elements after that

print(Students[1:4]) #Will print elements from index 1 to index 3

Students[2] = "Robert" #Changing the element at index 2
Students.extend(numbers) #Merging two lists
print(Students)
numbers.append(20) #Adding new element 20 to the list
print(numbers)
Students.insert(1,"Robert") #Replace
print(Students)
numbers.remove(8) #The element 8 will be removed
print(numbers)
Students.clear()
print(Students)
Students = ["John","Michael","Michael","Ricky","Steven","George"]
print(Students)
numbers.pop() #Pop the last element
print(numbers)
print(Students.index("Steven"))
print(Students.count("Michael")) #How many times Michael is appeared in the list
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)


numbers2 = numbers.copy()
del numbers2[2:]   #Will delete all the values from index 2 to last index
print(numbers2)

numbers3=[]
ElementNumber = int(input("Enter element number : "))

for i in range(ElementNumber):
    numbers3.append(int(input()))

print(numbers3)


