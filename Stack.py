"""
A stack is a data structure that follows the Last In First Out (LIFO) principle. 
This means that the last element added to the stack is the first element to be removed.

"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []     # Checks if the stack is empty by comparing the list to an empty list.

    def push(self, item):
        self.items.append(item)     # Adds an element to the end of the list using the append method.

    def pop(self):
        return self.items.pop()     # Removes and returns the last element from the list using the pop method.

    def peek(self):
        return self.items[-1]       # Returns the last element in the list without removing it.

    def size(self):
        return len(self.items)      # Returns the length of the list.


stack = Stack()

# Push some items onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Print the size of the stack
print(stack.size())  

# Print the top element of the stack
print(stack.peek()) 

# Pop an element off the stack
stack.pop()

print(stack.size())
