
students = {1:'John',2:'Steven',3:'Roberts',4:'Jack',5:'Ricky',6:'Jacob'}

Prog = {'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}} #List and Dictionary inside Dictionary

print(students[3])

print(students.get(2))

students.update({4:'Nathan'})

print(students)

del students[6]

print(students)

students.pop(5)

print(students)

print(Prog['Python'][1])
print(Prog['Java']['JSE'])

#Taking user input for dictionary

StudentsInfo = {}
n = int(input("Enter number of elements : "))

for i in range(n):
    k = input("Enter key : ")
    v = input("Enter value : ")
    StudentsInfo.update({k:v})

print(StudentsInfo)

