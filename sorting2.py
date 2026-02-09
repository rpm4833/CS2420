import random
import copy

def CreateRandomList(size):
    return [random.randrange(0, size - 1) for i in range(size)]

def QuickSortR(A, low, high, mod):
    #Base Case
    if high - low <= 0:
        return
    
    #Modify
    if mod:
        mid = (low + high) // 2
        A[low], A[mid] = A[mid], A[low]
    
    #Compare
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1     

    #Recurse
    pivot_index = lmgt - 1
    A[low], A[pivot_index] = A[pivot_index], A[low]
    QuickSortR(A, low, pivot_index - 1, mod)
    QuickSortR(A, pivot_index + 1, high, mod)

def QuickSort(A):
    QuickSortR(A, 0, len(A) - 1, False)

def ModQuickSort(A):
    QuickSortR(A, 0, len(A) - 1, True)

def MergeSort(A):
    #Base Case
    if len(A) <= 1:
        return
    
    #Split
    mid = len(A) // 2
    l = A[:mid]
    r = A[mid:]

    #Recurse
    MergeSort(l)
    MergeSort(r)

    #Combine
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            A[k] = l[i]
            i += 1
        else:
            A[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        A[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        A[k] = r[j]
        j += 1
        k += 1


def main():
    a = CreateRandomList(10)
    b = copy.deepcopy(a)
    c = copy.deepcopy(a)
    d = copy.deepcopy(a)
    a.sort()

    QuickSort(b)
    print(b == a)

    ModQuickSort(c)
    print(c == a)

    MergeSort(d)
    print(d == a)


if __name__ == "__main__":
    main()
    