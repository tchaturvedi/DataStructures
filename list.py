class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp
        self.size = self.size + 1

    def getSize(self):
        return self.size

    def contains(self, item):
        curr = self.head
        found = False
        while curr != None and not found:
            if curr.getData() == item:
                found = True
            else:
                curr = curr.getNext()
        return found

    def remove(self, item):
        curr = self.head
        previous = None
        found = False
        while curr != None and not found:
            if curr.getData() == item:
                found = True
            else:
                previous = curr
                curr = curr.getNext()

        if previous == None:
            self.head = curr.getNext()
        else:
            previous.setNext(curr.getNext())
        self.size = self.size - 1
