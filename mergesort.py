def merge_sort(a):
    if(len(a) > 1):
        mid = len(a)//2
        L = a[:mid]
        merge_sort(L)
        R = a[mid:]
        merge_sort(R)
        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i]>R[j]:
                a[k]=R[j]
                k+=1
                j+=1
            else:
                a[k]=L[i]
                k+=1
                i+=1
        while i<len(L):
            a[k]=L[i]
            k+=1
            i+=1
        while j<len(R):
            a[k]=R[j]
            k+=1
            j+=1

arr=[1,2,4,5,6,3,4,77,88,11,22,33,1,2,6]
merge_sort(arr)
print(arr)
