import random
a=random.randint(-100,100)
b=random.randint(-100,100)
c=random.randint(-100,100)
d=random.randint(-100,100)
e=random.randint(-100,100)
l=(a,b,c,d,e)
print(*l,sep=" ")
z=sum(l)
print(z)
k=a+b+c+d+e
print(k)