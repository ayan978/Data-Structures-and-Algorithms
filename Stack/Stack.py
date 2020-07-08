class Stack:

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def print(self):
        for i in range(len(self.items) - 1, -1, -1):
            print(self.items[i])
            
         
s = Stack()

s.push(10)
s.push(15)
s.push(18)
s.push(21)
s.print()
