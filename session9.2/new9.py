while True:
    like= ["anime","manga","light novel"]
    a=input("enterword")
    if a=="C":
        l= input("additional favourites:")
        like.append(l)
        print(*like, )
    if a=='R':
        for i in range(len(like)):

            print(like[i])
    if a=='U':
        n=int(input("enterplacenumber:"))
        like[n]=input('replacement')
        print(like)
    if a=='D':
        m=input("number")
        like.pop(m)
        print(like)
    else:
        print("reenter")