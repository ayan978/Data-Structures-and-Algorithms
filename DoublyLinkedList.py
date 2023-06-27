class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def add(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def add_first(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.size += 1

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.size += 1

    def insert(self, pos, data):
        node = Node(data)

        if pos == 0:
            if self.is_empty():
                self.head = node
                self.tail = node
                self.size += 1
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node

        else:
            i = 1
            temp = self.head
            while i < pos:
                temp = temp.next
                i += 1
            node.prev = temp
            node.next = temp.next
            if temp.next is not None:
                temp.next.prev = node
            temp.next = node

    def remove(self,value):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp is not None:
                if temp.data == value:
                    if temp == self.head:
                        self.head = self.head.next
                        temp.next = None
                    else:
                        temp.prev.next = temp.next
                        if temp.next is not None:
                            temp.next.prev = temp.prev
                            temp.next = None
                temp = temp.next

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print()


l = DoublyLinkedList()
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.insert(2,6)
l.print()
l.remove(6)
l.print()

