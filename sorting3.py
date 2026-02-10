import random
import math
import sys


def CreateRandomList(size):
    return [random.randrange(0, size - 1) for i in range(size)]

def MakeMostlySortedData(random_list):
    random_list.sort()
    random_list[0], random_list[-1] = random_list[-1], random_list[0]

def BubbleSort(A, work):
    sorted = False
    while not sorted:
        # Sort forward
        sorted = True
        for i in range(len(A) - 1):
            work[0] += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                sorted = False

def ShakerSort(A, work):
    sorted = False
    while not sorted:
        # Sort forward
        sorted = True
        for i in range(len(A) - 1):
            work[0] += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                sorted = False

        # Sort backward
        for i in range(len(A) - 1, 0, -1):
            work[0] += 1
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                sorted = False

def CountingSort(A, work):
    # Make frequency list
    freq = [0] * (max(A) + 1)
    for num in A:
        freq[num] += 1

    # Copy to frequency list
    k = 0
    for i in range(len(freq)):
        val = i
        count = freq[i]
        for j in range(count):
            A[k] = val
            k += 1
            work[0] += 1

def QuickSortR(A, low, high, mod, work):
    #Base Case
    if high - low <= 0:
        return
    
    #Modify
    if mod:
        mid = (low + high) // 2
        A[low], A[mid] = A[mid], A[low]
        work[0] += 1
    
    #Compare
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        work[0] += 1
        if A[i] <= A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1     

    #Recurse
    pivot_index = lmgt - 1
    A[low], A[pivot_index] = A[pivot_index], A[low]
    QuickSortR(A, low, pivot_index - 1, mod, work)
    QuickSortR(A, pivot_index + 1, high, mod, work)

def QuickSort(A, work):
    # Run quick sort unmodified
    QuickSortR(A, 0, len(A) - 1, False, work)

def ModQuickSort(A, work):
    # Run quick sort modified
    QuickSortR(A, 0, len(A) - 1, True, work)

def MergeSort(A, work):
    #Base Case
    if len(A) <= 1:
        return
    
    #Split
    mid = len(A) // 2
    l = A[:mid]
    r = A[mid:]

    #Recurse
    MergeSort(l, work)
    MergeSort(r, work)

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
        work[0] += 1

    while i < len(l):
        A[k] = l[i]
        i += 1
        k += 1
        work[0] += 1

    while j < len(r):
        A[k] = r[j]
        j += 1
        k += 1
        work[0] += 1

def main():
    sys.setrecursionlimit(5000)
    sorts = [BubbleSort, ShakerSort, CountingSort, MergeSort, QuickSort, ModQuickSort]
    print("Random Data\n")
    print("    Bubble    Shaker    Counting  Merge     Quick     MQuick\n")
    for s in range(3, 13):
        print(f"{s:02}", end="  ")
        for sort in sorts:
            a = CreateRandomList(2**s)
            work = [0]
            sort(a, work)
            print(f"{math.log(work[0], 2):05.2f}", end="     ")
        print("\n") 
    
    print("Mostly Sorted Data\n")
    print("    Bubble    Shaker    Counting  Merge     Quick     MQuick\n")
    for s in range(3, 13):
        print(f"{s:02}", end="  ")
        for sort in sorts:
            a = CreateRandomList(2**s)
            MakeMostlySortedData(a)
            work = [0]
            sort(a, work)
            print(f"{math.log(work[0], 2):05.2f}", end="     ")
        print("\n") 

if __name__ == "__main__":
    main()