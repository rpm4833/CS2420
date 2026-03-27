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
        
        new = Node(item)
        self.root = self.insertR(new, self.root)
        return True

    def insertR(self, new, current):
        if current is None:
            current = new
        elif new.item < current.item:
            current.l = self.insertR(new, current.l)
        else:
            current.r = self.insertR(new, current.r)
        return current
    
    def delete(self, item):
        if not self.exists(item):
            return False
        
        self.root = self.deleteR(item, self.root)
        return True
    
    def deleteR(self, item, current):
        if item == current.item:
            if not current.l and not current.r:     # leaf node
                current = None
            elif not current.l:                     # right-child node
                current = current.r
            elif not current.r:                     # left-child node
                current = current.l
            else:                                   # two-child node
                predecessor = current.l
                while predecessor.r:
                    predecessor = predecessor.r
                current.item = predecessor.item
                current.l = self.deleteR(predecessor.item, current.l)

        elif item < current.item:
            current.l = self.deleteR(item, current.l)
        else:
            current.r = self.deleteR(item, current.r)

        return current

    def retrieve(self, item):
        return self.retrieveR(item, self.root)

    def retrieveR(self, item, current):
        if current is None:
            return None
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