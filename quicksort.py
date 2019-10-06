def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    
def partition(arr,low,high):
    i=low-1
    j=low
    pivot=arr[high]
    for x in range(low,high):
        if arr[x]<=pivot:
            i+=1
            arr[x],arr[i]=arr[i],arr[x]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

arr=[1,6,5,4,3,9,8]
quicksort(arr,0,len(arr)-1)
print(arr)

