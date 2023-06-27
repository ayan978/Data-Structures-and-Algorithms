
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rare = self.temp = None
        self.size = 0

    def is_Full(self):
        n = node
        return n is None

    def is_Empty(self):
        return self.front is None

    def enqueue(self, data):
        if self.is_Full():
            return None

        n = node(data)
        if self.front is None:
            self.front = self.rare = n
        else:
            self.rare.next = n
            self.rare = self.rare.next
        self.size += 1

    def dequeue(self):
        if self.is_Empty():
            return None

        self.temp = self.front
        self.front = self.front.next
        self.temp.next = None

        self.size -= 1

    def __len__(self):
        return self.list.size

    def print(self):
        if self.is_Empty():
            print('The queue is empty')
        else:
            self.temp = self.front
            while self.temp:
                print(self.temp.data, end=' ')
                self.temp = self.temp.next
            print()


quetype = Queue()
quetype.enqueue(10)
quetype.enqueue(20)
quetype.enqueue(30)
quetype.enqueue(40)
quetype.enqueue(50)
quetype.enqueue(60)
quetype.print()

quetype.dequeue()
quetype.dequeue()
quetype.print()
