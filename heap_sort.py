from p_heaps import Heap

def heapsort(A):
    H=Heap()
    l=len(A)
    for i in range(l):
        H.insert(A[i])
    k=l-1
    for i in range(H.csize):
        A[k]=H.delete()
        k=k-1
A=[63,250,835,947,651,28]
print("orignal array is",A)
heapsort(A)
print("sorted array is",A)


 
