#
# Stack is a LIFO Datastructure
#
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        ''' Adds item to top of Stack '''
        self.items.append(item)

    def pop(self):
        ''' Remove item from top of stack '''
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        '''Returns a copy of the top item in the stack '''
        return self.items[:-1]

    def size(self):
        ''' Returns size of stack '''
        return len(self.items)


#
# Queue is a FIFO Datastructure
#
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(item):
        ''' Adds item to the end of queue '''
        self.items.append(item)

    def dequeue():
        ''' Returns the item at front of queue '''
        self.item.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        ''' Returns size of queue '''
        return len(self.items)


#
# Double ended Queue
#
class DeQueue:
    def __init__(self):
        self.items = []

    def addToFront(item):
        ''' Adds item to the front of queue '''
        self.items.insert(0, item)

    def addToEnd(item):
        ''' Adds item to the end of queue '''
        self.items.append(item)

    def removeFromFront():
        ''' Returns the item at front of queue '''
        self.item.pop(0)

    def removeFromEnd():
        ''' Returns the item at front of queue '''
        self.item.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        ''' Returns size of queue '''
        return len(self.items)
