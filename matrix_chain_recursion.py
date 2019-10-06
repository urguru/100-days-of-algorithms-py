import sys




def matrix_chain(p,i,j):
    _min = sys.maxsize
    if i==j:
        return 0
    for k in range(i,j):
        count=matrix_chain(p,i,k)+matrix_chain(p,k+1,j)+(p[i-1]*p[k]*p[j])
        if count<_min:
            _min=count

    return _min

arr = [1, 2, 3, 4, 3]; 
n = len(arr); 
  
print("Minimum number of multiplications is ",matrix_chain(arr, 1, n-1)); 
