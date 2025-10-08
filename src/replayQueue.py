from match import Match

class Node:
    def __init__(self, match: Match):
        self.match = match
        self.next = None

class ReplayQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, match: Match):
        new_node = Node(match)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self) -> Match | None:
        if self.is_empty():
            return None
        removed_match = self.head.match
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return removed_match

    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size