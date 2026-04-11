class Student:
    def __init__(self, last, first, ssn, email, age):
        self.first = first
        self.last = last
        self.ssn = ssn
        self.email = email
        self.age = age
    
    def __eq__(self, other):
        return self.ssn == other.ssn
    
    def __ne__(self, other):
        return self.ssn != other.ssn
    
    def __lt__(self, other):
        return self.ssn < other.ssn
    
    def __le__(self, other):
        return self.ssn <= other.ssn
    
    def __gt__(self, other):
        return self.ssn > other.ssn
    
    def __ge__(self, other):
        return self.ssn >= other.ssn
    
    def __hash__(self):
        return int(self.ssn.replace('-', ''))