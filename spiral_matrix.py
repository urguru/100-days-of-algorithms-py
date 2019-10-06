def spiral_matrix(m,n):
    arr=[[0 for i in range(n)] for j in range(m)]
    value=1
    l,r,t,b=0,m-1,0,n-1
    while l<=r and t<=b:
        for i in range(l,r+1):
            arr[t][i]=value
            value+=1
        # print_matrix(arr,m,n)
        t+=1
        for i in range(t,b+1):
            arr[i][r]=value
            value+=1
        # print_matrix(arr,m,n)
        r-=1
        for i in reversed(range(l,r+1)):
            arr[b][i]=value
            value+=1
        # print_matrix(arr, m, n)
        b-=1
        for i in reversed(range(t,b+1)):
            arr[i][l]=value
            value+=1
        
        l+=1
    print_matrix(arr, m, n)

def print_matrix(arr,m,n):
    for i in range(m):
        for j in range(n):
            print(' ',arr[i][j] ,' ',end=' ')
        print(end='\n')

spiral_matrix(5,5)

