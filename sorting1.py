import random
import time
import copy

def CreateRandomList(size):
    return [random.randrange(0, size - 1) for i in range(size)]

def BubbleSort(A):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                sorted = False

def ShakerSort(A):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                sorted = False
        for i in range(len(A) - 1, 0, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                sorted = False

def CountingSort(A):
    pass

def main():
    a = CreateRandomList(100)
    b = copy.deepcopy(a)
    b.sort()
    c = copy.deepcopy(a)
    d = copy.deepcopy(a)
    d.sort()

    start = time.time()
    BubbleSort(a)
    end = time.time()
    elapsedBubble = end - start
    print(a == b)

    start = time.time()
    ShakerSort(c)
    end = time.time()
    elapsedShaker = end - start
    print(c == d)

    print(f"Bubble Sort: {(elapsedBubble*1000):.4f} ms")
    print(f"Shaker Sort: {(elapsedShaker*1000):.4f} ms")

if __name__ == "__main__":
    main()