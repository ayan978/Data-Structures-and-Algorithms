
class dequeue:

    def __init__(self):
        self.items = []


    def add_front(self,data):
        self.items.insert(0,data)

    def add_rear(self,data):
        self.items.append(data)

    def remove_front(self):
        if self.items:
            value = self.items.pop(0)
            return value
        else:
            return None

    def remove_rear(self):
        if self.items:
            value = self.items.pop()
            return value
        else:
            return None

    def is_empty(self):
        if self.items==[]:
            return True
        else:
            return False

    def size(self):
        if self.items==[]:
            return None
        else:
            return len(self.items)

    def __repr__(self):
        return "Object : {}".format(self.items)

    def peek_front(self):
        return self.items[0]

    def peek_rear(self):
        return self.items[-1]

    def print(self):
        for i in self.items:
            print(i,end=" ")
        print()

dq = dequeue()
dq.add_front(1)
dq.add_front(2)
dq.add_front(3)
dq.add_rear(0)
print(dq.peek_front())
print(dq.peek_rear())
dq.print()

