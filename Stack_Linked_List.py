
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = self.temp = None
        self.size = 0

    def isEmpty(self):
        return self.top == None

    def push(self, data):
        n = node(data)
        n.next = self.top
        self.top = n
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.temp = self.top
            self.top = self.top.next
            self.temp.next = None
            self.size -= 1

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data

    def __len__(self):
        return self.size

    def display(self):
        if self.isEmpty():
            print('Stack is empty')
        self.temp = self.top
        while self.temp is not None:
            print(self.temp.data)
            self.temp = self.temp.next

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.display()


print(s.isEmpty())

