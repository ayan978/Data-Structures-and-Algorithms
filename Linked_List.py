class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.temp = None
        self.temp1 = None
        self.prev = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove(self, value):
        if self.head is None:
            return
        else:
            self.temp = self.head
            while self.temp is not None:

                if self.temp.data == value:
                    if self.temp == self.head:
                        self.head = self.head.next
                        self.temp.next = None
                        break
                    else:
                        self.prev.next = self.temp.next
                        self.temp.next = None
                        break
                self.prev = self.temp
                self.temp = self.temp.next
            self.size -= 1

    def remove_first(self):
        self.temp = self.head
        self.head = self.head.next
        self.temp.next = None
        self.size -= 1

    def remove_last(self):
        self.temp = self.head
        while self.temp.next is not self.tail:
            self.temp = self.temp.next
        self.temp.next = self.tail.next
        self.tail = self.temp
        self.size -= 1

    def insert(self, pos, data):
        if pos == 0:
            if self.head is None:
                self.size += 1
                node = Node(data)
                self.head = node
            else:
                self.size += 1
                node = Node(data)
                node.next = self.head
                self.head = node
        else:
            self.size += 1
            node = Node(data)
            self.temp = self.head
            i = 0
            while i < pos:
                self.prev = self.temp
                self.temp = self.temp.next
                i += 1
            self.prev.next = node
            node.next = self.temp


    def insert_sorted(self, data):
        self.temp1 = self.head
        self.temp = None
        n = Node(data)

        while self.temp1 and self.temp1.data < data:
            self.temp = self.temp1
            self.temp1 = self.temp1.next

        n.next = self.temp1

        if self.temp:
            self.temp.next = n

        if self.head == self.temp1:
            self.head = n



    def return_front(self):
        return self.head.data

    def return_back(self):
        return self.tail.data

    def __len__(self):
        return self.size

    def inverse(self):
        self.temp1 = self.head
        self.temp = self.prev = None

        while self.temp1 is not None:
            self.prev = self.temp
            self.temp = self.temp1
            self.temp1 = self.temp1.next
            self.temp.next = self.prev
        self.head = self.temp

    def display(self):

        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()

l = Linked_List()
l.append(1)
l.append(2)
l.append(4)
l.append(5)
l.display()
l.insert_sorted(3)
l.display()
#l.insert(4, 5)
#l.display()
#l.inverse()
#l.display()
#l.inverse()
l.insert_sorted(0)
l.display()
l.insert_sorted(6)
l.display()

