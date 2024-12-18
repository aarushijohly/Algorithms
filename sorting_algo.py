#insertion-sort algorithm

def insertion_sort(A):
    """Sort a list of comaprable elements in a non decreasing order"""
    for i in range(1, len(A)):
        cur = A[i]
        j = i
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur