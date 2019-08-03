while True:
    n=str(input("enterusername "))
    l=str(input("enterpass "))
    o=str(input("reenterpass "))
    m=str(input("enteremail "))
    
    if "@" not in m and len(m)<8 and l!=o and m.isdigit():
        print('reen')
    else:
        print("accessed")
        break