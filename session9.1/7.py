import random
while True:
    n=random.randint(0,100)
    l=random.randint(0,100)
    o=random.randint(0,100)
    a=random.randint(0,3)

    sign=""
    result=""

    if a==0:
        sign="+"   
        result=n+l
        
        
        print(n,sign,l,'=',o)
        b=str(input("true or false"))
        print(b)

        if b=="true":
            if o==result:
                print("correct")
            if o!=result:
                print("wrong")
        if b=="false" :
            if o==result:
                print("wrong")
            if o!=result:
                print("correct")
            
    if a==1:
        sign="-"   
        result=n-l
        
        print(n,sign,l,'=',o)
        b=str(input("true or false"))
        print(b)
        if b=="true":
            if o==result:
                print("correct")
            if o!=result:
                print("wrong")
        if b=="false" :
            if o==result:
                print("wrong")
            if o!=result:
                print("correct")
    if a==2:
        sign="*"   
        result=n*l
        
    
        print(n,sign,l,'=',o)
        b=str(input("true or false"))
        print(b)
        if b=="true":
            if o==result:
                print("correct")
            if o!=result:
                print("wrong")
        if b=="false" :
            if o==result:
                print("wrong")
            if o!=result:
                print("correct")
    if a==3:
        sign="/"   
        result=n/l
        
        print(n,sign,l,'=',o)
        b=str(input("true or false"))
        print(b)
        if b=='true':
            if o==result:
                print("correct")
            if o!=result:
                print("wrong")
        if b=="false" :
            if o==result:
                print("wrong")
            if o!=result:
                print("correct")
    



        
