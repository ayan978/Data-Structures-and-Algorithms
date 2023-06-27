class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        node = Node(data)

        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.tail.next = self.head
        self.size += 1

    def insert(self, pos, data):
        if pos == 0:
            if self.head is None:
                node = Node(data)
                self.head = node
            else:
                temp = self.head
                node = Node(data)
                node.next = self.head
                while temp.next is not self.head:
                    temp = temp.next
                temp.next = node
                self.head = node
        else:
            node = Node(data)
            temp = node
            i = 1
            while i < pos:
                temp = temp.next
                i += 1
            node.next = temp.next
            temp.next = node
        self.size += 1

    def remove(self, data):
        temp = self.head
        while temp.data != data:
            prev = temp
            temp = temp.next
        if temp.data == data:
            if temp == self.head:
                if self.head.next == self.head:
                    self.head.next = None
                    self.head = None
                else:
                    while temp.next is not self.head:
                        temp = temp.next

                    self.head = self.head.next
                    temp.next = self.head

            else:
                prev.next = temp.next
                temp.next = None
                temp = None
            self.size -= 1

    def is_empty(self):
        return self.size==0

    def print(self):
        temp = self.head
        if self.is_empty():
            print("List is empty")
        else:
            print(temp.data, end=" ")
            temp = temp.next
            while temp != self.head:
                print(temp.data, end=" ")
                temp = temp.next
            print()


l = CircularList()
l.add(1)
l.add(4)
l.add(7)
l.add(8)
l.add(10)
l.add(12)
l.print()
l.remove(10)
l.remove(8)
l.remove(1)
l.remove(4)
l.print()
l.remove(7)
l.remove(12)
l.print()

l.add(10)
l.add(20)
l.add(30)
l.add(40)

l.print()

