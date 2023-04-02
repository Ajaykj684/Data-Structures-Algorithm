"""
A linked list is a data structure consisting of a sequence of nodes, where each node contains a 
piece of data and a reference to the next node in the sequence. The first node is called the head, 
and the last node points to null.

Linked lists can be 
  --> singly linked (each node has a reference to the next node only), 
  --> doubly linked (each node has a reference to both the next and previous nodes), or 
  --> circular (the last node points to the first node).

"""


# Lets implement a singly linked list :

class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None


    #adds a new node with the given data to the end of the list
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return 
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node


    # adds a new node with the given data to the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # adds a new node with the given data after the specified node
    def insert_after_node(self, node, data):
        if not node:
            print("Node not found")
            return
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node


    # removes the node with the given data from the list
    def delete_node(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


    # prints the entire list
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next




linked_list = LinkedList()

# Append some data to the list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Prepend some data to the list
linked_list.prepend(0)

# Insert a node after a given node
node = linked_list.head.next
linked_list.insert_after_node(node, 1.5)

# Delete a node from the list
linked_list.delete_node(2)

# Print the entire list
linked_list.print_list()
