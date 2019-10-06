def permute(values):
    n=len(values)
    c=0
    for i in (range(n-1)):
        if values[i]<values[i+1]:
            break
        c+=1
    if c==n:
        values[:]=reversed(values[:])
        return values

    c=0
    for i in (range(n-1)):
        if values[i] > values[i+1]:
            break
        c += 1
    if c == n:
        values[n-2:n] = reversed(values[n-2:n])
        return values
    
    for i in reversed(range(n)):
        if values[i-1]<values[i]:
            values[i:]=sorted(values[i:])
            j=i
            while values[i-1]>values[j]:
                j=j+1
            values[i-1],values[j]=values[j],values[i-1]
            values[i:] = sorted(values[i:])
            return values
            
print(permute([1,2,3,8,7,7]))