# Types of items inserted must have a __eq__ overload
class Node:
    def __init__(self, item, nxt):
        self.item = item
        self.nxt = nxt

class Bag:
    def __init__(self):
        self.start = None

    def insert(self, item):
        if self.exists(item):
            return False
        self.start = Node(item, self.start)
        return True
    
    def delete(self, item):
        if not self.exists(item):
            return False
        
        if self.start.item == item:
            self.start = self.start.nxt
            return True

        current = self.start
        while current.nxt.item != item:
            current = current.nxt

        current.nxt = current.nxt.nxt
        return True

    def retrieve(self, item):
        current = self.start
        while current:
            if current.item == item:
                return current.item
            current = current.nxt
        return None
    
    def exists(self, item):
        current = self.start
        while current:
            if current.item == item:
                return True
            current = current.nxt
        return False

    def size(self):
        current = self.start
        total = 0
        while current:
            total += 1
            current = current.nxt
        return total

    def __iter__(self):
        current = self.start
        while current:
            yield current.item
            current = current.nxt


