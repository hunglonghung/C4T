from turtle import*
n=int(input("enter a number"))
c=180*(n-2)/n
for i in range(1,n+1):
    forward(200)
    left(180-c)
mainloop()


