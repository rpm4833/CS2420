import random
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
    freq = [0] * (max(A) + 1)
    for num in A:
        freq[num] += 1

    k = 0
    for i in range(len(freq)):
        val = i
        count = freq[i]
        for j in range(count):
            A[k] = val
            k += 1

def main():
    a = CreateRandomList(1000)
    b = copy.deepcopy(a)
    a.sort()
    c = copy.deepcopy(a)
    d = copy.deepcopy(a)

    BubbleSort(b)
    print(b == a)

    ShakerSort(c)
    print(c == a)

    CountingSort(d)
    print(d == a)

if __name__ == "__main__":
    main()