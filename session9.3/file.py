color =["red","green","white","blue"]
print(color)
print("our color list")
for i,n in enumerate(color):
    print(i,".",n)
r=int(input("items to delete:"))
color.pop(r)
for i,n in enumerate(color):
    print(i,".",n)


l=input('items delete name :')
color.remove(l)
for i,n in enumerate(color):
    print(i,".",n)
