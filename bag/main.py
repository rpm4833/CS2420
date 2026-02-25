from bag_pylist import Bag
from student import Student
from time import time

def main():
    bag = Bag()

    # Insertion
    start = time()
    with open('FakeNames.txt', 'r') as file:
        for line in file:
            values = line.split()
            student = Student(values[0], values[1], values[2], values[3], values[4])
            if not bag.insert(student):
                print(f"{student.first} {student.last} could not be added!")
    end = time()
    print(f"Insertion took {(end - start):.2f} seconds. Total students: {bag.size()}")

    # Deletion
    start = time()
    with open('DeleteNames.txt', 'r') as file:
        for line in file:
            temp = Student("", "", line.strip(), "", "")
            if not bag.delete(temp):
                print(f"Student with SSN {temp.ssn} not found!")
    end = time()
    print(f"Deletion took {(end - start):.2f} seconds. Total students: {bag.size()}")

    # Iteration
    start = time()
    ages = 0
    total = 0
    for item in bag:
        ages += int(item.age)
        total += 1
    end = time()
    print(f"Iteration took {(end - start):.4f} seconds. Average age of all students: {(ages / total):.4}")
    
    # Retrieval
    start = time()
    ages = 0
    total = 0
    with open('RetrieveNames.txt', 'r') as file:
        for line in file:
            temp = Student("", "", line.strip(), "", "")
            rtemp = bag.retrieve(temp)
            if type(rtemp) == Student:
                ages += int(rtemp.age)
                total += 1
            else:
                print(f"Student with SSN {temp.ssn} not found!")
    end = time()
    print(f"Retrieval took {(end - start):.2f} seconds. Average age of retrieved students: {(ages / total):.4}.")
    

if __name__ == "__main__":
    main()