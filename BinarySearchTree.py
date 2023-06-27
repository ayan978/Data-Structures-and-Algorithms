class Node:
    def __init__(self, data):
        self.leftChild = None
        self.data = data
        self.rightChild = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # If the tree is balanced O(logN), if it's not balanced O(N)
    def insert(self, data):
        if not self.root:  # it means if self.root is None
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data)

        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data)


    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.remove_node(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.remove_node(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                del node
                return None
            if not node.leftChild:
                temp_node = node.rightChild
                del node
                return temp_node

            elif not node.rightChild:
                temp_node = node.leftChild
                del node
                return temp_node

            temp_node = self.get_predecessor(node.leftChild)
            node.data = temp_node.data
            node.leftChild = self.remove_node(temp_node.data, node.leftChild)
        return node

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        return node

    def get_min_value(self):
        if self.root:  # If self.root is not None
            return self.get_min(self.root)
        else:
            return None

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        return node.data

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        return node.data

    def in_order(self):
        if self.root:
            self.in_order1(self.root)
        else:
            return None

    def in_order1(self, node):
        if node.leftChild:
            self.in_order1(node.leftChild)
        print(node.data, end=" ")
        if node.rightChild:
            self.in_order1(node.rightChild)

    def pre_order(self):
        if self.root:
            self.pre_order1(self.root)
        else:
            return None

    def pre_order1(self, node):

        print(node.data, end=" ")

        if node.leftChild:
            self.pre_order1(node.leftChild)

        if node.rightChild:
            self.pre_order1(node.rightChild)

    def post_order(self):
        if self.root:
            self.post_order1(self.root)
        else:
            return None

    def post_order1(self, node):

        if node.leftChild:
            self.post_order1(node.leftChild)

        if node.rightChild:
            self.post_order1(node.rightChild)

        print(node.data, end=" ")
    


b = BinarySearchTree()
b.insert(40)
b.insert(20)
b.insert(10)
b.insert(30)
b.insert(60)
b.insert(50)
b.insert(70)

b.in_order()
print()
print(b.get_max_value())
b.post_order()
b.remove(50)
print()
b.in_order()
print()
b.post_order()
print()
b.pre_order()
