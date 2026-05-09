# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert node with value x after pth node
    def addNode(self, p, x):
        new_node = Node(x)

        temp = self.head

        # Move to pth node
        for _ in range(p):
            temp = temp.next

        # Insert new node
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

        return self.head

    # Print Doubly Linked List
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end="")
            if temp.next:
                print(" <-> ", end="")
            temp = temp.next
        print()


# Driver Code
dll = DoublyLinkedList()

# Creating list: 2 <-> 4 <-> 5
dll.append(2)
dll.append(4)
dll.append(5)

p = 2
x = 6

dll.addNode(p, x)

dll.display()