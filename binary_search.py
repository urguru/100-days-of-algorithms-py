def binary_search(lst,i,j,key):
    mid=int((i+j)/2)
    if i>j:
        return False
    if lst[mid]==key:
        return True
    elif lst[mid]<key:
        return binary_search(lst,mid+1,j,key)
    else:
        return binary_search(lst,i,mid-1,key)

lst=[1,2,3,4,5,6,7,8,9,10]
print(binary_search(lst,0,8,1))
