"""
A queue is a data structure that allows you to add and remove elements in a first-in, first-out (FIFO) order. 
In other words, the first element added to the queue is the first one to be removed.

"""



from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)                # Adds an item to the back of the queue.

    def dequeue(self):
        if len(self._items) == 0:
            raise ValueError('Queue is empty')
        return self._items.popleft()            # Removes and returns the item at the front of the queue. Raises a ValueError if the queue is empty.

    def is_empty(self):
        return len(self._items) == 0            #  Returns True if the queue is empty, False otherwise.

    def size(self):
        return len(self._items)                 # Returns the number of items in the queue.
    

    def AllItems(self):
        return self._items                 # Returns All items in the queue.






q = Queue()

# Add some items to the queue
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Remove and print the first item in the queue
print(q.dequeue())  

# Check if the queue is empty
print(q.is_empty())  

# Print the size of the queue
print(q.size()) 

# Print all items in the queue
print(q.AllItems()) 
