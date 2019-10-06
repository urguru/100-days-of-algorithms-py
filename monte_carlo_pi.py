import random
def is_in_circle(x,y,r):
    if x**2+y**2<=r**2:
        return True
    return False

def trial(r):
    x=random.randint(-r,r)
    y=random.randint(-r,r)
    if is_in_circle(x,y,r):
        return True
    return False

count=0
for i in range(1000000):
    if trial(100000):
        count+=1
pi=4*(count/1000000)

print(pi)