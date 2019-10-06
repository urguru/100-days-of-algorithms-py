def subsets(arr,n,r,data,index,i):
    if(r==index):
        for x in range(r):
            print(data[x],end=' ')
        print('')
        return
    if(i>=n):
        return
    data[index]=arr[i]
    subsets(arr,n,r,data,index+1,i+1)
    subsets(arr,n,r,data,index,i+1)

def print_combination(arr,n,r):
    data=list(range(r))
    subsets(arr,n,r,data,0,0)

lst=[]
def subsets2(so_far,remaining):
    if len(remaining)==0:
        lst.append(so_far)
    else:
        subsets2(so_far+remaining[0],remaining[1:])
        subsets2(so_far,remaining[1:])

subsets2('','1234')
lst.sort()
print(lst)

# print_combination([1,2,3,4],4,2)