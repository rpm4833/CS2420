# Types of items inserted must have a __eq__ overload
class Bag:
    def __init__(self):
        self.items = []

    def insert(self, item):
        for value in self.items:
            if value == item:
                return False
        self.items.append(item)
        return True

    def delete(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = self.items[-1]
                self.items.pop()
                return True
        return False

    def retrieve(self, item):
        for value in self.items:
            if value == item:
                return value
        return None

    def exists(self, item):
        for value in self.items:
            if value == item:
                return True
        return False

    def size(self):
        return len(self.items)

    def __iter__(self):
        for item in self.items:
            yield item
