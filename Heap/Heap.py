# Constructing max heap

class Heap:

    def __init__(self, size):
        self.size = size
        self.heap = [0]*size
        self.currentPosition = -1

    def isFull(self):
        if self.currentPosition >= self.size:
            return True
        else:
            return False

    def insert(self,data):

        if self.isFull():
            print("Heap is full")
            return
        else:
            self.currentPosition += 1
            self.heap[self.currentPosition] = data
            self.fixUp(self.currentPosition)


    def fixUp(self,index):
        parentIndex = int((index-1)/2)

        while parentIndex>=0 and self.heap[parentIndex]<self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            parentIndex = int((index-1)/2)

    def heapSort(self):

        for i in range(0,self.currentPosition+1):
            temp = self.heap[0]
            print(temp,end=" ")
            self.heap[0] = self.heap[self.currentPosition-i]
            self.heap[self.currentPosition-i] = temp
            self.fixDown(0,self.currentPosition-i-1)
        print()

    def fixDown(self,index,upto):
        while index <= upto:

            leftChild = 2*index+1
            rightChild = 2*index+2

            if leftChild<upto:
                childToSwap = None
                if rightChild>upto:
                    childToSwap = leftChild
                else:
                   if self.heap[leftChild]>self.heap[rightChild]:
                       childToSwap = leftChild
                   else:
                       childToSwap = rightChild
                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break

                index = childToSwap

            else:
               break


h = Heap(5)
h.insert(13)
h.insert(16)
h.insert(4)
h.insert(2)
h.insert(6)
