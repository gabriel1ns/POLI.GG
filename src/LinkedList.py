class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#linked list that will be used on the match history, with (append) and (__iter__) serving a huge role.
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.size += 1

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next