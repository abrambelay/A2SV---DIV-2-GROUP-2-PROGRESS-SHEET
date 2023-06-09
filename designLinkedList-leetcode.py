class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if  index>=self.size:return -1
        node = self.head
        for i in range(index-1,-1,-1):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        if not self.head:
            node = Node(val)
            self.head = node
        else:
            node = self.head
            while node.next:
                node = node.next
            tail = Node(val)
            node.next = tail
            self.tail = tail
        self.size+=1
    def addAtIndex(self, index: int, val: int) -> None:
        if self.size>=index:
            if self.size==0:
                self.head = Node(val)
                print(self.head.val)
            else:
                if index==0:
                    node = Node(val)
                    node.next = self.head
                    self.head = node
                else:
                    node = self.head
                    for i in range(index-1,0,-1):
                        node = node.next
                    next = node.next
                    newNode = Node(val)
                    newNode.next = next
                    node.next = newNode
            self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if self.size>index:
            if index==0:
                self.head = self.head.next
            else:
                node = self.head
                for i in range(index-1,0,-1):
                    node = node.next
                node.next = node.next.next
            self.size-=1

        

