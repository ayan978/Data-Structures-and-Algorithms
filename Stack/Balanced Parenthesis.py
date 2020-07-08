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


def BalancedString(string):
    s1 = Stack()

    for i in string:
        if s1.isEmpty():
            s1.push(i)
        elif i == ')' and s1.peek() == '(':
            s1.pop()
        else:
            s1.push(i)

    if s1.isEmpty():
        print("Balanced")
    else:
        print("Not Balanced")


s = Stack()
BalancedString('((()))')
