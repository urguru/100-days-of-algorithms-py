def merge_sort(arr,n):
    temp_arr=[0]*n
    return _merge_sort(arr,temp_arr,0,n-1)

def _merge_sort(arr,temp_arr,left,right):
    inversion_count=0
    mid=(left+right)//2
    if left<right:
        inversion_count=_merge_sort(arr,temp_arr,left,mid)
        inversion_count+=_merge_sort(arr,temp_arr,mid+1,right)
        inversion_count+=merge(arr,temp_arr,left,mid,right)
    return inversion_count

def merge(arr,temp,left,mid,right):
    i=left
    j=mid+1
    k=left
    inversion_count=0
    while i<=mid and j<=right:
        if arr[i]<arr[j]:
            temp[k]=arr[i]
            k+=1
            i+=1
        else:
            temp[k]=arr[j]
            inversion_count+=mid+1-i
            k+=1
            j+=1
    while i<=mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<=right:
        temp[k]=arr[j]
        j+=1
        k+=1
    for m in range(left,right+1):
        arr[m]=temp[m]

    return inversion_count

print(merge_sort([1,3,4,2,5,6,4,3,9],9))
