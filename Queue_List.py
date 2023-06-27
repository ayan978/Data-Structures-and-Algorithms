class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.items:
            data = self.items.pop(0)
            return data
        else:
            return None

    def peek(self):
        if self.items == []:
            return self.items[-1]

    def is_empty(self):
         return self.items == []

    def size(self):
        return len(self.items)

    def print(self):
        if self.items:
            for i in self.items:
                print(i, end=" ")
        else:
            print("Queue is empty")
        print()


q = Queue()

q.enqueue(2)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.print()
q.dequeue()
q.dequeue()
q.print()
q.dequeue()
q.dequeue()
q.dequeue()

q.print()
