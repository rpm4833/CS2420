from bag_binary_search import Bag as BSTBag
from student import Student
from time import time

bag = BSTBag()

start = time()
with open('FakeNames.txt', 'r') as file:
    for line in file:
        values = line.split()
        student = Student(values[0], values[1], values[2], values[3], values[4])
        if not bag.insert(student):
            print(f"{student.first} {student.last} could not be added!")
end = time()
print(f"Insertion took {(end - start):.4f} seconds. Total students: {bag.size()}")