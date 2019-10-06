def permute_string(so_far, remaining):
    if remaining == '':
        print(so_far)
    else:
        for i in range(len(remaining)):
            permute_string(so_far+remaining[i:i+1],remaining[0:i]+remaining[i+1:])

permute_string('', 'hello')

def tostring(lst):
    return ''.join(lst)

def permute_string2(a,l,r):
    if l==r:
        print(tostring(a))
    else:
        for i in range(l,r+1):
            a[i],a[l]=a[l],a[i]
            permute_string2(a,l+1,r)
            a[i],a[l]=a[l],a[i]


a=list(input("Enter a string"))
print(a)
permute_string2(a,0,len(a)-1)
