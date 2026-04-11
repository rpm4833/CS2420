# Types of items inserted must have overloaded comparison operators and __hash__
from math import sqrt
class Bag:
    def __init__(self):
        self.table_size = 0
        table_capacity = 100
        while not self.is_prime(table_capacity):
            table_capacity += 1
        self.table = [None] * table_capacity

    def insert(self, item):
        if self.exists(item):
            return False
        
        if self.size() >= 2/3 * self.capacity():
            self.resize()
        
        key = hash(item)
        index = key % self.capacity()
        while True:
            if not self.table[index]:
                self.table[index] = item
                self.table_size += 1
                return True
            
            index = (index + 1) % self.capacity()
    
    def delete(self, item):
        if not self.exists(item):
            return False
        
        key = hash(item)
        index = key % self.capacity()
        while True:
            if self.table[index] and self.table[index] == item:
                self.table[index] = False
                self.table_size -= 1
                return True
            
            index = (index + 1) % self.capacity()

    def retrieve(self, item):
        key = hash(item)
        index = key % self.capacity()
        start_index = index
        while True:
            if self.table[index] is None:
                return None
            if self.table[index] and self.table[index] == item:
                return self.table[index]
            
            index = (index + 1) % self.capacity()

            if index == start_index:
                return None
    
    def exists(self, item):
        key = hash(item)
        index = key % self.capacity()
        start_index = index
        while True:
            if self.table[index] is None:
                return False
            if self.table[index] and self.table[index] == item:
                return True
            
            index = (index + 1) % self.capacity()
            
            if index == start_index:
                return None

    def resize(self):
        new_table = self.capacity() * 2 + 1
        while not self.is_prime(new_table):
            new_table += 2
        old_table = self.table
        self.table = [None] * new_table
        self.table_size = 0
        for item in old_table:
            if item:
                self.insert(item)

    def size(self):
        return self.table_size
    
    def capacity(self):
        return len(self.table)

    def __iter__(self):
        for item in self.table:
            if item:
                yield item

    @staticmethod
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        
        for i in range(3, int(sqrt(num)) + 1, 2):
            if num % i == 0:
                return False

        return True
    