from math import sqrt
def get_primes(n):
    a=[True for i in range(n+1)]
    for i in range(2,int(sqrt(n))):
        for j in range(i+1,n+1): 
            if j%i==0:
                a[j] = False
    res=[]
    for i in range(2,n+1):
        if a[i]==True:
            res.append(i)
    return len(res)

print(get_primes(100000))
