from bag_hash import Bag as HashBag
from student import Student
from time import time

bst_small_insertion = 0.1242
bst_small_iteration = 0.0144
bst_small_deletion = 0.0499
bst_small_retrieval = 0.0271

bst_med_insertion = 2.0060
bst_med_iteration = 0.1802
bst_med_deletion = 0.7376
bst_med_retrieval = 0.4483

def main(size):
    bag = HashBag()
    times = []

    # Insertion
    start = time()
    with open(f'FakeNames{size}.txt', 'r') as file:
        for line in file:
            values = line.split()
            student = Student(values[0], values[1], values[2], values[3], values[4])
            if not bag.insert(student):
                print(f"{student.first} {student.last} could not be added!")
    end = time()
    print(f"Insertion took {(end - start):.4f} seconds. Total students: {bag.size()}")
    times.append(end - start)

    # Iteration
    start = time()
    ages = total = 0
    for item in bag:
        ages += int(item.age)
        total += 1
    end = time()
    print(f"Iteration took {(end - start):.4f} seconds. Average age of all students: {(ages / total):.4f}")
    times.append(end - start)
 
    # Deletion
    start = time()
    with open(f'DeleteNames{size}.txt', 'r') as file:
        for line in file:
            temp = Student("", "", line.strip(), "", "")
            if not bag.delete(temp):
                print(f"Student with SSN {temp.ssn} not found!")
    end = time()
    print(f"Deletion took {(end - start):.4f} seconds. Total students: {bag.size()}")
    times.append(end - start)

    # Retrieval
    start = time()
    ages = total = 0
    with open(f'RetrieveNames{size}.txt', 'r') as file:
        for line in file:
            temp = Student("", "", line.strip(), "", "")
            rtemp = bag.retrieve(temp)
            if type(rtemp) == Student:
                ages += int(rtemp.age)
                total += 1
            else:
                print(f"Student with SSN {temp.ssn} not found!")
    end = time()
    print(f"Retrieval took {(end - start):.4f} seconds. Average age of retrieved students: {(ages / total):.4f}.")
    times.append(end - start)

    return times

if __name__ == "__main__":
    small = main("")
    med = main("Medium")
    print(f"BST Small:   | Insertion : {bst_small_insertion:.4f} | Iteration : {bst_small_iteration:.4f} | Deletion : {bst_small_deletion:.4f} | Retrieval : {bst_small_retrieval:.4f} |")
    print(f"Hash Small:  | Insertion : {small[0]:.4f} | Iteration : {small[1]:.4f} | Deletion : {small[2]:.4f} | Retrieval : {small[3]:.4f} |")
    print(f"BST Medium:  | Insertion : {bst_med_insertion:.4f} | Iteration : {bst_med_iteration:.4f} | Deletion : {bst_med_deletion:.4f} | Retrieval : {bst_med_retrieval:.4f} |")
    print(f"Hash Medium: | Insertion : {med[0]:.4f} | Iteration : {med[1]:.4f} | Deletion : {med[2]:.4f} | Retrieval : {med[3]:.4f} |")