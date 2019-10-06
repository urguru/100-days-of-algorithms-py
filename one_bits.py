def count_one_bits(n):
    x=1
    c=0
    while x<=n:
        if x & n:
            c+=1
        x=x<<1
    return c

print(count_one_bits(127))