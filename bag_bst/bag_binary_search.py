# Types of items inserted must have overloaded comparison operators
class Node:
    def __init__(self, item):
        self.item = item
        self.l = None
        self.r = None

class Bag:
    def __init__(self):
        self.root = None

    def insert(self, item):
        if self.exists(item):
            return False
        
        n = Node(item)
        self.root = self.insertR(n, self.root)
        return True
    
    def insertR(self, n, current):
        if current is None:
            current = n
        elif n.item < current.item:
            current.l = self.insertR(n, current.l)
        else:
            current.r = self.insertR(n, current.r)
        return current
    
    def delete(self, item):
        pass

    def retrieve(self, item):
        return self.retrieveR(item, self.root)

    def retrieveR(self, item, current):
        if current is None:
            return False
        elif item == current.item:
            return current.item
        elif item < current.item:
            return self.retrieveR(item, current.l)
        else:
            return self.retrieveR(item, current.r)
    
    def exists(self, item):
        return self.existsR(item, self.root)

    def existsR(self, item, current):
        if current is None:
            return False
        elif item == current.item:
            return True
        elif item < current.item:
            return self.existsR(item, current.l)
        else:
            return self.existsR(item, current.r)

    def size(self):
        return self.sizeR(self.root)

    def sizeR(self, current):
        if current is None:
            return 0
        return self.sizeR(current.l) + 1 + self.sizeR(current.r)

    def __iter__(self):
        yield from self.iterR(self.root)
    
    def iterR(self, current):
        if current is not None:
            yield from self.iterR(current.l)
            yield current.item
            yield from self.iterR(current.r)

