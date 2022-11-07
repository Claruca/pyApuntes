


class Node:
    def __init__(self, name, next=None):
        self.name = name
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        node = self.head
        while node is not None:
            print(node.name)
            node = node.next


    def addBeginning(self,Node):
        newNode = Node
        newNode.next = self.head
        self.head = newNode


listaEn = LinkedList()
first = Node(3)
second = Node(6)
third = Node(2)
listaEn.head = first
listaEn.head.next = second
listaEn.addBeginning(third)

listaEn.printList()
