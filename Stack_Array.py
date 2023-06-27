class Stack:

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        item = self.items.pop()
        return item

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
        if self.isEmpty():
            print('List is empty')
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

def infix_to_postfix(s):
    Precedence = {
        '/' : 4,
        '*' : 3,
        '-' : 2,
        '+' : 1
    }
    s1 = Stack()
    output = ''
    for i in s:
        if i.isdigit():
            output += i
        else:
            if i==' ':
                continue
            elif i=='(':
                s1.push(i)
            elif i==')':
                while not s1.isEmpty() and s1.peek() != '(':
                    item = s1.pop()
                    output += item
                if s1.isEmpty():
                    print('Invalid Expression')
                s1.pop()
            else:
                if not s1.isEmpty():
                    if s1.peek() != '(':
                          while Precedence[s1.peek()] > Precedence[i] and not s1.isEmpty():
                             item = s1.pop()
                             output += item
                          s1.push(i)
                    else:
                        s1.push(i)
                else:
                    s1.push(i)
    s1.print()
    while not s1.isEmpty():
        item = s1.pop()
        output += item

    return output


def precedence_converter(data, pos1):
    p_stack1 = Stack()
    x = int(input(len()))





s = Stack()

s.push(10)
s.push(15)
s.push(18)
s.push(21)
s.print()

BalancedString('((()))')
BalancedString('(()))()')

print(infix_to_postfix('(4+8)*(6-5)/((3-2)*(2+2))'))
