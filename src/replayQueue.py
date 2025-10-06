from match import Match

class Node:
    def __init__(self, match: Match):
        self.match = match
        self.next = None

class ReplayQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self,match: Match):
        new_node = Node(match)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        print("match queued")

    def dequeue(self) -> Match | None:
        if self.length == 0:
            return None
        
        removed_match = self.head.match
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        self._size -= 1
        return removed_match
