# import random
# a=random.randint(-100,100)
# b=random.randint(-100,100)
# c=random.randint(-100,100)
# d=random.randint(-100,100)
# e=random.randint(-100,100)



a=[int(x) for x in input().split(",")]

for i in range(len(a)):
    if a[i]%2==0:
        print(a[i])
 